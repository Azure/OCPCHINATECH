SIEM，一个已经存在20多年的安全产品领域，一个很多企业所必须的安全事件监控和管理平台，但现在它所承载的功能和价值也随着现在企业办公环境的变化而面临巨大的挑战。

首先，最大的一点的不同在于，企业的安全边界已经改变，何谓企业的安全边界，十年前，可以说是企业所拥有的电脑资产和服务器资产，因为在当时近乎所有的办公都是发生在公司管控范围内的电脑及服务器上。因此只需针对设备做到监管，如限制USB的接入，限制互联网的接入等，就能够很大程度上抵御来自外部的威胁。但如今，不仅企业允许员工自带办公设备，越来越多的企业应用在移动设备端的访问频次的提升。企业已经很难通过管控设备来达到企业信息安全的管控。因此，现在越来越多的企业已经将安全边界的确定，转移到了员工的身上，及从该员工在公司的角色及工作职责范畴来对其在公司企业中的账号的行为进行管控。比如一个前端业务销售，如果登录到企业服务器的数据库的这个行为就可以被界定为可疑，甚至是高危的行为，需要采取安全措施。

其次，数据信息量的爆炸，延展到员工在工作期间需要交互的信息量的暴涨，导致企业中所产生的日志量的规模已几何的形式进行增长，如何在巨量的信息中仍旧能够检索到有利于判断潜在威胁的过程，将会对原本部署在本地的日志搜索引擎的扩展灵活性，及服务器的性能有很高的要求。

最后，不得不说，随着比特币的出现，及其在资本市场中价格的稳定性的提高，这样安全攻击者的获利成本和风险大大降低，也滋养了这样的一个市场，因此对于现在的SIEM来说，常规的安全管理的功能不可或缺以外，其提供威胁情报的分析能力，事件调查和响应的能力成为了各厂商的着重发力点。

一直以来，微软对于安全的重视及相关功能的开发，也一直受到客户的追捧，从最早的RMS Server，Windows ATP到现在云端的Microsoft Information Protection, Office 365 ATP, Azure ATP，这些产品借助云端应用的优势，以及微软在Machine Learning上的积累，各个产品中的分析能力的优势越来越凸显。结合微软在全球的合作伙伴生态圈的建设，各个产品也开始表现出对于第三方的产品，甚至同类的竞品都表现出了极强的延展性。
也正是这样的大环境下，微软推出了Azure Sentinel，在已有的微软一方产品的安全防御及分析的基础上，将云端无限的计算能力及微软安全团队的经验赋能到客户所使用的其他第三方安全产品，从而能够实现对于一个安全事件全视角的分析及追踪能力。
接下来，我们一起就来看下在微软的Azure Sentinel中，大家如何来做企业安全信息和事件的管理及响应。
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%201.jpg)
    Azure Sentinel的默认仪表板首先会将所监控到的所有日志中所产生的事件，网络峰值等信息按时序的展现给客户，并且把从事件所引申出来的威胁警报及案件，作为客户最关心的重点展现在首页。
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%202.jpg)
这些Alerts的汇聚，及案件中各个alert的关联性，都来自于Azure平台所赋予的机器学习的能力，以及微软安全团队专家在应对每天数以亿计的安全事件中如何找到真正威胁所在的经验等，将这个能力转化到Azure Sentinel的平台上，来第一时间甄别出，企业到可疑IP的流量往来；企业内部用户异常的用户行为等警告，第一时间帮助客户防御潜在的威胁。

 ![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%203.webp)
 
为了能够赋能客户已有的安全产品及其他监控组件，客户在使用Azure Sentinel的第一时间就应当来到Data Connector栏，将已有的微软的一方安全产品的日志信息，及三方的日志信息对接到平台上。从目前的支持列表中可以看到，我们不仅支持像F5,Palo Alto，Check Point等主流厂商的快速接入，您也可以通过CEF（Common Event Format）或者Syslog这些常用的日志格式的文件，按配置步骤实现接入。
实例中，我们点击Palo Alto进行配置，之后就可以看到Palo Alto那边的流量信息已经展现在面板上，此外，Palo Alto还与微软合作，将其搜集到的信息，分别由微软和Palo Alto各制作了一款完整的仪表板来展现客户所关心的日志信息的汇总。我们点击Palo Alto设计的仪表板。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%204.jpg)

进入仪表板后，可以看到威胁会按种类，来源的应用及时序的量值按重要性依次从上到下排列在仪表版上，如果您对于默认所展现的列别以及展示的时间段等信息想进行修改，都可以点击各块信息右上角的”Edit Query”来修改所要展示的信息。
     
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%205.jpg)

当你接入好所有一方和三方的日志后，你可以回到首页，从Azure Sentinel左侧的Dash board中看到所有连接的log日志。并且你可以为不同的用户，设定他所可以查看的仪表版中所能看到的数据的权限，来符合所需要满足的合规要求。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%206.jpg)

上述的仪表版只能对于日志呈现一些简单的，大局上的信息，如果需要对于特定的安全事件进行搜寻，则可以通过左侧栏中的“Logs“来对不同日志源中的数据进行统一的搜索和排查。整个Log平台依托于微软的Log Analytics以及Azure Monitor这两个组件，每天都会帮助客户处理10 PB以上的日志数据，客户只需通过短短的几行搜索命令就能够进行复杂的搜索逻辑，并且不需要考虑底层计算平台的算力，快速返回所查询到的结果。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%207.jpg)

当然，你也可以通过左侧的筛选器，对所收集的日志进行简单的分类，从而精准的执行所需要查找的日志数据。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%208.jpg)

另外，很多常用的搜索逻辑，比如查找异常登录信息，可疑IP地址段的提取等，你都可以直接在右侧的Query Explorer中利用微软安全团队已经生成的查询模板，就能够针对你接入的日志数据进行查询，查询的结果你可以根据需要，通过表单形式或者柱状图或者饼状图的形式展现在下方的结果显示栏中。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%209.jpg)

接下来，我们来看下Azure Sentinel中最强大的部分之一，案件的生成。    
我曾经看到一份调查报告，它统计到，在2017年每个企业的安全团队每星期都需要面对近1万7千条的木马警告信息，以及数以十万计的各类事件，这样的一个工作面使得企业团队很难去精准的定位潜在的威胁。
同样的，微软的安全团队每天也需要面对是近四千万行的日志数据，但借助于微软AI所赋能的分析工具以及团队的专业经验，他们每天能将这四千万行的日志数据筛选到只剩100-200个可疑事件。
微软也将这个能力，将专家对于各类事件ID中的洞察力，内置到Azure Sentinel，从而让客户所需要直接面对的，变成呈几何数缩减的警报及案件，能够基于这个点，从点到面的对案件进行调查，找到真正的漏洞所在。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%2010.jpg)

这里的Case（案件）指的是一系列相关Event汇聚而成的一个案件，它可以包括多个不同的警报，并且你可以到Analytics自己定义案件的形成方式（会在后续文章中进行讲解），并且平台会按照案件的严重程度及状态反馈给客户。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%2011.jpg)

案件之所以称之为案件，就因此客户的团队可以按标准流程来跟踪整个案件的进展，比如对案件的负责人进行指派，案件的进展汇报跟踪，结案等，都能通过
案件之所以称之为案件，就因此客户的团队可以按标准流程来跟踪整个案件的进展，比如对案件的负责人进行指派，案件的进展汇报跟踪，结案等，都能通过Azure Sentinel平台以及借助其他工具来实现。
我们回到Demo中，大家可以看到，案件会根据发生的时间顺序，并用不同颜色标明严重程度，标识在界面上。
点击具体的一个案件，它会显示案件的描述，之后点击Investigate。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%2012.jpg)

首先在Investigate中的右侧会把一个事件中相关的Alerts，按时间顺序进行排列。在Investigate初期，Alerts相互之间会处于独立状态。

这里我们已一次异常登录为案件发起点进行调查，点开案件后，针对异常登录自然会有异常登录的机器和异常登录的人员。我们点击人员，可以看到，你可以去查看与这个人员相关联的事件，比如这个人员所参与的其他的相关警告，或者他还在其他机器上的登录记录等。
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%2013.jpg)

之后点开登录的机器，我们拉出与这台机器相关的警报。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Sentinel%20--%20云原生企业安全信息和事件管理平台%EF%BC%88SIEM%EF%BC%89初探系列一%2014.jpg)

    
点开后发现，在anomalous login之后的一个事件点，还有另外一个case，就是该机器上的powershell有异常的活动。这样就把这个可疑用户的行为衍生到它所造成的其他严重的事件。

那一般的，公司的安全团队会从最严重的case开始调查，这样他们按照以上的逻辑倒推回来，就会发现在以前的某个时间，是否存在该机器上的异常登录状态，追踪到具体产生异常登录的用户，并且横向移动看到该用户是否还登录了其他的机器，从而可以拦截该用户到其他几台机器上，甚至根据其产生的危害，禁止其登录所有机器等权限管控动作，快速的降低该事件在未来可能发生在其他虚机上的风险。

 这样的一个调查过程，就能够及时从一个公司内部受危害的点，快速扩展了解到可能泄露的用户名，并看到其潜在的危害面，从而快速切断其对于公司环境内其他部分的影响，及时阻止其进入核心数据部分。
      
以上就是Azure Sentinel 介绍的第一部分，后续我们会来看下Azure Sentinel如何能够主动进行威胁的探查，根据企业自身的员工行为，企业特点来自定义进行安全的主动防御。


