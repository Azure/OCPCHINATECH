最近一段时间，会慢慢开始接触Azure AI相关的知识和服务，做一些实验，来亲身体会一下AI，尤其是Azure提供的AI，可以拿来做什么事情。如果想要了解每一个服务的详细情况，可以在参考资料中的链接找到所有服务的详细介绍。

总体上看，Azure中提供的AI能力主要分为三个层次，每个层次针对不同的人群：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%201.webp)

### Cognitive Services & Bot Framework
认知服务是一组面向开发人员的API、SDK服务，帮助我们快速的将AI的能力引入现有的应用中，来提升应用的智能性和吸引力。认知服务中用到的算法模型都是经过了算法优化，训练，并标准化后的AI模型，对用户透明，用户只需要通过简单的，基于REST API的CRUD的方式，即可使用，只需要搞清楚认知服务的输入及输出含义，即可轻松的在应用中实现AI能力。

认知服务提供5个大类，20几种的服务功能：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%202.webp)

其中，你会发现很多`Custom`开头的服务，这些服务允许你在标准模型的基础上，进行一些定制化的训练，比如`Custom Speech Service`，允许你添加一些专业词汇或特定语调，来丰富你的语音文字的翻译服务。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%203.webp)

下面是Azure官网提供的一张架构图，展示了如何快速的通过Cognitive Service & Bot Framework 与 企业的CRM系统进行集成，来打造企业智能聊天机器人。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%204.webp)

### Azure Machine Learning
认知服务不需要你有机器学习的基础，但有时，会与你自己的意愿不match，你总是想自己去构建一个模型，这个时候你就会用到下面的一系列服务。Azure ML会有多种服务，提供的主要是ML相关的框架，工具以及模型管理、部署、运行的相关服务，只要你有机器学习的相关知识，这些工具可以快速的帮你构建你想要的模型。

Azure ML的服务主要分为：ML 框架；ML相关工具；ML 模型管理工具；ML 模型运行时。

#### *框架*

Microsoft自身参与并提供的框架包括`Microsoft Cognitive Toolkit (CNTK)`和`Open Neural Network Exchange (ONNX)`。同时，对于市面上主流的框架，Azure ML的绝大部分服务是支持或兼容的，主要支持的框架如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%205.webp)

#### *工具集*

Azure ML 中提供了多种用于开发的工具包，方便大家构建机器学习的模型：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%206.webp)

Azure ML 中提供了一种用于数据科学人员开发模型的IDE`Azure Machine Learning Workbench`：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%207.webp)

ML Workbench是支持Windows和MacOS的IDE，基于Python的ML开发工具，支持主流的框架，可以与流行的IDE集成，内置Jupyter Notebook服务及客户端，可以将模型训练及验证运行在本地及云端的虚机或容器环境中，并提供对实验历史纪录的视图，监控及管理工作。可集成AAD来实现企业级权限管控，并支持Git，以实现版本控制。
Azure ML中还提供了一种SaaS服务 ， 来帮助数据科学家快速构建数据模型，而无需代码的编写。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%208.webp)

ML Studio是一个协作型拖放式工具，可用于根据数据构建、测试和部署预测分析解决方案。 其特点是可视化、可拖拽的模型构建方式，以及丰富的数据集资源，同时可以与其他Azure服务进行无缝的结合。
另外一个ML Studio的重要功能在于ML Gallery，这是一个机器学习模型的Community，在这里可以找到针对各行业的垂直解决方案，并可以基于现有的模型进行二次开发。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%209.webp)

Azure ML 提供的最后一个工具集是`Team Data Science Process`，一种帮助科学家融入工程团队的方法论。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%2010.webp)

TDSP一种敏捷的迭代式数据科学方法，可有效交付预测分析解决方案和智能应用程序。TDSP是一种方法论，定义了数据科学的生命周期，项目的标准化结构，数据科学项目所需资源及项目执行所需的工具集等，目标是提高数据科学家与团队的写作能力。TDSP有一个标准化的项目模板，里面规划了代码及文档的结构。

#### *管理工具*

Azure ML的管理服务主要包括`ML Experimentation Service`和`ML Model Management Service`。
Experimentation Service为数据开发人员构造了独立的运行环境，确保脚本的运行在隔离环境中执行。该服务可以管理试验的运行环境，包括跟踪试验的历史记录，并提供与Git的集成，AD的访问控制等。
Model Management Service用来管理和部署ML的工作流级模型。MMS提供模型版本的注册表，并提供自动化的工作流，通过REST API的形式打包和部署ML容器。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%2011.webp)

#### *模型运行时*

当ML模型最终完成，需要部署到生产环境中去时，就涉及到了运行时的支持。基于Azure ML服务开发的模型，既可以发布在云端，又可部署在地端：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%2012.webp)

Azure中，支持部署ML模型的服务（俗称卖铁的铁），主要包括：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%2013.webp)

到现在为止，这一眼终于瞄完了。

有张图，希望可以在选择服务的时候帮到大家：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/瞄一眼%20Azure%20AI%20%26%20Machine%20Learning%20的服务们%2014.webp)

### 参考资料：
Azure AI & ML 服务总览 : https://azure.microsoft.com/en-us/overview/ai-platform/

Azure机器学习探索 ：https://azure.microsoft.com/zh-cn/services/machine-learning-services/

Azure AI Gallery : https://gallery.azure.ai/

Team Data Science Process 详解 ：https://docs.microsoft.com/zh-cn/azure/machine-learning/team-data-science-process/overview
