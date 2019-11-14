今天我们来聊聊 Azure 虚拟机运维的计划运维管理（Scheduled Event），在微软云 Azure 上会出现计划性的运维事件一种是 Azure 平台发起的，一种是客户自主发起的，对于这种可预知的运维事件，是否可以进行有效的发现-管理-响应呢，下面我们就来做个小 demo 来带大家 Get 这个技能。

# 发现：

Azure 上支持将计划性运维事件发布出来，在 Azure 的虚拟机中，可以通过访问 Metadata 的方式来探知计划性运维事件，下面是计划性运维事件的 Schema：

```
{
    "DocumentIncarnation": {IncarnationID},
    "Events": [
        {
            "EventId": {eventID},
            "EventType": "Reboot" | "Redeploy" | "Freeze",
            "ResourceType": "VirtualMachine",
            "Resources": [{resourceName}],
            "EventStatus": "Scheduled" | "Started",
            "NotBefore": {timeInUTC},              
        }
    ]
}
```

其中 EventType 字段标识，即将发生的计划性运维事件，Reboot 标识该运维事件会引起虚拟机重启，Redepoly 标识该运维事件会引起虚拟机在其它物理计算节点部署，Freeze 标识该运维事件会引起虚拟机 CPU 短暂的挂起（主要是针对平台对节点做热升级/热补丁），另外一个关键字段 NotBefore 表示该事件将在什么时间发生。

如何访问此 Metadata，在 VM 节点内可以通过访问虚拟机 metadata endpoint 来取得相应信息，以 Linux VM 为例，可以通过 **curl -H Metadata:true http://169.254.169.254/metadata/scheduledevents?api-version=2017-08-01** 来获取计划运维事件。

# 管理：

当有大量被管理虚拟机时，可以通过分布式在每个虚拟机上运行一个守护进程，该守护进程定时执行来进行计划运维事件发现。采集通过分布式来完成，管理集中化可以方便对事件进行统一处理，这个小 Demo 中以 Azure Event Grid 作为消息队列，当节点上发现计划运维事件后，将消息推送到 Event Grid 服务，以便被后端响应处理程序消费。

```
 1 #!/bin/bash
 2 key="#input your eventgrid topic secret here"
 3 endpoint="#input your eventgrid endpoint here" 
 4 for (( ; ; ))
 5 do
 6    metadata=$(curl -H Metadata:true http://169.254.169.254/metadata/scheduledevents?api-version=2017-08-01 | jq '.Events
 7 []')
 8    if [ -z "$metadata" ]
 9    then
10       sleep 30
11       continue
12    else
13       event='[ {"id": "'"$RANDOM"'", "eventType": "ScheduledEvent", "subject": "metadatademo/demovm", "eventTime": "'`da
14 te +%Y-%m-%dT%H:%M:%S%z`'", "data":'"$metadata"',"dataVersion": "1.0"} ]'
15       curl -X POST -H "aeg-sas-key: $key" -d "$event" $endpoint
16       sleep 30
17    fi
18 done
```

Note：上述 bash 脚本调用了 jq，请保证 runtime 已安装 jq。

# 响应：

发现的计划运维事件放置在 Evnetgrid 消息队列中，即可被响应处理应用来进行消费，在本 Demo 中通过 Azure Logicapp 服务来进行事件响应，当收到事件后邮件通知管理员。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20%E8%99%9A%E6%8B%9F%E6%9C%BA%E8%AE%A1%E5%88%92%E8%BF%90%E7%BB%B4%E7%AE%A1%E7%90%8601.png)

Azure 平台对上述三种计划性运维事件已经定义的最小通知时间窗口，Freeze：10 mins，Reboot：15 mins，Redeploy：10 mins，平台会保证在该时间内用户可以进行相关的响应操作，比如客户可以备份，清理连接，主备切换，日志告警，Graceful shutdown等。

# 测试：

Azure 对于计划性运维时间的支持不仅仅是对平台运维所产生的事件，对于用户操作所产生的事件也是支持的，比如客户在 Portal 中执行 Reboot，Redeploy 操作，大家在测试验证自己的响应逻辑时，可以通过模拟管理操作来进行测试。基本逻辑已经介绍清楚，小伙伴们动手开干吧！

# 学习资料：

1. Azure 虚拟机计划性运维 Metadata 介绍：https://docs.microsoft.com/en-us/azure/virtual-machines/linux/scheduled-events

2. Azure 平台计划性运维发现介绍：https://azure.microsoft.com/en-us/blog/find-out-when-your-virtual-machine-hardware-is-degraded-with-scheduled-events/

3. 揭秘 Azure 平台计划运维与人工智能的结合：https://azure.microsoft.com/en-us/blog/improving-azure-virtual-machine-resiliency-with-predictive-ml-and-live-migration/
