目前Machine Learning的知识还在学习阶段，让我独自写一个算法模型出来还需时日，但基础工作要做好，先要搞明白如果算法模型写出来后如何发布给大家使用。



这篇文章是参考Azure官方Docs中的一篇名为 人工智能 (AI) 应用程序的 DevOps：使用 Docker 和 Kubernetes 在 Azure 上创建持续集成管道，但做了些小的改动，如果大家感兴趣的话，可以跟着这个实验一起来做一遍：当我们拿到开发好的ML模型，如何发布成对外的Web Service，同时，当模型更新后，如何自动的触发 Build & Release 流程。



架构图如下：

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2001.webp)

# 环境准备

所有环境均放在同一个资源组下。

## 创建 Azure Container Registry

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2002.webp)

## 创建 Azure Container Service （AKS）

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2003.webp)

## 创建Storage Account，并上传机器学习模型到Blob

有两个文件，一个是ML的模型ResNet_152.model，一个是示例代码需要用到的数据synset.txt。原文件链接为：https://www.cntk.ai/resnet/ResNet_152.model；http://data.dmlc.ml/mxnet/models/imagenet/synset.txt。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2004.webp)

# CI/CD Pipeline的构建



本次实验主要基于VSTS，结合Github中保存的代码，进行CI/CD的构建，包含了Build & Release 的流程。



## CI/CD Build 部分概览

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2005.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2006.webp)

## 下载ML模型及数据

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2007.webp)

Arguments部分的参数为五个，中间用空格隔开，分别为：存储账户名称，存储账户的访问密钥，存储账户中的Container名称，ML模型对应的Blob名称，数据集对应的Blob名称。

## 构建ML模型的Docker Image

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2008.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2009.webp)

## 将Docker Image推送到ACR中

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2010.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2011.webp)

## 创建 Release 定义

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2012.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2013.webp)

## CI / CD Release 部分

此部分有两个个任务，来完成应用的发布工作，第一个任务属于Hard Code，是为了多次发布可以不Block现有的环境，而做的环境清理，在实际的应用中不需要做这样的事情，只有最后一个任务是重要的，就是将Build好的Image发布成K8S Service。

## Release概览

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2014.webp)

## 清理现有环境

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2015.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2016.webp)

## 将新的Image部署在AKS环境中

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2017.webp)

deploy.yml文件中的内容很简单，就是创建一个K8S的Deployment，并创建一个K8S的Service。

## 测试整个 Build & Release 流程是否成功

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2018.webp)

## 通过CloudShell来查询创建结果

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2019.webp)

多加一步，如果针对模型有任何的改动，想要实时的Trigger。基于此，额外增添了Logic App，添加了两个步骤，当Blob有任何改动，都会产生一个Event，这个Event会通过VSTS的RESTAPI触发一次Build&Release的流程。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2020.webp)

最后通过一个Python小程序测试一下模型的功能，会通过检测如下图形，反馈一个结果：

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2021.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%94%92%E4%B8%80%E7%AF%87%E5%AE%9E%E9%AA%8C%20%EF%BC%9A%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2%E4%BD%A0%E7%9A%84%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B%E5%88%B0AKS%2022.webp)

留给大家的想象空间：如何穿插镜像的Unit测试，集成测试等，如何扫描镜像的安全性等，如何通过更改deploy.yml实现Image更新过程中不会造成现有应用中断。



# 参考资料：

人工智能 (AI) 应用程序的 DevOps：使用 Docker 和 Kubernetes 在 Azure 上创建持续集成管道使 ： https://docs.microsoft.com/zh-cn/azure/machine-learning/team-data-science-process/ci-cd-flask#github-repository-with-document-and-code
文章中用到的源代码 ：https://github.com/jianzj/DevOps-For-AI-Apps

DevOps for Artificial Intelligence (AI) applications : https://github.com/jianzj/DevOps-For-AI-Apps/blob/master/Tutorial.md
