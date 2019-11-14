今天来介绍一款Global Azure上的服务，名为 Application Insights 的服务，通过它，可以让你的Apps，快速集成性能监控的能力（APM），真正做到你的Apps，一切都在你的掌握。



Application Insights 是一款Azure提供的智能APM服务，无论你的Apps是运行在本地，还是运行在公有云上，都可以通过它来完成应用的性能监控，实时了解到目前我的应用的健康状况，是否出现问题，各个功能是否存在Bug或Performance的问题，同时，内嵌的AI、数据分析的能力，能够自动进行探测分析，快速告知你当前应用的潜在风险，并借助于数据分析的能力，快速定位出现的问题，保障应用高效运行。



# Application Insights 中实现的APM的功能



**Application Map** 能够以图形化的方式，呈现应用程序及其依赖的调用关系，以及不同调用链上的请求速率，失败速率，提供一个对应用程序的总体视图。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2001.webp)

**Live Metrics Stream** 能够实时查看应用的健康状况，进出的流量，失败速率等，并可针对Failure进行快速定位。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2002.webp)

**Availability** 能够帮助你了解应用的可用性，并可针对应用不可用进行不同程度的告警。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2003.webp)

**Failures & Performance** 能够让你了解应用中的错误或性能瓶颈，并统计了当前影响范围最大地方，可以帮助你进行快速的定位问题。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2004.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2005.webp)

# Application Insights AI&数据分析的功能



**智能监测&报警** 不需要你做什么设置（除了需要填写下告警时需要的邮箱），根据机器学习的模型结合收集到的数据，分析应用访问流量，对突然增多的Failures，或客户端&服务端的性能异常，都会第一时间通知到你，并给出分析的结果和一些可能的建议。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2006.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2007.webp)

**Analytics** 通过收集到的日志数据，进行聚合分析，结合查询语句，快速查询并返回图形化的结果。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2008.webp)

**Workbooks & Troubleshooting Guide** 能够让你将查询的图标嵌入到用于运维查错的Runbook中，容易让新来的人更加方便的上手。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2009.webp)

# Application Insights 业务层面的辅助



**Users** 能够帮助你了解访问应用的用户分布，使用的浏览器以及点击最多的地方，帮助你去更好的优化应用。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2010.webp)

**Events** 能够帮助你了解用户最感兴趣的页面或按钮，更好的辅助你做活动或应用的设计。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2011.webp)

**User Flows** 能够帮助你了解用户的访问过程中，停到哪里，在哪里流失了客户，帮助你去更好的运营。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2012.webp)

将Application Insights添加到你的应用中并不难，只需要将对应平台的SDK或JAR包添加到应用中，并添加相应的配置文件即可。目前Application Insights支持 .Net / .Net Core / Java / Node.js / Web应用 / 移动用于 / 网页 / Docker容器中的应用 等语言，且照原样用，无需做代码层面的修改。



当然，你也可以在应用程序中，添加代码，收集定制化的数据或异常，来帮助你更加完善的监控你的应用程序，例如：

```
var sample = new MetricTelemetry();
sample.Name = "metric name";
sample.Value = 42.3;
telemetryClient.TrackMetric(sample);
```

# Demo 为一个本地的Demo应用程序引入Application Insights



## 第一步 创建 Application Insights 

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2013.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2014.webp)

创建好后，你会拿到一个叫做 Instrumentation Key 的字符串，形如 69a30cbb-8551-4f50-a805-d110e10a82b6 ，这个是需要后续配置到配置文件中，用来告诉SDK，该将数据发到哪里。



## 第二步 打开 Visual Studio 2017，创建一个ASP.NET的Project

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2015.webp)

## 第三步 配置Application Insights

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2016.webp)

右键Project，会有Config Application Insights的选项，输入你的Global Azure的账号，可以选择刚才创建的Application Insights进行设定，会自动帮你配置好所有SDK及配置文件。主要的配置文件如下，包含了 Instrumentation Key以及相应的配置信息，用来规定如何发送Metrics，速率以及该发送何种Metrics。

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2017.webp)

当然，手动一步步下载并添加SDK，并手工添加配置文件也是可以的，详情参见参考资料。



## 第四步 本地运行应用，并监测数据是否发送到Application Insights

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2018.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%80%9F%E5%8A%A9Application%20Insights%EF%BC%8C%E8%AE%A9Apps%E5%BF%AB%E9%80%9F%E6%8B%A5%E6%9C%89APM%2019.webp)

# 参考文件：

什么是Application Insights : https://docs.microsoft.com/zh-cn/azure/application-insights/app-insights-overview?toc=/azure/azure-monitor/toc.json

如何将Application Insihgts 添加到Java应用中：https://docs.microsoft.com/zh-cn/azure/application-insights/app-insights-java-get-started

Application Insights 常见的问题 ：https://docs.microsoft.com/zh-cn/azure/application-insights/app-insights-troubleshoot-faq?toc=/azure/azure-monitor/toc.json
