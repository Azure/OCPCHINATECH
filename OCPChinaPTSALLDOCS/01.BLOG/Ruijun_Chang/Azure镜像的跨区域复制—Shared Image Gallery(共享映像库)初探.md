在上一篇文章末尾我们总结了几种VM磁盘的操作，关于“镜像捕获”这一栏，若要跨Region创建VM，可以对通用化的VM磁盘做快照，然后使用SAS URL将快照复制到目标region的存储账号中再创建VM。有个问题，如果要对捕获后的镜像做多区域的复制，快速扩展部署环境，有没有一个更快速便捷的方式来做这个事呢。是有的，使用Azure Global 的Shared Image Galleries（共享映像库）便可实现这个需求，下面我们来demo一下这个功能。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A201.png)

因为当前这个功能还处于limited preview阶段，暂时只能用CLI去创建和使用，因此开始之前需要先更新一下CLI到最新版本，当前最新版本是2.0.60，可以用 az --verison 查看下当前版本，如果是windows用户，可以按照https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest 操作，macOS 按照https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos?view=azure-cli-latest，windows用户如果是WSL（Windows Subsystem for Linux (WSL)）的更新，建议参照https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest 去一步一步手动更新，如果直接按照Linux(https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?view=azure-cli-latest)的方式更新会报错，因为WSL需要先更新相关的依赖项才能继续往下走。

更新完成后，因为是preview阶段，因此开始之前首先注册一下这个功能：

```
az feature register --namespace Microsoft.Compute --name GalleryPreview
az provider register -n Microsoft.Compute
```

执行az provider show -n Microsoft.Compute 结果显示为registed就可以了。首先我们为位于eastus的源image:VM0image创建一个名为vm0imagegallery的共享库，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A202.png)

必选参数有两个：--gallery-name 和 --resource-group，接下来创建一个image definition，这个image definition主要是标明这个镜像的有关信息，包括它的SKU,OS 类型等，方便管理和复用，如下，定义这个image definition为webserverdemo,demo中这个image是要作为web 服务器，因此这样定义它：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A203.png)

截图中的都是必选参数，其他可选参数还可以指定它的CPU核数，内存等，具体可以参考：https://docs.microsoft.com/en-us/cli/azure/sig/image-definition?view=azure-cli-latest#az-sig-image-definition-create。关于image definition,贴下面这张图可能会更清楚：可以定义不同功能的应用，以便在该应用的definition里面管理不同的版本。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A204.png)

接下来重头戏来了，我们需要执行az image gallery create-image-version命令来定义image的版本，要复制的目标region，份数，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A205.png)

--replica-count 指定每个region默认的复制份数，如果需要指定某个region的数量，可以用--target-regions中的等于号来特定化，上图中我们是将VM0image复制到了West Central US, South Central US,East US 2，East，4个region，创建完成后回到portal页面看一下：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A206.png)

然后我们尝试在westcentralus以image gallery中的image为源创建一台VM，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A207.png)

可以看到创建成功了，至此实现了跨region的复制和创建。每个订阅创建image galleries时有限额的，当然我们也可以删除一些过往的库或者从管理上将image definition 命名好都放在一个库里就好。

* 10 shared image galleries, per subscription, per region
* 200 image definitions, per subscription, per region
* 2000 image versions, per subscription, per region

另外本身Shared Image Gallery 这项服务不收费，但是image的存储和源区域复制的出站要收费。除了这篇文章中演示的部分，有兴趣的读者如果需要增加一个新的image版本或者定义更多可选参数，可以参考：https://docs.microsoft.com/en-us/cli/azure/sig/image-version?view=azure-cli-latest#az-sig-image-version-create做更多尝试。 

最后放一张官网的大图来总结下共享映像库（比较一目了然）的功能：帮助用户快速实现跨区域的镜像复制和扩展。当然产品组也在不断完善portal和powershell的支持以及更多源region的支持，包括创建完成之后查看目标区域的镜像状态，情况等命令也会做的更加细化，一起期待GA。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E9%95%9C%E5%83%8F%E7%9A%84%E8%B7%A8%E5%8C%BA%E5%9F%9F%E5%A4%8D%E5%88%B6%E2%80%94Shared%20Image%20Gallery(%E5%85%B1%E4%BA%AB%E6%98%A0%E5%83%8F%E5%BA%93)%E5%88%9D%E6%8E%A208.png)

标签: Azure Image
