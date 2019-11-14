刚刚过去的六月，Azure中国又有一批新的服务落地，其中就有一款非常令人期待的服务***Application Insights***。

***Application Insights*** 是一款智能的APM工具，能够帮助用户打造应用程序端到端的链路监控解决方案，发现应用程序的性能问题，及时修复应用程序中的错误，快速掌握应用程序中不健康的地方，让应用程序对外提供更好的体验；同时，能够分析应用的访问分布，用户的感兴趣点，最受欢迎的区域，可以让运维人员参与到业务，提供业务层面的数据支撑。

***Application Insights*** 目前在中国Azure已经可用，且功能上并未与Global Azure有太多的gap，保持了其智能APM有点。Application Insights不仅支持多语言的应用，如`.NET`,`.NET Core`,`Java`,`Node.js`等，无论你的应用部署在哪里，`本地机房`还是`其他云中`，都可以通过***Application***监控管理，且`Visual Studio`的插件支持，可以让我们的开发人员更加方便的使用Visual Stuido完成监控修复，提高开发运维的效率。
话不多说，今天会带大家通过一个小的实验，了解如何快速的在应用中添加***Application Insights*** ，同时，在预先准备好的环境中，带大家看一下各个功能的长相及用途。
## Part 1  为 Azure 中的 .NET 程序添加 Application Insights
### Step 1 创建 Application Insights 实例
创建 Application Insights 实例特别简单
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%201.webp)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%202.webp)

检查创建后的`Application Insights`实例，可以看到图中显示的`Instrumentation Key`，这代表应用程序发送数据到Azure的Key

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%203.webp)

### Step 2 创建一个简单的 .NET Project
创建一个ASP.NET Web程序，名且`Demo01`

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%204.webp)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%205.webp)

升级`ApplicationInsights`相关的SDK包，确保其为最新的稳定版本，当前为`v2.10.0`

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%206.webp)

配置`ApplicationInsights.config`，添加必要的连接信息，相比于Global版本的配置，Azure Mooncake的`Application Insights`除了配置 Instrumentation Key之外，需要配置三个额外的地方，以确保数据可以发送到云端，详见如下：
#### 配置`Instrumentation Key`

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%207.webp)

#### 配置`elemetryModules - Microsoft.ApplicationInsights.Extensibility.PerfCounterCollector.QuickPulse.QuickPulseTelemetryModule, Microsoft.AI.PerfCounterCollector`下的`QuickPulse_Endpoint_Address`

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%208.webp)

#### 配置`ApplicationIdProvider`下的`ProfileQueryEndpoint`

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%209.jpg)

#### 配置`TelemetrySinks`-` TelemetryChannel`下的`EndpointAddress`

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2010.webp)

本地运行应用程序，并验证是否将数据已经发送至云端

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2011.webp)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2012.webp)

接下来只需要将应用部署到相应的环境中，你就已经为你的环境添加了智能APM服务。
### Part 2 解读一下`Application Insights`的各个功能
为了更直观的让大家了解Application Insights的各个功能，这个部分我使用了预先准备好的环境。
***Application Insights 中实现的APM的功能***
***Application Map***能够以图形化的方式，呈现应用程序及其依赖的调用关系，以及不同调用链上的请求速率，失败速率，提供一个对应用程序的总体视图。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2013.webp)

***Live Metrics Stream***能够实时查看应用的健康状况，进出的流量，失败速率等，并可针对Failure进行快速定位。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2014.webp)

***Availability***能够帮助你了解应用的可用性，并可针对应用不可用进行不同程度的告警。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2015.webp)

***Failures & Performance***能够让你了解应用中的错误或性能瓶颈，并统计了当前影响范围最大地方，可以帮助你进行快速的定位问题。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2016.webp)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2017.webp)

***Application Insights AI&数据分析的功能***
***智能监测&报警***不需要你做什么设置（除了需要填写下告警时需要的邮箱），根据机器学习的模型结合收集到的数据，分析应用访问流量，对突然增多的Failures，或客户端&服务端的性能异常，都会第一时间通知到你，并给出分析的结果和一些可能的建议。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2018.webp)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2019.webp)

Analytics 通过收集到的日志数据，进行聚合分析，结合查询语句，快速查询并返回图形化的结果。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2020.webp)

***Workbooks & Troubleshooting Guide***能够让你将查询的图标嵌入到用于运维查错的Runbook中，容易让新来的人更加方便的上手。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2021.webp)

***Application Insights 业务层面的辅助***
***Users***能够帮助你了解访问应用的用户分布，使用的浏览器以及点击最多的地方，帮助你去更好的优化应用。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2022.webp)

***Events***能够帮助你了解用户最感兴趣的页面或按钮，更好的辅助你做活动或应用的设计。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2023.webp)

***User Flows***能够帮助你了解用户的访问过程中，停到哪里，在哪里流失了客户，帮助你去更好的运营。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Application%20Insights%20完成应用程序的全链路监控%2024.webp)

### 参考资料 ：
- 在 Azure 中创建 ASP.NET Framework Web 应用 ：https://docs.azure.cn/zh-cn/app-service/app-service-web-get-started-dotnet-framework

- [不断上新！Azure 6月重大产品发布速览](https://mp.weixin.qq.com/s?__biz=MzA4MzA1OTc1MA==&mid=2649848748&idx=1&sn=04515985953aa5298606818be611ed59&chksm=87f9eee5b08e67f3a5ef409cff409dbbd3773c4586332a3fa0750de745c80fe87e9312a698d0&mpshare=1&srcid=&scene=21#wechat_redirect)

- [Azure超强大招：5大服务大降价，数据传输入站流量全部免费](https://mp.weixin.qq.com/s?__biz=MzA4MzA1OTc1MA==&mid=2649848778&idx=1&sn=bb4730e09947fb2d849f9a0f6ed34596&chksm=87f9ee83b08e6795ae184bd73c6d2500a96e34a0bbd5f31205946648781687ff34bd8eaceace&mpshare=1&srcid=&scene=21#wechat_redirect)

