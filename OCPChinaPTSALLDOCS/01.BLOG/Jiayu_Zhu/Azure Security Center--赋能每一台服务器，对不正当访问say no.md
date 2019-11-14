自从木马病毒的产生，加上比特币这类数字型货币的产生，攻击企业环境已经慢慢成为了一个黑色产业。利用企业在生产环境中的一些疏于防范的设置，如服务器都采用类似的用户名和密码，或者同一组用户名和密码管理不同的几台物理机或虚机的生产环境，攻击者只需要购买相应的工具或者材料，就可以轻松的对用户的生产环境进行最直接的暴力破解，或者撞库等操作进入到企业的环境中，之后以加密主库，删除所有从库的方式逼迫企业付费，从而获利。
根据来自“Microsoft安全情报报告”，再进入2018年以后，上述勒索病毒已不再是企业或个人遭受最多的来自恶意软件的攻击。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%201.jpg)

随着全球数字货币的建立，攻击者发现了还有另外一种更为方便的直接获利的方式，就是用别人的计算机算力来挖矿：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%202.jpg)

可以看到，在2018年挖矿软件的遭遇率已经是勒索软件的两倍之多。对于攻击者来说，挖矿软件的普遍性使得其攻击成本大大降低，挖矿软件可以通过不同的方式加载到受害者的计算机终端，来为攻击者提供算力进行挖矿。甚至现在市面上已经出现了不需要透过恶意软件渗透到终端进行安装后挖矿，而直接基于游览器的方式，让用户在访问网站的当下，在后台进行挖矿（例如像：Brocoiner）。
因此对于企业级用户，如何管理企业环境内数百数千台机器，减少暴露给这些恶意软件的攻击面变得尤为重要。接下来，我们就一起来看下，Azure安全中心是如何帮助企业从多个维度来降低被打击面，保护企业应用环境。
为了使用Azure安全中心中的高级云防御等功能组，需要先把订阅升级到标准版：https://docs.azure.cn/zh-cn/security-center/security-center-get-started。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%203.jpg)

之后点击左侧的“入门”，拉到最下面，勾选账号内的相关订阅，点击“开始试用”。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%204.jpg)

接下来就需要给Azure中的VM安装Azure Monitoring Agent来搜集数据，这里可以通过“安全策略”中选择开启“自动预配”来实现：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%205.jpg)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%206.jpg)


对于工作区的配置，可以选择一个为安全中心创建的默认命名方式的工作区，胡总和选择自己已有的一个工作区。下拉以后还需要选择对Windows 安全事件的提醒，这里，微软已经参考行业标准，以及客户对于不同安全事件的敏感程度进行了分级，例如像此集用户成功和失败的登录的事件（事件 ID 4624 和 4625），则会包含在“最小”这个等级及以上的事件提醒中。而像用户注销（事件 ID 4634）之类的事件，只有在选择了“通过”及以上等级的情况下才会被采集及记录。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%207.jpg)

在设定完毕以后，等候一段时间，就可以在“推荐”中看到建议的安全措施，来提高整个Azure环境中的安全程度：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%208.jpg)

如果想要从不同的资源属性，更细致的看到建议，就可以选择进入“推荐”下面各大块资源组中，来查看一个门类的资源中碰到的建议，从而可以更系统的看到某块资源集中性的问题所在。更好的把握企业云上环境潜在的攻击面及短板。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%209.jpg)

另外，您也可以选择把Azure的安全中心扩展到其他非Azure上的虚拟机资源，或者与公司现有的SIEM平台相整合，形成一个统一的监控门户。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2010.jpg)

介绍完上述针对不同资源的建议事件，我们来继续深入看在防御的功能点上，如何才能真正做到不同程度对于云端生产环境的保护。
在现在的企业环境中，为了做到更好的防御，企业首先需要做到的就是减少自己攻击面，不暴露自身的任何信息到外部，也正是出于这样的一个概念，企业中开始流行一个概念叫做“Zero Trust”，即对于每一个访问企业服务器，应用或数据的访问者保持零信任。每台服务器在被访问时就应该询问访问者：“你是谁？（Who?）”，“你为什么要来？(Why?)”，“你要去哪里？(Where?)”。
 
“你是谁？(Who?)”
在对企业发起任何的攻击之前，拿到访问凭据是所有事件的开始，与之相对应的措施就需要比如访问者做多因子认证来做身份的二次校验。此功能包含于Azure AD 中，此处不做介绍。
 
“你为什么要来？(Why?)”
当攻击者凭着初始凭据进到企业内部以后，他们会进行长时间的潜伏，其首要目标，就是获得企业超级管理员的凭据，从而可以直奔企业的核心数据。而有些防范疏忽的企业往往一个超级管理员就可以登录企业大部分的服务器，或者很多服务器的管理员账号的用户名和密码的组成有很大的相似之处。从而让攻击者可以肆意地在企业环境中游动。
因此，对于所有的服务器或者数据的访问都推荐依照JIT（Just In Time）原则来进行访问。其道理就是，针对核心的服务器，首先需要减少所有不必要的超级管理员的账号，其次，相关操作人员再登录时，需要额外审批才能在有限时间内进行访问等操作，这样才能有效的降低企业生产环境所暴露出的攻击面。
作为Azure安全中心的核心功能之一，实时VM访问，就是为了给到客户最直接的管理企业云端核心虚机的访问控制的方式。
其原理是通过根据客户设定的JIT的策略，来实时改变虚机上的网络安全组（NSG）的策略，保证特定端口和访问来源的IP保持关闭状态，并且企业允许的运维窗口期进行有限的开放。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2011.jpg)

接下来我们一起来看下如何通过Azure安全中心来设置JIT策略，首先选择你的目标管理虚机，点击”在X个VM上启用JIT”:

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2012.jpg)

之后，你就可以配置如下图，对每个端口，访问来源的IP地址进行可用访问时效的限定：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2013.jpg)

再设置完毕后，点击保存之后，那虚机就会对于设定的端口从NSG规则上设定为关闭状态，我们回到上一页就可以看到，虚机会转移到“已配置”的数据下面。之后如果需要对于JIT策略中规定的端口进行连接和访问，就需要从安全中心中，选中该虚机，“请求访问”：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2014.jpg)

并且只有如下图所示，指定访问的源IP，才能开启NSG规则，让该端口只对你需要针对的IP可访问：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2015.jpg)

并且，再有效的时间到期后，该端口又会关闭，但已经连接的访问不会受到影响，将可以继续访问该虚机。
 
“你要去哪里？(Where ?)
当用户在经过层层审核，进入到服务器以后，我们仍旧需要秉持“Zero Trust”原则，对于用户的行为进行有效的约束。我们从服务器自身来看，企业中的每台服务器都应该各司其职，跑着某一些特定的应用，特别在云端，用户可以通过对于CPU和内存的拆分，将原先运行在本地同一台物理机上的几个应用分隔到云端的不同机器上，相关之间的环境完全独立。那即使用户登录到其中的一台服务器上，也需要主动阻止其访问比如游览器或者其他应用，减少引入其他的危害。
然后很多企业都知道应用白名单制的方式可以大大降低企业的攻击面，但这个规则的应用面却一直不广，其原因在于，人为的确定每一台不同服务器允许的应用程序，并找出相关路径加入白名单的方式无法在复杂的企业环境中被普及，可行性很低。而现在通过Azure安全中心中的“自适应应用程序控件”就可以借助微软强大的机器学习的能力，帮助企业管理云端Windows的服务器，建立应用程序的白名单，管理对于应用程序的访问，从而加强虚机对于恶意软件的防御能力。
接下来我们进入“自适应应用程序控件”来看下如何对虚机的可访问的应用进行控制。
如果你刚开始使用此功能，则在推荐的目录下不会有任何的组别出现，因为安全中心需要至少两周的数据，学习每个虚机的行为，才能为虚机创建基线，并将行为类似的虚机归纳成一个虚机组给出建议。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2016.jpg)

这里我们监控了一台Exchange2016的Server，来看下安全中心推荐的规则控制，我们点击“GROUP1”。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2017.jpg)

接着我们看到了在这一组别中包含的虚拟机以及该虚拟机上频繁使用的应用，点击创建以后，安全中心就可以借助AppLocker为以下应用针对某一些用户开启白名单访问规则。
等待片刻后，规则生成完成，该组别就会转到“已配置”目录下，我们接着来看下该组别虚机的监控情况：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2018.jpg)

对于自动创建的应用程序控制规则，用户可以选择“审核”，即不强制实行规则，而是监控VM上的行动，如果企业在初始实施过程中，建议对于大多数的机器应用此项规则。“强制”则自然是明确阻止不允许的应用程序，建议再实行一段时间“审核”状态下的VM后，对于特定的虚机进行强制管控。
如果客户觉得自动学习到的虚机上的应用程序白名单不够完善，也可以手动通过“策略扩展”部分，手动添加允许的应用程序的路径。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2019.jpg)

根据虚机上应用的属性的不同，以及访问用户的不同，Azure安全中心会按照“发布服务器允许列表规则”，“路径允许列表规则”以及“哈希白名单规则”将不同的的被允许的应用自动归类。如果对于允许的用户有不同的设置，用户也可以通过右侧点击相应的规则来勾选不同的允许的用户。
在对虚拟机的访问和行为进行控制后，实际对于机器自身的监控也是必不可少的，例如定时check注册表的变化，或者操作系统级别是否有更改。
在Azure的安全中心里，就提供了对于这些可能代表了遭受攻击后所造成的更改的监控模块—文件完整性监视（FIM），在启用了FIM以后，安全中心会对以下文件的活动进行监视：
- 文件和注册表的创建与删除
- 文件修改（文件大小、访问控制列表和内容哈希的更改）
- 注册表修改（大小、访问控制列表、类型和内容的更改）
接下来我们来看下FIM是如何工作的，首先我们选择手头的一个工作区来开启FIM：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2020.jpg)

点击“Enable”：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2021.jpg)

在这个工作区中，我们来细看下，对于工作区内的Linux虚机会查看哪些文件地址：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2022.jpg)

勾选完所需要追踪的文件路径，点击启用FIM后，就会对所应用的虚机进行更改追踪。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2023.jpg)

如果想要对自定义的一些文件路径也进行追踪，可以点击“设置”，来添加某个注册表或者文件的改动。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2024.jpg)

以上便是Azure安全中心的高级云防御来从三个维度以上（3W）来帮助企业缩小环境的受攻击面，做好防范措施。
不仅如此，Azure安全中心还提供一项看似简单，然后实则依托于丰富的微软多年来处理安全事件的经验，结合机器学习对于客户环境的日志的分析生成的“警报功能”。
在传统的客户实践中，客户需要雇佣专业的安全团队或者人士，需要大量的人力，财力去将公司数百万甚至数千万条的日志中，抓取出一系列可能相关的，导致企业安全事件的动作，来一点一点的顺藤摸瓜，找到最终的安全隐患或者源头。但随着现代企业环境的复杂程度越高，大数据分析，机器学习的产生，传统的，靠人工，靠经验的排查方式变得成本更好，且实施难度更大。
而微软则将多年来，各大平台的运维上的安全团队专家的经验，结合云端强大的大数据清洗，筛选的能力，又用机器学习平台进行赋能。将这些结合到一起，呈现给客户如下的，自动生成的，安全警报分析监控面板。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20Security%20Center--赋能每一台服务器%EF%BC%8C对不正当访问say%20no%2025.png)

Azure 安全中心自动从 Azure 资源、网络和合作伙伴解决方案（例如恶意软件和防火墙）收集、分析和融合数据。检测到威胁时会创建安全警报。这些威胁都会按类别被分析到，如虚拟机行为分析，网络分析，SQL数据库和SQL 数据仓库分析以及上下文关联分析。
以虚拟机行为分析为例，大到虚拟机被暴力破解的事件，小到一个隐藏文件被执行，一个带有随机名称的进程被启动等超过70多种的事件，都会根据日志中不同记录间的关联性被分析得到。
但是，与此同时，微软又结合专家团队的经验以及威胁智能（Threat Intelligence）将这些安全警报依据对于客户环境不同的影响程度进行严重程度分类，这样使得用户能够在看到企业内的所有事件的同时，有优先级地去处理此类事件。
虽然现在很多企业面临的形式是：攻击者的攻击模式日益复杂，企业自身的工作负荷，运维环境也由传统的单一数据中心化转向本地+云+SaaS的混合化，与之相对应的确是严重缺乏安全团队进行保护。利用Azure安全中心，企业就可以主动进行全方位的防御措施，另外也不用担心攻击者的手段推陈出新，企业拥有的将是浓缩世界顶尖的安全团队应对威胁的经验以及7*24不间断，反应迅速的监控中心。这样就能专注于业务层面的创新，迭代，没有后顾之忧。
