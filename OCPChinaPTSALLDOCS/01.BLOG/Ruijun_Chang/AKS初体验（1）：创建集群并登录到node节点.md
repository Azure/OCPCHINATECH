随着容器的火爆，各家云厂商都推出自己的kubernetes服务，Azure平台上提供的托管kubernetes服务为AKS（Azure Kubernetes Service）。AKS服务本身免费，用户只需为使用的Node虚机付费，master节点由Azure自动创建和维护，用户也无需为master节点付费。下面是一张架构图示：
本篇文章主要带领大家创建一遍AKS集群，一方面方便了解AKS是什么，另一方面为之后的深入介绍做环境准备。
文章主要分为两部分：
（1）AzurePortal、CLI创建集群演示；
（2）SSH登录到AKS Node节点。
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点1.png)
 
（1）AzurePortal、CLI创建集群演示
登录portal.azure.com，搜索Kubernetes Service，选择订阅，资源组，为自己的Cluster命名，DNS name prefix指的是一个用于连接K8S API server的DNS前缀，service principal可以创建一个新的或者指定一个已有的，Azure中的服务本身也是一项需要验证的身份，因为这项服务用到了平台的资源，因此每项服务都需要一个service principal作为身份认证，具体可以参考https://docs.microsoft.com/zh-cn/azure/role-based-access-control/overview中的说明。初次实验，我们先都按照默认配置来，网络以及其他部分会慢慢在后面的文章添加，按照提示输入相关字段后点击创建，等待完成。创建过程中可能会发现，AKS node 选机型的时候默认是一组相同配置的机型，比如你选的是Standard DS2 v2，node count 为3，那么后台就会创建3台DSv2 VM，一组一样的为一个node pool，AKS当然也支持管理多组不同配置的node pool（节点池），这部分可以参考同事的一篇文章：https://mp.weixin.qq.com/s/Z1Wyuhi4wQ75DCoh5PjjGQ。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点2.png)
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点3.png)

创建完集群后，你会发现你的资源组中多了两个而不是一个资源组，这是因为每创建一个AKS集群都会产生两个资源组，一个是你刚创建的那个，记录集群的信息，另一个是自动创建的第二个资源组，MC_myResourceGroup_myAKSCluster_location格式命令，里面有集群所有节点的VM，存储，网络信息：

 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点4.png)
 
CLI命令创建的话，需要 CLI  version 2.0.50以上，为了方便后面的操作，建议直接升级到最新版本，用户可以用 az --verison 查看下当前版本，如果是windows用户，可以按照https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest 操作，macOS 按照https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos?view=azure-cli-latest，windows用户如果是WSL（Windows Subsystem for Linux (WSL)）的更新，建议参照https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest 去一步一步手动更新。
更新完成后我们尝试在中国北2区域创建一个集群，当然还是熟悉的套路，创建资源组，命令的具体参数可以参考https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough，涉及的参数名称也是一目了然，可以跟着链接的介绍直接走一遍。
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点5.png)
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点6.png)

（2）SSH登录到AKS Node节点 
SSH登录node是想重点介绍的，因为作为一个托管的kubernetes平台服务，AKS集群中的master和node都不提供公有IP地址供直接登录，但是用户不可避免要登录到node上去查看比如一些pod信息，日志，或者troubleshooting,AKS提供的进入node的方式是：使用秘钥对，在AKS集群中创建一个运行linux镜像，如debian的pod,通过pod SSH 你要进入的那个node的私有IP去访问这个node（https://docs.microsoft.com/zh-cn/azure/aks/ssh），具体演示如下：
首先，开始之前你需要生成一个秘钥对，而后将你的公钥添加到要登录的节点中，如下面2个图片中的命令显示简要描述一下这个过程：

a, 将你的AKS集群资源组的信息打包到变量CLUSTER_RESOURCE_GROUP中；

b, 查看这个变量下的node VM信息，记下这个你要登录的node的名称；

c, 更新你的公钥到node中，其中，--ssh-key-value ~/.ssh/id_rsa.pub 这里输入你本地存放公钥的路径信息。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点7.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%881%EF%BC%89%EF%BC%9A创建集群并登录到node节点8.png)


第二步是查看你要登录的那台node的私有IP，可以用命令查看，也可以在portal上的MC_开头的资源组里直接查看：比如我要登录的这台就是10.240.0.6

第三步，
a，先在集群中运行一个debian的容器，这个image创建完成后即启动bash界面，bash中先安装SSH客户端：apt-get update && apt-get install openssh-client -y
b，与此同时打开另一个terminal窗口，kubectl get pods查看在上一步中的pod名称，然后将你的私钥拷贝到pod中去：kubectl cp ~/.ssh/id_rsa aks-ssh-554b746bcf-kbwvf:/id_rsa
c，需要的话修改私钥为只读，然后回到debian容器中执行ssh -i id_rsa azureuser@node 私有IP， by default 集群中每个node的登陆名都是azureuser。然后就可以登录到目标node了：
 
以上就是本篇文章的内容，附上相关参考文章：
 https://docs.microsoft.com/en-us/azure/aks/
