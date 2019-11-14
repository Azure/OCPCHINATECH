小伙伴们好久不见，今天我们来聊聊中国 AZURE 的日志分析告警。为什么是中国 AZURE，目前中国 AZURE 的 Monitor 服务和运维相关周围服务和 Global 是有所不同的，所以有些功能和设计不能复制和套用全球版 AZURE 的架构。我们先看一下中国 AZURE 运维管理方面一些平台原生功能的缺失，1. Azure Monitor 支持新的 Metric 指标分析服务，但不支持基于新的 Metric 指标分析的告警设置，简而言之能看不能告警；2. 中国 AZURE 目前不支持 Azure Log Analytics 服务，平台原生不支持日志分析服务，无法通过原生服务进行日志分析和告警。所以对于平台原生支持的一些 Metric 或者 Log 无法通过 Azure Monitor 或 Azure Log Analytics 分析并发送告警。今天的 Demo 中以一个例子，通过 EventHub + Stream Analytics + Function 来实现流式分析实时告警。

# 架构图：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A601.png)

日志源：EventHub 原生已经支持对于 Azure 平台服务的日志消息采集能力，VM 的日志可以通过 Azure VM Diagnotics Extension 进行聚集并传入 EventHub, 对于平台的原生服务可以直接与 EventHub 集成。对于非 Azure 原生服务，比如客户自己的一些日志系统等可以通过 Logstash，Fluentd 的方式将日志注入到 EventHub, Azure 已经有相关的插件来支持和 Logstash 这种日志服务进行集成。

日志聚集：EventHub 来做日志的聚集，可以将多个日志源聚集到同一个 EventHub 下来实现日志消费下游服务的统一分发。

日志实时分析：Stream Analytics 来对 EventHub 聚集的日志进行消费，完成日志的流式实时分析，在此 Demo 中，Sream Analytics 进行应用网关 （Application Gateway）的后端服务节点的健康状态情况，当可用节点小于一个时，触发告警事件。

日志告警：通过 Function 服务，以事件驱动的方式获得 Stream Analytics 的告警，执行 Function 代码推送告警。此 Demo，以邮件告警为例，如果客户有短消息推送等其它推送需求，可以类同方式调取集成。

# 配置方法：

1. 配置日志源

此次 Demo 中以应用网关的 Metric 日志为例，此处忽略应用网关的相关创建动作和配置动作，下面是开启日志推送到 EventHub 的配置方法，此步执行前需要创建好 EventHub

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A602.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A603.png)

2. 配置 EventHub

EventHub 配置方法比较简单，创建 EventHub，然后为了方便区分后端消费者，在创建好的 EventHub 下创建消费组

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A604.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A605.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A606.png)

3. 配置 Stream Analytics 服务

此处跳过 Steam Analytics 的创建过程，直接在创建好的 Stream Analytics 服务上进行配置，分别配置 Input 和 Output，Stream Analytics 作为 EventHub 消息的消费者，首先我们需要在 Stream Analytics 中将 EventHub 配置为 Input，反之 Function 服务是 Stream Analytics 的数据消费者，所以把 Function 服务配置为  Ouput。

此 Demo 中有架构有一些微调，EventHub 和 Stream Analytics 分别对消息事件做了两次处理，流程如下：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A607.png) 

原因是因为 Application Gateway 推送出来的 Metric 日志是以5分钟为间隔一条消息，每个消息中包含5分钟内每分钟的消息，是以 Json 嵌套数组的方式来做的，我们通过第一层的 Stream Analytics 来完成将嵌套的 Metric 日志序列化，将每分钟的 Metric 日志以独立消息的方式注入到 EventHub，然后重新在第二层的 Stream Analytics 中来进行流式分析，以5分钟为间隔来分析5分钟内性能指标的平均值，当平均触碰阈值后生成告警事件，将告警事件通知 Function 服务，通知事件内包含监控指标类型名称和现有指标5分钟平均值，Function 服务以事件驱动执行通知分发程序将告警以相应方式推送到相关责任人。

从 Application Gateway 的生成的 RAW Date 日志格式参考如下：

```
{"records":[{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:27:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:28:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:29:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:25:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:26:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:27:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:28:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:29:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:25:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:26:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:27:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:28:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:29:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:27:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:28:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:29:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:27:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:28:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:29:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:25:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:26:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:27:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:28:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:29:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"}],"EventProcessedUtcTime":"2018-09-10T07:38:52.6261568Z","PartitionId":0,"EventEnqueuedUtcTime":"2018-09-10T07:35:52.4790000Z"}
{"records":[{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:30:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:31:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:32:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:33:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:34:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:30:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:31:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:32:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:33:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:34:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:30:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:31:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:32:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:33:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:34:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:30:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:31:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:32:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:33:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:34:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:30:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:31:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:32:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:33:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:34:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:30:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:31:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:32:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:33:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:34:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"}],"EventProcessedUtcTime":"2018-09-10T07:42:19.8630447Z","PartitionId":0,"EventEnqueuedUtcTime":"2018-09-10T07:42:18.9160000Z"}
{"records":[{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:35:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:36:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:38:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":869,"minimum":869,"maximum":869,"average":869,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:39:00.0000000Z","metricName":"Throughput","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:35:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:36:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:38:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:39:00.0000000Z","metricName":"UnhealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:35:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:36:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:38:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:39:00.0000000Z","metricName":"HealthyHostCount","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:35:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:36:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:38:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":12,"minimum":12,"maximum":12,"average":12,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:39:00.0000000Z","metricName":"TotalRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:35:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:36:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:38:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:39:00.0000000Z","metricName":"FailedRequests","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:38:00.0000000Z","metricName":"ResponseStatus","timeGrain":"PT1M"},{"count":1,"total":12,"minimum":12,"maximum":12,"average":12,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:39:00.0000000Z","metricName":"ResponseStatus","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:35:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":0,"minimum":0,"maximum":0,"average":0,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:36:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:38:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"},{"count":1,"total":1,"minimum":1,"maximum":1,"average":1,"resourceId":"/SUBSCRIPTIONS/4507938F-A0AC-4571-978E-7CC741A60AF8/RESOURCEGROUPS/ALERTDEMO/PROVIDERS/MICROSOFT.NETWORK/APPLICATIONGATEWAYS/ALERTDEMO","time":"2018-09-10T07:39:00.0000000Z","metricName":"CurrentConnections","timeGrain":"PT1M"}],"EventProcessedUtcTime":"2018-09-10T07:45:55.9598069Z","PartitionId":0,"EventEnqueuedUtcTime":"2018-09-10T07:45:55.8810000Z"}
```

第一层 StreamAnalytics 配置：

Input：第一层 EventHub (alertdemo)，Ouput：第二层 EventHub (EventhubStream)

查询语句

```
WITH 
Metric AS
(
    SELECT   
        arrayElement.ArrayIndex,  
        arrayElement.ArrayValue  
    FROM alertdemo as event  
    CROSS APPLY GetArrayElements(event.records) AS arrayElement
),
TransformedInput AS (
    SELECT
        Metric.arrayvalue.*
    FROM Metric
)
SELECT
    *
INTO EventhubStream
FROM TransformedInput
```

第二层 StreamAnalytics 配置：

Input：第二层 EventHub (EventhubStream)，Ouput：Function (FuncOutput)

```
SELECT
    metricName,
    AVG(average) as avg
INTO FuncOutput
FROM EventhubStream TIMESTAMP BY time
GROUP BY
    metricName,
    TumblingWindow(minute, 5)
HAVING
    (
        avg(average) <= 1 and metricName = 'HealthyHostCount'
    )
```

4. 配置 Function 服务

这里在配置过程中有个地方需要注意：需要在 Function 服务的 SSL 部分将 TLS 版本设置为 1.0， 这个是 Function 和 Stream Analytics 服务集成的要求。

本例中以 Python Runtime 为例，创建一个 Http Trigger 触发的 Function 函数，代码如下：

```
import os
import json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "******@***.com"
toaddr = "******@***.com"

postreqdata = json.loads(open(os.environ['req']).read())
if postreqdata:
    
    #Create Alert Message
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alert Fire"
    body = postreqdata[0]['metricname'] + " fire the alert"
    msg.attach(MIMEText(body,'plain'))

    #Send Alert Message
    s = smtplib.SMTP('smtp.***.com')
    s.ehlo()
    s.login("*******@***.com", '******')
    s.sendmail(fromaddr, toaddr, msg.as_string())

#Prepare Success Code
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": "<h1>Azure Works :)</h1>",
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
```

检查邮件告警

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/AZURE%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%87%AA%E5%8A%A8%E5%91%8A%E8%AD%A608.png)

本文中的 Demo 只是一个简单的示例，大家可以根据自己实际的业务场景需求对流分析部分的告警策略自行定义，流式分析服务内置了很多分析能力可以满足我们不同的分析需求。

# 参考阅读：

1. Stream Analytics 常用语法：https://msdn.microsoft.com/zh-cn/azure/stream-analytics/reference/stream-analytics-query-language-reference

2. Stream Analytics 分析场景示例：https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-stream-analytics-query-patterns

3. Azure 平台服务日志参考：https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics
