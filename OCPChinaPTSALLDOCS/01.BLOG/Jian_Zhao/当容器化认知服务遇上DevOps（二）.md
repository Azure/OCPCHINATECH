接第一篇，当容器化认知服务遇上DevOps（一），除了微软官方给出的镜像外，形如Custom Vision这类的认知服务，是允许用户根据自己的实际场景，进行模型的再训练，从而定制属于自己的认知服务。

今天的实验，就是基于训练后Custom Vision生成的Dockerfile，自动化生成对应的容器镜像，并部署到AKS集群中。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8901.webp)

# 前期准备
训练好的Custom Vision ：针对Custom Vision，微软专门提供了对应的页面，方便用户图形化的对模型进行训练测试等，具体连接可以从参考资料中找到；

Github Repo : 创建一个Github Repo；

Azure DevOps Org & Azure DevOps Project : 准备好Azure DevOps的资源，为后面创建Build&Release Pipeline做准备；

ACR : 用来存储创建好的容器镜像；

AKS 集群 ：准备可用的AKS集群；

# Step 1 导出训练后的 Custom Vision Dockerfile，并添加到 Github 中
根据页面的提示，将训练好的模型下载为Dockerfile

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8902.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8903.webp)

下载下来的文件包含了Dockerfile，及一些模型&服务需要的应用文件，将所有都上传到Github

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8904.webp)

# Step 2 通过Azure Pipelines 将Dockerfile生成容器镜像，并上传到Azure Container Registry
创建Build Pipeline，将Dockerfile上传到ACR

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8905.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8906.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8907.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8908.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8909.webp)

# Step 3 将上传好的Custom Vision Image部署到AKS集群
创建Release Pipeline，将部署好的Custom Vision Image部署到AKS中，并通过Service发布成对外可访问的服务。

可以看到，目前AKS的集群的详细信息，顺便提一下，中国区的AKS目前已经可以使用。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8910.webp)

创建下载镜像需要用的的ACR Secret，名为acrsecret

```
kubectl create secret docker-registry acrsecret --docker-server="zjregistry01.azurecr.io" --docker-username=zjregistry01 --docker-password=NelhejXggstEwx0pRIveCIp/5IPJDRsY --docker-email=demo@outlook.com
```
创建Release Pipeline，并将Image发布成为AKS的Service，创建Kubernetes中资源的所有YML文件，均可在参考文件中的Github Repo中找到。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8911.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8912.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8913.webp)

# Step 4 验证创建的Custom Vision Service
我们看到，相关的资源已经在集群中部署出来

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8914.webp)

接下来我们调用相应的API进行测试

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%BA%8C%EF%BC%8915.webp)

# 参考资料
Custom Vision 使用界面 ：https://www.customvision.ai/

Custom Vision DevOps Demo Repo : https://github.com/ericzhao0821/customvisiondevops01
