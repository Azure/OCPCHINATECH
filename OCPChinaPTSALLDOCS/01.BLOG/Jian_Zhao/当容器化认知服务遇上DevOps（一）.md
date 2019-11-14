本文是一篇动手实验，通过Azure DevOps Pipelines，将可以容器化部署的认知服务 Text Analysis 部署到 IoT Edge 中。标题特别的唬人主要是昨天晚上喝了酒，虽然是米酒，但是劲还是挺大的。

前端时间，Azure发布了容器化的认知服务，有了容器化的认知服务，可以方便我们将认知服务就近的部署，无论是云端环境中的Web Apps& AKS还是本地容器化环境或IoT Edge环境，从而更加便捷的实现实际环境中的需求。目前Azure支持包括计算机视觉、人脸、文本分析和语言理解 (LUIS)在内的四种认知服务放入Container，且正在不断推出新的认知服务镜像。

本次实验分为两篇，第一篇主要介绍如何将Text Analytics通过Azure DevOps Pipelines自动化部署到IoT Edge中；第二篇主要介绍如何将Custom Vision训练好的模型，借用Dockerfile，通过Azure DevOps Pipelines自动部署到IoT Edge中。

# 前期准备：
以下资源需要在实验开始前进行创建，创建资源步骤请参阅参考资料中的链接：

Azure IoT Edge及Ubuntu 16.04 VM : 通过VM模拟本地设备，将IoT Edge运行时环境安装在Ubuntu VM中，并与IoT Hub进行连接，方便后续管理；

Azure DevOps Org & Azure DevOps Project : 用于创建 Azure DevOps Pipelines;

Azure Cognitive Services Text Analytics : 部署到本地的认知服务，仍然需要定期与云端的服务进行通信，且共享云端服务的Key，通信的目的主要是针对Billing部分；

本次实验架构图如下：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8901.webp)

# Step 1 制作包含 Text Analytics 的 IoT Edge 部署模板
DevOps Project 概览

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8902.webp)

新创建一个Pipeline，名为 devops01-CI

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8903.webp)

制作部署模板

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8904.webp)

关于部署模板的内容，可参见：https://github.com/ericzhao0821/zjcognitiveops01/blob/master/deployment.template.json

针对于环境中该如何使用特定版本的Text Analytics Image，可以通过更改 deployment.template.json 进行版本控制，使得只有特定需要版本的容器化 Text Analytics 才会部署到 IoT Edge中。

将Build好的deployment file传递给Release的pipeline

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8905.webp)

# Step 2. 将包含 Text Analytics 的 IoT Edge部署模板，部署到IoT Edge环境中
创建一条 Release Pipeline，用于持续化部署

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8906.webp)

通过Artifacts，与Build进行结合

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8907.webp)

添加部署到IoT Edge环境的Task

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8908.webp)

简单的测试了下Pipeline，目前运行良好

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8909.webp)

# Step 3. 验证发布到 IoT Edge的文本分析服务是否正常运转
由于创建之初，我为IoT Edge准备了相应的VM，可以通过 SSH 命令登陆到虚拟机，通过私有地址进行服务调用，如下所示：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8910.webp)

可以看到，Text Analytics中的Language识别可以正常本地使用。

# Tips ：
我们可以通过Github来完成 Text Analytics Image及其他相关文件的版本管理，每当更改完相应文件后，会自动触发之前创建好的CI/CD的Pipeline，完成Module的构建，并部署到IoT Edge环境中。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8911.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BD%93%E5%AE%B9%E5%99%A8%E5%8C%96%E8%AE%A4%E7%9F%A5%E6%9C%8D%E5%8A%A1%E9%81%87%E4%B8%8ADevOps%EF%BC%88%E4%B8%80%EF%BC%8912.webp)

有兴趣的可以去尝试一下 !

# 参考资料：
Azure 认知服务中的容器支持 : https://docs.microsoft.com/zh-cn/azure/cognitive-services/cognitive-services-container-support

Running Cognitive Services on Azure IoT Edge : https://azure.microsoft.com/zh-cn/blog/running-cognitive-services-on-iot-edge/?from=singlemessage&isappinstalled=0
