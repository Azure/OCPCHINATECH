# 前言

在IT的世界里，区块链一直扮演着一个革命者，一个秩序打破者的角色。大家一度从技术上认为区块链是一个相当神秘的存在，另外也是一个不合作者的存在。但是当你打开每一个运用区块链技术的真实商业案例的时候，你会发现区块链作为一个单独解决方案的存在，从目前来看不是一个很恰当的选择，从安全性能上都会和其他的架构做一定的整合，来满足商业的需求。

 

# 思路以及架构

这个小实验，主要是想要验证以太坊协议的框架，怎样结合Azure里的PaaS。实验的目标是做一个区块链的简单投票器，所有的投票记录作为交易信息存在区块链里。同时又通过mysql PaaS去建立下链的能力，为以后做数据分析提供便利。在验证用户权限方面，考虑直接使用AAD，这样的话就免去了自己去做鉴权的步骤，方便快速迭代开发。下面我们来看一下架构图。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA01.webp)

# 实现步骤

 

## 第一部分：新建AAD的App, 管理用户验证

1. 创建一个新的AAD下面的App

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA02.webp)

2. 配置一下新建的这个APP属性

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA03.webp)

3. 在Azure上新建一台验证服务器，部署一台AAD验证服务器，目的就是验证客户的权限。看是否可以合法的用户可以进入到后台区块链的投票系统，使开发人员可以避免自己去搭建身份认证系统，让用户通过AAD来管理，是一种PaaS的用户身份管理托管模式。

 

微软给了参考demo的链接如下：

https://github.com/Azure-Samples/active-directory-javascript-singlepageapp-dotnet-webapi

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA04.webp)

4. 在AAD的App中修改reply url的地址，因为我们希望用户身份验证后，直接跳转到区块链的投票页面。我们需要把回复地址中把区块链主机的IP加入。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA05.webp)

5. 在验证服务器上需要修改AAD的信息，现在我们按照demo的知道，把app.js的相应代码修改一下。把Azure上面的tenant和clientID，根据新建的App信息相应填入。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA06.webp)

6. 好了，接下来我们把这个验证服务，放在服务器的apache上，进入登录页面，随后用我们的Azure账号登录，紧接着就能跳转到区块链的投票页面了。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA07.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA08.webp)

## 第二部分：区块链投票主机的搭建

1. 在一台Azure的虚机上开始搭建基于Ethereum的实验区块链系统，主要放在内存中的一个实验系统。作用就是简单的记录投票的行为，最后做一个汇总。那么所有的投票信息就会以区块链的模式存取下来，不能肆意的篡改任何投票内容，做到技术上的公平公开。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA09.webp)

2. 首先你需要安装gancache，一个区块链模拟器，这样你不需要真的去建立区块链的节点，作为开发测试是一个比较好的选择。其次我们再安装一个web3，可以和本地的区块链通过JS来快速的沟通。安装sloc npm包，我们会用solidity语言来写一个简单的投票软件。

源码文件传送站：

 

 

3.  进入node命令行交互界面，载入web3

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA10.webp)

4. 查看一下区块链初始化的结果，列举一下里面建好的账户

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA11.webp)

5. 接下来把刚刚写好的solidity程序编译载入一下。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA12.webp)

6. 下面我们把编译好的代码部署到区块链之中，形成一个之前定义好的区块链合同。其中定义了我们三个被投票人，Nick， Rama，Jose，还有每条投票产生的奖励。大家可看到这个区块链合同有一个地址，这个我们需要记下来，需要再前段交互代码里写入。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA13.webp)

7. 现在我们在前段的JS代码里，把记录下来建立的这个合同地址写入。这样前段的页面就能顺利投票进入到后台的区块链了合同了。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA14.webp)

8. 之前我们已经通过AAD登录了投票页面，现在我们就打开投票的页面，尝试在区块链中投几个票试试啦。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA15.webp)

9. 那么我们现在回到node控制台上，看看我们在页面上输入的投票是否成功了呢？查询一下Rama的数量看看。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA16.jpg)

10. 好了，至此我们已经完成了一个简单的验证，并且交互区块链投票的小应用了。下个章节，我们简单看下如何吧区块链和数据库做个集成。

 

## 第三部分：区块链与MySQL的集成

1. 首先我们在Azure上打开一个MySQL PaaS的实例。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA17.webp)

2. 配置一下访问控制，把区块链的主机加入到可以访问的名单中

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA18.webp)

3. 现在回到node的控制台，登录进mysql。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA19.webp)

4. 先读一下数据库，目前里面没有什么区块链的数据

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA20.webp)

5. 随后我们通过简单的命令同步区块链里的数据到关系型的mysql数据库，以便以后快速的查询或者做数据挖掘。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E5%8C%BA%E5%9D%97%E9%93%BE%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%A6%82%E5%BF%B5%E6%90%AD%E5%BB%BA21.webp)

# 总结：

在哈耶克倡导的自由市场下，他指出好的平台本身不一定要完美到极致，但是在这个平台之上可以孵化出很多创新性的模式。那么区块链和公有云平台两者其实就是一个平台，任何有意思，突破性的技术以及商业模式都是可以在这个丰富的平台上开花结果。在这篇文章中，我们结合了云上的鉴权，数据库，区块链虚机，迅速把想法付诸于实践。在通往自由创新之路上，如何能够摆脱基础架构的繁杂无序，快速搭建自己想要的架构与商业实践，这一切恰恰是Azure云计算能带给大家的优势。

 

# 参考资料：

AAD SSO

https://github.com/Azure-Samples/active-directory-javascript-singlepageapp-dotnet-webapi

 

Azure mysql PaaS 参考资料

https://docs.azure.cn/zh-cn/mysql/connect-nodejs

 

代码传送门

https://github.com/jurejoy/blockchain
