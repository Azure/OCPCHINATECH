在上一篇文章中，我们创建好了一个AKS集群，并通过在集群中起pod的方式登录到node节点上，在平日的运维中，显然通过pod登录的方式是比较麻烦的，这里我们也可以通过其他更简单的方法去登录：
1，通过跳板机登录
2，通过loadbalancer登录
3，通过Azure Portal上的串行控制台登录
AKS中的node节点本身也是虚拟机，这些虚拟机包括其所在的VNET，存储等基础信息统一在MC_开头的资源组里，因此登录node节点其实就是登陆到AKS所创建的特定资源组的虚拟机上。本篇文章将演示第一种和第三种场景，第二种留着大家自行实践吧~

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式1.png)

1，通过跳板机登录
首先在node虚拟机所在的资源组中，创建一台名为JumpBox的虚拟机，注意location，vnet要和集群相同：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式2.png)
 
然后登录到这台跳板机上：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式3.png)

同一vnet下的资源是可以相互ping通的，找到你要登录的那台node的私有地址，这里我们选择node2：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式4.png)
 
然后在JumpBox登录node，注意在登录之前，我们需要先在node2虚拟机上修改一下登录账号和密码，因为在创建集群的时候，默认登录方式为秘钥对方式，登录用户名默认为azureuser，我们在portal上重置用户名和密码之后再通过进行登录：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式5.png)

登录成功，我们查看一下Node的container情况，

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式6.png)

显示了相关信息，是的，登录过程还是相对简单的（如果过程中提示resource unavailable，查看下机器网卡的NSG有没有开22端口），嗯，其实为了方便运维人员操作，Azure还在portal上提供了一个串行控制台界面，这种可以让使用人员快速的看到本台机器的情况，相当于省去了手工ssh到这台机器的步骤，下面演示一下。
3. 通过Azure Portal上的串行控制台登录
先在portal上找到你要登录的node虚机，页面左侧找“串行控制台”：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式7.png)

点开控制台后直接登录你会发现报错的，正常，报错提示需要先开启诊断日志，按图索骥我们先开一下这个功能，就在上图左侧红框上数3个“启动诊断”部分：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式8.png)

诊断日志可以单独创建一个存储来保存这些日志，保存修改成功后如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式9.png)

然后我们再回到串行控制台登录，直接输入密码后成功登录：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS初体验%EF%BC%882%EF%BC%89%EF%BC%9A登录到node节点的几种方式10.png)
 
至此两种登录node的演示完成了，还有一种创建loadbalancer,后端池挂上node所在的subnet,然后再LB上配置NAT规则，也可以实现登录到node虚拟上，这个大家可以自行实践。
希望这篇文章对大家有用。
