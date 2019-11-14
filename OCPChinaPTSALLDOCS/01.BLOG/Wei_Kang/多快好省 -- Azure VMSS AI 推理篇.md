上一期文章介绍了 Azure Batch + Low Priority VM 的方式实现了成本优化的训练架构，其实训练这种任务式的场景在可接受中断的情况下非常适合 Low Priority VM 来执行，即使中途被中断了也没有关系，可以重新来执行。推理场景就略有不同，推理通常是一个 Always On 永久在线的服务，不太接受中断。Low Priority VM 同时支持 VMSS 服务，但推理场景下 Low Priority VM 可能被抢占召回，这势必会影响推理服务的可用性。所以在推理场景下，可以基于服务可用性的容忍度做进一步区分然后来选择适合产品服务架构，1. 开发测试场景：可接受服务中断，这个时候如果追求成本可以采用 VMSS + Low Priority VM 来部署 GPU 资源来进行推理；2. 一般生产场景，可接受一定服务中断，这个时候如果追求成本可以采用 VMSS + Low Priority VM，其中弹性扩展集中的虚拟机数量可以大于等于2，这样避免 Low Priority VM 同时被抢占召回的可能，但无法避免同时被召回的可能；3. 严格生产场景，不接受服务中断，这个时候还追求成本的话，可以采用 VMSS + Low Priority VM & VMSS + Dedicated VM 的方式，服务前端分配可以通过 Azure Load Balancer 来负载分摊，当极端情况 Low Priority VM 全部被召回场景，Dedicated VM 依然工作。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇1.png)

 
本文以上述一般生产场景部署方案为例，介绍如何结合 VMSS + Low Priority VM 来部署推理模型，本示例中的推理模型采用上一篇文章训练出的 MNIST 模型。操作部中如下：
1. 创建 VMSS + Low Priority VM

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇2.png)

操作系统磁盘镜像选择上一篇文章中所创建的虚拟机镜像，这里采用自定义镜像的好处可以优化部署时间，不需要在增加节点时候费时安装 GPU 相关驱动

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇3.png)


机器类型选择 NC6，实际生产可以依据需要进行替换， 勾选以 Low Priority VM 部署选项，Eviction Policy 选择 Delete。Eviction Policy 是指在出现 Low Priority VM 被抢占召回时对该 VM 的处理操作，Delete 策略即为将被抢占召回的 VM 删除，此处建议 Delete 策略是因为 VMSS 节点数少于预设节点数量时候，VMSS 会尝试重新添加节点，但同时 Delete 策略删除 VM 时也会同步将 VM 所使用的磁盘删除。如果希望对数据做留存，可以选择 Stop/Deallocate

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇4.png)

负载均衡类型选择 Load Balancer

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇5.png)

2. 在 VMSS 上的 upgrade-policy-mode 设置为 automatic，示例中采用 Azure CLI，默认 Portal 创建的 VMSS，该策略为 Manual

`az vmss update --resource-group YOURRESOURCEGROUPNAME --name YOURVMSSNAME --set upgradePolicy.mode=automatic`

3. 创建存储账号，推理模型的部署采用 custom-script 扩展来实现，将计划推送的推理代码和模型打包上传至存储账号
创建存储账户可以访问：https://docs.microsoft.com/en-us/azure/storage/common/storage-quickstart-create-account?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal，获取存储 Key 可参阅：https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?irgwc=1&OCID=AID681541_aff_7806_1246483&tduid=(ir__as11wmbyw0kfrnb6xmlij6lydu2xjyq2zvrd6acb00)(7806)(1246483)(%28b33facbe09bb16a52db15b61562293e1%29%2881561%29%28686431%29%28at106619_a107739_m12_p15155_cSG%29%28%29)(b33facbe09bb16a52db15b61562293e1)&irclickid=_as11wmbyw0kfrnb6xmlij6lydu2xjyq2zvrd6acb00
4. 部署模型代码
已打包好的模型和代码可以直接访问：https://github.com/nonokangwei/AzureVMSSMnist 下载（deploy_mnist_flask.tar.gz 文件）。也可以通过克隆这个 Repo 自己来打包。将打包文件上传至存储账户。示例中将打包文件上传至存储账户 repo 存储容器下。然后同时将 requirements.txt 文件上传至存储容器中。
创建 custom-script 部署文件 customConfig.json 。
```
{
  "commandToExecute": "pip3 install -r requirements.txt && tar -xvzf deploy_mnist_flask.tar.gz && cd deploy_mnist_flask
&& python3 app.py &",
  "storageAccountName": "{YOURSTORAGEACCOUNTNAME}",
  "storageAccountKey": "{YOURSTORAGEACCOUNTKEY}",
  "fileUris": ["https://{YOURSTORAGEACCOUNTNAME}.blob.core.windows.net/repo/deploy_mnist_flask.tar.gz","https://{YOURSTORAGEACCOUNTNAME}.blob.core.win
dows.net/repo/requirements.txt"]
}
```
通过 Azure CLI 进行部署，替换下面指令中的 resource-group 和 vmss-name 名称
```
az vmss extension set --publisher Microsoft.Azure.Extensions --version 2.0 --name CustomScript --extension-instance-name modeldeployupdate --resource-group {YOURRESOURCEGROUPNAME} --vmss-name {YOURVMSSNAME} --protected-settings ./customConfig.json
```
5. 检验部署，获取 VMSS 创建后的配置的 Standard Load Balancer 的公网 IP 地址
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇6.png)

浏览器打开 http://{公网 IP 地址}
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇7.png)

测试推理
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇8.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20VMSS%20AI%20推理篇9.png)

上述介绍了 VMSS + Low Priority VM 的方式部署 GPU 推理模型，前述提到 Low Priority VM 可能会被抢占召回，那是否有方式可以响应抢占召回事件呢？Azure VM Metadata Service 已经提供的对于 Low Priority VM Eviction 事件的支持（"EventType": "Preempt",），可以通过该服务在 30 秒前获得抢占召回事件。基于该事件可以做相应的处理操作，如尝试增加 VMSS 节点（low priority 或 regular），之前写过一篇介绍 Azure Metadata Service 事件处理的文章，大家可以参阅：https://www.cnblogs.com/wekang/p/10455744.html，可以依照文章中的架构进行自己的事件相应逻辑设计。好了今天就介绍到这里，训练推理成本优化搞定，希望对大家有所帮助。
