在上一篇文章中，我们看到了如何对案件通过相关性迅速找到事件发生的根源，但查找到威胁仅仅只是个开端，后续如何流程化的解决这个威胁，实现安全编排和自动相应。也是安全团队所需要去完成的工作，而这个过程，Azure Sentinel作为SOAR平台，也能够帮助客户将整个case解决的流程给自动化。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%201.jpg)

点击View Full Details
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%202.jpg)
点击case最右边的view playbook，就会出现整片右边的菜单栏，这些是微软根据特定的case所预先生成和定义的自动化脚本，您只需一键RUN选择所需要执行的动作，就会触发对应的安全动作。
如果您对于所列的安全修复措施想做额外的修改和补充，您只需点击需要改进的action，通过Logic App自己设计触发的逻辑及动作。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%203.jpg)

此外，在Playbook中，微软现在支持连接ServiceNow, Jira等ticket system来对接到客户的案件平台，对案件做有序的追踪，解决和记录。
除了以上一系列对于安全事件的快速响应机制，Azure Sentinel 还为客户提供了客制化安全防御的功能。
一段时间以来，公众对于安全可能一直存在一种固定认知，即安全与防御是紧密关联的，殊不知，一个成熟的安全团队，也会根据客户的行业属性，长时间对于公司内部应用，人员的使用情况的熟悉，进行主动的威胁追踪。借用Azure Sentinel中的Hunting模块，客户就可以为企业度身定做一款安全的矛，主动地去定位及清扫企业环境可能存在地风险。
举个场景，某企业客户中，他们的安全团队清楚的了解，他们公司设计的应用所在的托管服务器常年都只由同一个用户名做登录，因此，即使公司内部存在其他账号，可能可以被赋予相应的权限，在公司内部受信任的IP登录这台Host，但即使针对这个看似正常的行为，我也希望对这一个行为进行监控。因此他可以通过Hunting对所有这台托管机上新登录的这个操作进行监控及告警：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%204.jpg)

这里，我们就以针对一台服务器的登录情况，建立Query，并定期触发这个搜索，返回相应的结果给到安全团队。
微软的安全专家团队已经为客户可能关心的几十种场景，针对不同的log来源，编写了对应的查询语句脚本，罗列给到客户进行选用。大家可能会比较疑惑的是，Bookmark会有什么用处，其实它是为了方便安全团队在今后的事件中，提前做个标记，方便之后将相关联的事件能够做汇聚，可以把比如服务器上单个用户名的正常登录状态与两三个月前，该用户在其他某处的异常登录状态做关联，分析这个ID的行为状况。从而帮助安全团队对威胁进行预判。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%205.jpg)

点开Query，我们就可以把所有新用户登录成功及登录失败的事件都查看到，并且做了一个计数。
仔细来看搜索语句就可以看到，具体的搜索逻辑在这个查询中是通过Event ID来进行筛选。这里的EventID的4624，4625在Windows Security Log中都指的登录相关的事件。因此如果想了解对应到Linux机器中的登录情况，就可以去搜索在Syslog中对应登录状态的EventID或者EventType来放到查询语句中做查找。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%206.jpg)

如果对于这里所使用的查询语句不太熟悉，建议大家学习Azure Log Analytics中的查询语句的规范。如果是对于使用的场景不太熟悉，则可以借助微软团队建立的Query库中的各种Hunting不同事件的Notebook中进行学习：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%207.jpg)

简单介绍下Azure Notebook，它是微软提供的运行在Azure云平台上的Jupyte rNotebook，帮助大家快速的进行代码的调试和计算而不用担心底层承载的物理机的性能。 Azure 的安全团队也利用这个平台，为客户真实场景中碰到的主动防御的场景，编写了不同的脚本。
点击Clone Azure Sentinel Notebooks,就会跳转到属于每个人自己的Notebook的目录，并且把github上Azure Sentinel中的部分都clone到你的目录中。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%208.jpg)

我们进到其中一个Hunt demo来一起看下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%209.jpg)

在这个Notebook的目录下，微软的安全工程师会按上图所示的逻辑把Hunt的脚本描述清楚，如Description中，会把暴力破解的几个场景罗列并解释清楚，并建议给客户推荐的数据收集来源。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%2010.jpg)

接下来我们来看下如何Hunting攻击者的暴力破解。
首先，当然需要从海量的日志数据中，把可疑的SSH登录的事件都筛选出来，借助Azure在各个组件中内置的检测机制，利用ML的分析能力，在事件发生的第一时间，就能够去判断事件自身是否异常。
那再经过Azure 日志分析的大漏斗以后，就可以定位到发生可疑登录的服务器，找到这些服务器的IP地址等信息，经由其IP找到它与公司内部其他服务器间的流量往来，从而定位公司内部可能遭受公司的整个面。

回到Azure Sentinel的平台，不知道大家是否还记得，在上篇文章中，我们提到过，Case是由Alerts汇聚而成，那想问的是Alerts又是从何而来。那接下来，我们就来看下Alerts的出处，以及是否公司可以根据自己的企业应用使用情况，来自行定义Alerts。
我们回到Azure Sentinel的面板上，来看下Alert是的定义。打开左侧栏的Analytics：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%2011.jpg)

我们就会发现，之前Case中的一系列Alerts其实都来自于这个警报库。那我们也尝试着自己来添加一个Alert，点击左上角的添加：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%2012.jpg)

这里能看到对于一个警报，我们可以自己定义命名警报的名称和严重级别。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%2013.jpg)

然后就是最核心的部分，自定义查询语句，比如对于Azure中所有创建资源的动作，或者流量达到什么峰值之类的。如果对于查询语句不太了解，推荐可以到左侧栏中的Community，跳往Github中，来参考微软安全团队及其他贡献者定义的特殊事件的查询方案。另外对于所需要查询的范围，也可以通过限定操作人员，服务器主机或者IP的形式进行精细查询。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%2014.jpg)

点击蓝色按钮，我们跳转到社区来仔细查看下由微软团队及其他贡献者所定义的警报类型及搜索机制。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%2015.jpg)


进入Detections子目录后就能根据你所连接的数据集，选择相应的Query语句，修改编辑后就可以应用于之后新创建的Alert rule里了。
接下来我们回到Analytics来继续看下可以对警报进行的其他配置。
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20初探系列二之案件调查及追踪%2016.jpg)

在定义完警报的类型及覆盖的主体后，可以接着设定其触发的阈值以及运行的时间表。并且这里可以连接到前文提到的Playbook，从而设定自动化的程序，比如对于虚机暴力破解的警报，可以接入Playbook来启动安全团队较高的响应机制，任命负责人员进行调查等。如果对于一些警报，如果其发生的频次较高，也可以在最后打开压缩的设定，从而降低警报的数量对于安全人员的调查的阻碍。

以上就是对Azure Sentinel的初步尝试，可以看到的是，Azure Sentinel背靠微软强大的安全解决方案以及ML的分析能力，今后会在其与更多的微软一方的解决方案如Office 365 ATP相结合，依托于强大的AAD体系(Azure B2B, Azure B2C)，将监测的颗粒度可以落到每个人员的ID上，帮助企业建立新型的企业安全边界应对当前开放的企业办公环境。保证企业中每个员工灵活高效的办公方式的同时，保护企业的数据及资产安全。
