
上一回我们对 NSG Flow Log 方案的整体架构做了介绍，大家可以参考下面的架构图，快速回忆一下。本文我们主要聚焦在事件驱动的日志注入部分，即架构图中流程中的第一到第三步。
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入1.png)
NSG Flow Log 目前支持的 Export 方式只有持久化到 Blob 存储中，使用的是 Block Blob 类型，NSG Flow Log 以 1 分钟为间隔向 Block Blob 中的日志文件追加 Block，在 Storage Account 内所有日志文件均归属在名为 insights-logs-networksecuritygroupflowevent Blob Container 下，Blob 日志文件的命名规则如下：resourceId=/SUBSCRIPTIONS/{subscriptionID}/RESOURCEGROUPS/{resourceGroupName}/PROVIDERS/MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/{nsgName}/y={year}/m={month}/d={day}/h={hour}/m=00/macAddress={macAddress}/PT1H.json，每一小时都会产生一个独立的 Blob 日志文件，因为同一个 NSG 策略可以被使能在多台虚拟机上，所以在 Blob 命名规则上大家可以看到 macAddress 这个字段用来标识虚拟机网卡的 Mac 地址。在将 Blob 存储的日志流化的实现里面很重要的一个目标就是实时性，上面看到 Blob 存储的 Log 最小的更新周期是 1 分钟，以事件驱动的方式来处理可以满足实时性的要求，当 Blob 中产生新文件或者现有文件有更新时，用该事件驱动后续对日志的处理流程来保证最新的日志被注入到后端的分析引擎。Azure 中的 Event Grid 原生支持 Blob 存储作为事件源，当 Blob 中产生新文件或者现有文件有更新时，Event Grid 可以释放该事件消息。在消费该事件消息时，我们需要知道触发该事件的 Blob 名称，以及该事件产生的新增日志偏移量。我们先来看一下 Blob 变更事件的 Schema ：

```
[{
  "topic": "/subscriptions/{subscription-id}/resourceGroups/Storage/providers/Microsoft.Storage/storageAccounts/xstoretestaccount",
  "subject": "/blobServices/default/containers/testcontainer/blobs/testfile.txt",
  "eventType": "Microsoft.Storage.BlobCreated",
  "eventTime": "2017-06-26T18:41:00.9584103Z",
  "id": "831e1650-001e-001b-66ab-eeb76e069631",
  "data": {
    "api": "PutBlockList",
    "clientRequestId": "6d79dbfb-0e37-4fc4-981f-442c9ca65760",
    "requestId": "831e1650-001e-001b-66ab-eeb76e000000",
    "eTag": "0x8D4BCC2E4835CD0",
    "contentType": "text/plain",
    "contentLength": 524288,
    "blobType": "BlockBlob",
    "url": "https://example.blob.core.windows.net/testcontainer/testfile.txt",
    "sequencer": "00000000000004420000000000028963",
    "storageDiagnostics": {
      "batchId": "b68529f3-68cd-4744-baa4-3c0498ec19f0"
    }
  },
  "dataVersion": "",
  "metadataVersion": "1"
}]
```

其中 data 部分的 url 属性标识了触发事件的 Blob 名称，contentLength 属性标识当前 Blob 文件的总字节大小，新增日志的偏移量可以通过前后两次事件的差值进行计算。偏移量计算要求每次事件处理时对前序事件有依赖关系，所以需要一个持久化存储来记录相同 Blob 文件的前序状态，将 Blob 文件名和 contentLength 记录下来，这是一个典型的 KV 持久化场景，我们选择了 Azure Table Storage 来实现，CosmosDB 也是不错的选择。实现已经介绍清楚，一起来看下配置方法：
1. 创建 NSG Flow Log 存储账号，

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入2.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入3.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入4.png)

2. 打开 NSG Flow Log，Storage Account 指向第一步创建的存储账户

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入5.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入6.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入7.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入8.png)

3. 配置 Event Grid 的 Blob 事件触发器（此步也可跳过，参考 Azure Function ETL 部分），

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入9.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入10.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入11.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20事件驱动的日志注入12.png) 
配置完成了， Blob 事件触发就绪，后续就可以开始 NSG Flow Log 的流式处理啦。未完待续...
