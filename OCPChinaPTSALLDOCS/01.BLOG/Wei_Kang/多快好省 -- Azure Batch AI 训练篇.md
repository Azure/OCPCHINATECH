 今天我们来说一说如何通过 Azure Batch 实现多快好省的 AI 训练。多：Azure 云平台提供各种规格型号的计算服务资源，从 CPU 到 GPU 再到 FPGA，响指一打最新的 V100 卡加持 NVLINK 手到擒来。快：Azure 平台除了基础的计算资源外，还提供其它丰富的产品和工具，使工作效率大大提升，以 Azure Batch 做 AI 训练为例，Batch 服务提供的 SDK 及功能可以方便的帮助我们完成 AI 训练的资源调度和任务管理。好：东西好，价格还好。省：46个区域，计算资源价格高低不一任你选，还不爽？Low Priority 了解一下，价格让你动容，而且 Azure Batch 服务本身是免费的呦。得嘞，口嗨结束，make hands dirty，使用 Azure Batch Low Priority GPU 资源训练 MNIST。 
1. 准备 Azure Batch Account
登陆 Azure Portal，选择 Azure Batch 服务

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20Batch%20AI%20训练篇1.png)

选择添加创建，地区需要注意，每个地区计算资源的价格不同，按照需要进行选择

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20Batch%20AI%20训练篇2.png)

 资源池分配模式选择 Batch service 类型即可
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20Batch%20AI%20训练篇3.png)

创建好后，记录 Batch Account Name 和 Batch Account URL，下例中，Batch Account Name 为 batchaidemo，URL 为 https://batchaidemo.westus2.batch.azure.com

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20Batch%20AI%20训练篇4.png)

2. 创建 Service Principle
创建方法参见：https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal， 记录下Tenant ID，Client ID，Service Principle Secret。
3. 创建 GPU 虚拟机镜像
 此示例中采用 Keras 框架来完成对 Mnist 数据集的深度学习，所以 GPU 的计算资源上需要安装 CUDA 驱动，以及 cuDNN 驱动，这两个驱动预装比较耗时，所以这里面在开启 Batch 计算资源时去做安装会比较耗时，所以这里建议大家可以不采用 Batch 预知的计算镜像，通过自定义镜像来创建。
GPU 相关驱动安装可参阅：https://docs.microsoft.com/en-us/azure/virtual-machines/linux/n-series-driver-setup ，本文后续在 Batch 部分使用的系统版本为 Ubuntu 16.04，所以大家可以可以参阅这个文档中 Ubuntu 系统的 GPU 安装方法进行安装（注：其中 sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub 这部中如果报错，可以采用 wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub，然后通过 sudo apt-key add 7fa2af80.pub 来添加）。cuDNN 的安装可参阅 https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#download 进行安装。
自定义镜像的方式可以参阅如下链接：https://docs.microsoft.com/en-us/azure/virtual-machines/linux/capture-image
镜像创建完毕后，记录镜像的资源 ID：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20Batch%20AI%20训练篇5.png)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/多快好省%20--%20Azure%20Batch%20AI%20训练篇6.png)

4. 创建存储账户，存储账户区域建议与 Batch 在同一区域，记录存储账号名称，以及 Key
创建存储账户可以访问：https://docs.microsoft.com/en-us/azure/storage/common/storage-quickstart-create-account?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal，获取存储 Key 可参阅：https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?irgwc=1&OCID=AID681541_aff_7806_1246483&tduid=(ir__as11wmbyw0kfrnb6xmlij6lydu2xjyq2zvrd6acb00)(7806)(1246483)(%28b33facbe09bb16a52db15b61562293e1%29%2881561%29%28686431%29%28at106619_a107739_m12_p15155_cSG%29%28%29)(b33facbe09bb16a52db15b61562293e1)&irclickid=_as11wmbyw0kfrnb6xmlij6lydu2xjyq2zvrd6acb00
5. 开始 Build
可以访问：https://github.com/nonokangwei/AzureBatchMnist 将代码克隆到本地，然后进行如下操作：

1.在 config.py 中将相关参数替换为前述步骤记录的参数

2.执行 azurebatchdemo.py, 相关程序说明可参见程序注释，这里不做赘述

3.执行结束后，访问输出结果。进入上述所创建的存储账号，找到名称为 (OutputFilePrefix)output 的存储容器，可以看到 model_json, model.h5, stderr.txt, stdout.txt 文件，其中 model_json 和 model.h5 为训练输出模型及描述文件，stderr.txt 为程序执行的错误输出文件，stdout.txt 为程序执行的标准输出（如训练程序中所打印的结果均可以在这里查询）
        本文中通过代码的方式在 Azure Batch 中创建了包含单节点 GPU 算例的计算资源池，通过 StarTask 将 MNIST 训练的程序依赖包进行节点自动安装，然后将 MNIST 训练的代码以及数据集数据通过先创建 Job，然后定义 Task 的方式来调用创建好的计算池进行执行，执行完毕将结果数据导出到存储账户。整个过程中采用了 Low Priorty 低优先级大大降低了运算成本，如果 Low Priority 实例在执行过程中被中断，Azure Batch 中的 Job 和 Task 内置重试功能，会将未完成的任务重新分配到其它可用节点进行执行。除此之外还可以结合 Azure Batch 计算池的 Auto-Scale 自动伸缩能力，结合任务数量来定义伸缩规则来实现自动化的资源分配和回收工作（参见：https://docs.microsoft.com/en-us/azure/batch/batch-automatic-scaling?irgwc=1&OCID=AID681541_aff_7806_1246483&tduid=(ir__as11wmbyw0kfrnb6xmlij6lydu2xjyq30frd6aeb00)(7806)(1246483)(%28b33facbe09bb16a52db15b61562293e1%29%2881561%29%28686431%29%28at106619_a107739_m12_p15155_cSG%29%28%29)(b33facbe09bb16a52db15b61562293e1)&irclickid=_as11wmbyw0kfrnb6xmlij6lydu2xjyq30frd6aeb00）
        好了今天就先到这里，希望上述介绍可以帮助你了解到 Azure Batch 通过 Low Priority 来实现深度学习场景下的一些优势，大家可以结合自己的实际业务场景开始耍拉，传送门 Low Priority 的机器到底有多便宜。还不过瘾，训练场景搞定了，推理场景呢？ 下一期带上你的模型，Low Priority + VMSS 来喽，跟你一起实现低成本 GPU 推理部署架构。
