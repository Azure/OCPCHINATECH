今儿咱们撩一撩 Brigade，AZURE 的童鞋出去讲容器总会把 Helm，Draft，Brigade 挂在嘴边，这 Brigade 到底能做什么今天我们就来说一说。K8s 中有一种调度模式叫 Job，Job 不名思意就是任务，以达到某一目标定义的一系列执行，Job 其实非常适合在 K8s 中执行，容器呼之即来挥之即去的特点，可以非常方便的做任务的编排，任务执行中申请资源，任务结束返回结果释放资源。简单的一些的任务可能由一个事务构成，复杂的任务可能由一系列事务构成。当需要执行一系列事务时可以把所有事务放在一个容器中执行，也可以通过把事务放入流水线（workflow）来执行。流水线作业显然在灵活性和效率上更胜一筹，流水线通过将复杂任务拆分为独立的事务单元，然后每个事务单元分别由专门的处理单元来进行出来，然后将结果传递给下一个处理单元，通过这种方法，一个复杂的任务可以拆解为多个标准的事务，后续当有新的复杂事务时，这些标准事务单元可以进行重组来实现新的事务逻辑。在 K8s 中 Job 更像简单事务的处理逻辑，在单个容器中将事务进行处理，缺乏通用性和灵活性，那么有没有这样一个工具或平台可以实现复杂事物内任务的的编排，并在任务间实现消息的传递以及事件驱动逻辑，Brigade 就是我们要找的答案。下面我们就以一个 CI （Continue Intergrated）的例子来为大家介绍一下 Brigade。

在 CI 过程中我们想实现一个从代码更新 -> 镜像Build -> 通知开发人员新版本发布 ，我们今天把整个过程通过 Brigade + AKS + ACR 的方式来实现，下面我们先来看一下 CI Workflow 的流程图：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BE%AE%E8%BD%AF%E5%AE%B9%E5%99%A8%E5%91%A8%E8%BE%B9%E7%8E%A9%E5%85%B7%E4%B9%8B%20Brigade%20%E7%AF%8701.png)

在开始之前我们先来完成一些基本组件的安装，假设我们在环境中已经拥有 AKS，ACR，以及现成的 Slack 账户，下面我们先来进行 Brigade Gateway的安装，Brigade Gateway 是 Brigade 的事件监听网关，上述我们在预定义的流水线的事件驱动监听器都是由 Brigade Gateway 来实现，当 Brigade Gateway 听到事件请求后会触发相关联的任务（比如上述的容器镜像 Build，Slack Notification）。安装很简单我们可以直接通过 helm 来进行快速安装：

```
helm repo add brigade https://azure.github.io/brigade
helm install brigade/brigade --set cr.enabled=true,cr.service.type=LoadBalancer
```

本文不对 helm 做深入介绍，感兴趣的童鞋可以等我下一篇文章。这里上述两条命令是快速安装了 Brigade Gateway，其中指定的参数 cr.enable=true, cr.service.type=LoadBalancer 是用来在 Brigade Gateway 上开启 ACR（Azure Container Registry）事件监听器，并且由于 ACR 是个公网服务，所以 Brigade Gatway 需要暴露公网访问节点来供 ACR 的 Webhook 访问。好奇的童鞋可能问，为什么没有关于 Github 的参数，默认 Brigade Gateway 就支持监听 Github Webhook 的事件消息。除此之外，Brigade 项目还支持一些其它网关类型（如 EventGrid，Kubernetes Event 等， 可以访问：https://github.com/Azure/brigade 了解更多所支持网关的内容）。安装成功后通过 kubectl get pods 可以看到在 kubernetes cluster 内多了两个 Pod。

```
kubectl get pods
NAME                                         READY   STATUS      RESTARTS   AGE
brigade-brigade-api-6bf4cbdccd-5p7br         1/1     Running     0          6d
brigade-brigade-cr-gw-77d965d846-pkbmk       1/1     Running     0          6d
brigade-brigade-ctrl-8544c45b68-2tb5k        1/1     Running     0          6d
brigade-brigade-github-gw-5ff9c674cf-xtt4f   1/1     Running     0          6d
```

其中 brigade-brigade-github-gw 和 brigade-brigade-cr-gw 就是 Brigade 用来监听 Github 和 ACR 的事件网关。万事俱备，我们可以开始进入主题，通过 Brigade 如何来编排整个上述 CI 的水线。

Brigade 整个任务编排的逻辑通过  brigade.js 文件来进行描述，Brigade 对任务编排逻辑进行了代码的抽象，用户客户方便的通过二次封装的类库来编写流水线逻辑，以本文的示例为例，我们来进行一些解读，帮助大家理解。大家在进行自己的项目时，可以参考 https://azure.github.io/brigade/topics/scripting.html 和 https://azure.github.io/brigade/topics/javascript.html 来编写自己的流水线。

```
 1 const { events, Job } = require("brigadier");
 2 
 3 events.on("push", function(e, project) {
 4   var driver = project.secrets.DOCKER_DRIVER || "overlay"
 5 
 6 // Build and push a Docker image.
 7   const docker = new Job("dind", "docker:stable-dind")
 8   docker.privileged = true;
 9   docker.env = {
10     DOCKER_DRIVER: driver
11   }
12   docker.tasks = [
13     "dockerd-entrypoint.sh &",
14     "sleep 20",
15     "cd /src",
16     "docker build -t $DOCKER_REGISTRY/flask ."
17   ];
18 
19 // If a Docker user is specified, we push.
20   if (project.secrets.DOCKER_USER) {
21     docker.env.DOCKER_USER = project.secrets.DOCKER_USER
22     docker.env.DOCKER_PASS = project.secrets.DOCKER_PASS
23     docker.env.DOCKER_REGISTRY = project.secrets.DOCKER_REGISTRY
24     docker.tasks.push("docker login -u $DOCKER_USER -p $DOCKER_PASS $DOCKER_REGISTRY")
25     docker.tasks.push("docker push $DOCKER_REGISTRY/flask")
26   } else {
27     console.log("skipping push. DOCKER_USER is not set.");
28   }
29  
30   docker.run()
31 })
32 
33 events.on("image_push", (e, project) => {
34   var docker = JSON.parse(e.payload)
35   console.log(docker)
36   var message = "New Build " + docker.target.repository + ":"+ docker.target.tag + " available!"
37   var slack = new Job("slack-notify", "technosophos/slack-notify:latest", ["/slack-notify"])
38   slack.storage.enabled = false
39   slack.env = {
40       SLACK_WEBHOOK: project.secrets.SLACK_WEBHOOK, 
41       SLACK_USERNAME: "BrigadeBot",
42       SLACK_TITLE: "Brigade Build Demo",
43       SLACK_MESSAGE: message,
44       SLACK_COLOR: "#0000ff"
45   }
46   slack.run()
47 })
```

代码中基本组成框架为 event.on 和 job，event.on 来定义触发事件，job 来定义事件的响应。job 中通过调用容器来实现任务的执行。以上述 events.on("push", function(e, project) 为例，定义了当收到 Github push 事件后，将事件消息 e 和 项目 project 信息传参至 context 内，然后创建 job 对该事件进行处理，job 以 new Job("dind", "docker:stable-dind") 进行创建，通过 docker：stable-dind 镜像创建一个任务处理环境来执行镜像 build 和 镜像 push 的工作。第二部分 events.on("image_push", (e, project) 定义了当 ACR 发出 push 事件通过后进行 Slack 消息推送的任务。这部分也出现了 e 和 project，e 很容易理解，就是上游事件通告方传入的事件消息的内容，那 project 是什么呢?

Brigade 中定义 project 为一个 Code Version Control System。即你有很多的代码项目，你可以通过定义多个 project 来描述不同的项目，从而实现在不同项目下定义不同参数、不同 context 的目标。project 在 Brigade 中通过 yaml 文件的方式进行描述，以上述示例为例，我们来看一下如何通过它定义参数和 context。

```
 1 cloneURL: "https://github.com/nonokangwei/brigadedemo.git"
 2 namespace: "default"
 3 project: "nonokangwei/brigadedemo"
 4 repository: "github.com/nonokangwei/brigadedemo"
 5 sharedSecret: "09879879879879879879879871"
 6 secrets: {
 7   DOCKER_USER: "k8sdemoacr",
 8   DOCKER_PASS: "xxyJ5ON6M4/ur11yl1ta0X6P5g9vZP19",
 9   DOCKER_REGISTRY: "k8sdemoacr.azurecr.io",
10   SLACK_WEBHOOK: "https://hooks.slack.com/services/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"
11 }
```

其中 project 关键字定义了项目名称，repogistory 定义了代码仓库信息，secrets 是针对这个项目的参数信息，在 brigade.js 中可以引用这些参数来进行任务的定制化。yaml 文件创建好后，需要在 Brigade 中进行注册来让 Gateway 开始监听相关项目的事件消息。注册方法如下：

```
helm install brigade/brigade-project -f {project-name}.yaml
```

执行后你会发现在 kubernetes cluster 它会创建一个 kubernetes secrets 对象，将上述信息存入其中，后续可以被 Job 中创建的容器来加载使用。

通过上面的定义我们示例中的 CI 流水线已经定义好了，下面我们来配置一下 Github 和 ACR 中的 Webhook，然后再在 Slack 中配置一下消息接收。

Github Webhook 配置方法如下，进入到自己的 Github 项目中，选择 Setting -> Webhooks，然后选择 add webhook，Content Type 选择 application/json，Payload URL 填入通过 kubectl get svc 中获取的 brigade-brigade-github-gw 的公网地址按照 “http://YOUR_HOSTNAME:7744/events/github” 格式填写。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BE%AE%E8%BD%AF%E5%AE%B9%E5%99%A8%E5%91%A8%E8%BE%B9%E7%8E%A9%E5%85%B7%E4%B9%8B%20Brigade%20%E7%AF%8702.png)

ACR 的 Webhook 配置方法如下，在 Azure Portal 选择创建的 ACR，选择 Webhook -> Add, Service URI 按照 http://YOUR_HOSTNAME:80/events/webhook/**nonokangwei/brigadedemo**?commit=master 格式进行输入，其中 **nonokangwei/brigadedemo** 替换为你们自己的项目名称，这里的名称需要与在上述 project yaml 文件中定义的 project 名称一致，这样当事件消息进入 Gateway 后，Gateway 才可以知道该消息归属哪一个项目该如何进行处理。

Slack 可以登入 https://api.slack.com/incoming-webhooks 来定义侦听器。

下面我们来对整个流水线进行仿真，在该项目中定义了一个简单的 python flask 框架的 Web 程序，在 github 中对 Web 程序进行更新并发布，然后来观察整个流水线的执行情况。编辑 github 中的 app.py 文件，将 Hey 替换为 Hello 并 commit 提交。kubectl get pods 会看到一个名为 dind-01cx5x48c5cmnbtsmry84pwxz9 的 Pods 被创建开始执行，该 Pods 对 Github 的 Push 事件消息进行处理，开始 Docker Build 的操作，操作成功后将 Build 好的镜像发布至 ACR，ACR 收到镜像后，触发 Webhook 发出事件消息，此时在 kubernetes cluster 中看到一个名为 slack-notify-01cx5xb79t3z6fc3552d28h869 的 Pods 被该事件触发，然后发出 Slack 的通知消息，最后在 Slack 中我们收到有新镜像可用的通知消息。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%BE%AE%E8%BD%AF%E5%AE%B9%E5%99%A8%E5%91%A8%E8%BE%B9%E7%8E%A9%E5%85%B7%E4%B9%8B%20Brigade%20%E7%AF%8703.png)

通过上面一个 CI 流水线的示例，相信大家已经对 Brigade 有所了解，Brigade 是一个开源的借助 Kubernetes 来实现事件驱动事务处理编排的工具，并且其原生提供了很多常见事件网关和任务容器镜像，方便大家做流水线化的事务编排。最后给再分享给大家一些学习资料，方便大家快速上手。

# 阅读资料：

1. Brigade 手册列表： https://azure.github.io/brigade/topics/

2. brigrade.js 开发说明：  https://azure.github.io/brigade/topics/scripting.html  必读，可以帮助你快速掌握 brigade 的开发方法

3. brigade SDK 类库字典：https://azure.github.io/brigade/topics/javascript.html 不懂的地方就查查字典
