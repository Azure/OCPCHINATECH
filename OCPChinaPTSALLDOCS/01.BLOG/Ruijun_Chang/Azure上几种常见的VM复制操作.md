对于很多新上手使用Azure 虚拟机的客户，常常有做快照，做镜像，复制OS盘等的需求，有时会出现没有事先阅读到azure.cn上对应部分的文档，创建完虚拟机下意识在portal上点了错误的按钮出现“意料之外的停机”的情况，因此这里针对常见的VM复制的需求和操作做一个简单的梳理，以截图的方式帮助我们的Azure用户更好的理解VM复制这块的操作，以根据实际需求选择正确的处理方式。

# 快照（snapshot）

快照是VHD在某个时间点的完整只读副本，要对VM的OS盘或者数据盘做快照，或者通过快照创建虚机，可以通过命令行来做，如下演示了将一个名为VM0（创建区域在北2）的虚拟机做快照，然后利用该快照重新创建一台虚拟机VM2的过程（CLI命令）：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C01.png)

简单解释一下这个过程：首先是通过 az vm show获取磁盘ID并且存到了osDiskId这个变量中，然后将这个ID作为源创建了一个名为VM0snapshot的快照，再用这个快照创建了一个名为VM2OSDisk的托管磁盘，最后将这个托管磁盘作为OS盘attach创建了一台名为VM2的虚拟机。图中报错的两个地方是我做的两个尝试：第一处是在创建VM0的快照时企图将创建的region直接指定在东2，提示东2找不到源ID；第二处是在创建VM2的时候企图将OS托管磁盘创建的VM直接指定在东2，提示失败。所以这里我们可以看到，创建快照的时候是不能直接跨region的。

那么回到portal.azure.cn，如果想在网页上创建快照，需要找到要创建快照的磁盘，点进去，下面以VM2的OS为例，展示下页面操作的位置（红框处）：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C02.png)

点完【创建快照】后，可以直接在页面上输入快照名称，注意【位置】部分的选项已经置灰，默认是和源盘放在同一个region的，那么问题来了，如果我想要利用这个快照在不同region创建VM，怎么操作呢，别着急，我们可以对创建好的快照执行导出（export）操作，用导出的vhd来创建，用CLI或者页面上都可以导出，页面上如下：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C03.png)

 这里会生成一个有过期时间的url让用户下载，然后我们演示一下如何使用这个url的内容在不同region创建一个新虚机：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C04.png)

简单解释一下：首先是在要创建VM的那个region创建好一个存储账号，在该存储账户里面创建好一个container，然后执行 az storage blob copy命令，将上一步在页面上执行export后生成的url链接作为源，复制到这个存储账号下面的blob上，命名为vm2snapsot.vhd，然后将这个vm2snapsot.vhd作为源创建托管磁盘再创建一个VM，这样就实现了跨region的创建。

# 捕获镜像（image capture）

通常我们创建好VM后，转到VM下面会看到概述里面有个【捕获】的按钮，英文界面显示的是capture：

 ![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C05.png)

 这里特别提醒，这个capture，不是捕获虚机的快照，它是捕获虚机映像用的，通常我们会有以这台配置好的虚拟机为模板，创建多个同样环境的虚拟机的需求，这里的capture指的就是捕获这台虚拟机的映像，去掉机器的个人账户等信息，通用化之后用于再部署，所以点了这个按钮，一定会先停机，因为要先解除这台虚拟机的资源分配然后创建镜像。点完这个按钮之后页面上也会有明确的提示，‘创建映像前，请先使用命令做通用化并且会使当前虚机不可用’，下面演示下CLI如何捕获镜像再创建VM：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C06.png)

首先登陆到要捕获的这台VM上执行sudo waagent -deprovision+user 命令将用户等特定的信息删除，然后将这台VM解除分配，通用化之后做映像：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C07.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C08.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C09.png)

然后用az vm create以刚刚的image为源创建一台新的VM，这里做了个小小的验证，原来的那台VM0里是启动了nginx的，通用化之后重新建的这台VM里我们重新开了下80端口去验证服务是正常启动没问题的：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C10.png) 

所以简单总结就是，镜像捕获（capture）会停机，且如果捕获之前没有登录到虚机执行“取消预配”的操作，新创建的虚拟机会报错。

# 磁盘复制或导出

如果想对正在运行的VM磁盘做复制，可以用az disk create的方式来创建，源选对就可以：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C11.png)

如果想对正在运行的VM磁盘做导出，必须先停机，将这个盘解除attach才可以执行，页面上操作的话也会有明确的提示：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C12.png)

接下来的步骤跟快照中导出后再创建虚机一样，同样的方式也可以支持跨region创建。

 

最后简单总结下这几种方式：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%87%A0%E7%A7%8D%E5%B8%B8%E8%A7%81%E7%9A%84VM%E5%A4%8D%E5%88%B6%E6%93%8D%E4%BD%9C13.png)

希望这篇文章能帮大家更清楚的认识这几种操作的区别，方便在生产中做决策。

另附上几篇参考链接：

如何创建虚拟机或 VHD 的映像：https://docs.azure.cn/zh-cn/virtual-machines/linux/capture-image

从快照创建虚拟机：https://docs.azure.cn/zh-cn/virtual-machines/scripts/virtual-machines-linux-cli-sample-create-vm-from-snapshot?toc=%2fcli%2fmodule%2ftoc.json

如何复制或导出托管磁盘：https://docs.azure.cn/zh-cn/articles/azure-operations-guide/virtual-machines/aog-virtual-machines-howto-export-managed-disks

浅谈Azure的虚机复制：http://aubreyhan.net/undefined/21136/ 

 

标签: Azure VM
