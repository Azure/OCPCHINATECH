 请一篇介绍了Azure内置的DNS服务，虽然很方便，但是也有不少缺点，例如无法跨vnet、不能自定义域后缀、只对VM生效等。而在Global上线的Private DNS Zone服务完美的解决了这个问题。
## Private DNS Zone创建
  Private DNS Zone的创建很简单，在所有服务里搜索DNS等关键词就可以找到：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%201.png)
  
  进入后就可以创建Private DNS Zone：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%202.png)
 
 进入后就可以创建Private DNS Zone：
  创建Private DNS Zone很简单，只需要资源组、Private DNS Zone的名字（域后缀格式）、区域（与资源组一致，无法修改）即可：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%203.png)
  
  进入后就可以创建Private DNS Zone：
  创建完成后，就有了一套私有的DNS服务系统：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%204.png)
  
  进入后就可以创建Private DNS Zone：
## Private DNS Zone配置
  Private DNS Zone的配置主要有两部分内容：作用的vnet以及解析记录。
### 配置vnet
  测试环境提前准备了两个vnet：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%205.png)
  
  进入后就可以创建Private DNS Zone：
  将DNS作用在vnet的地方是Private DNS Zone的setting-Virtual network links：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%206.png)
  
  进入后就可以创建Private DNS Zone：
  点击Add添加vnet：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%207.png)
  
  进入后就可以创建Private DNS Zone：
  可以看到，甚至可以添加不同订阅的vnet。
  现在把vnet01添加进来，并且选上Enable auto registration:

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%208.png)
  
  进入后就可以创建Private DNS Zone：
  同样添加vnet02，但是不选Enable auto registration。两个vnet添加后如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%209.png)
  
  进入后就可以创建Private DNS Zone：
  vnet配置完成。
  
  *注：一个Private DNS Zone添加多个vnet，但是一个vnet只能配置一个Private DNS Zone*
### 添加解析记录
  在Private DNS Zone里添加解析记录有两种方式：手工添加记录和VM自动注册。当vnet在Private DNS Zone里AUTO-REGISTRATION选项Eabled时，创建的VM会自动注册。
#### 自动注册DNS
  创建一台VM，虚机名vm01，使用vnet01网络，内网ip是10.1.0.4：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2010.png)
  
  进入后就可以创建Private DNS Zone：
  现在去看Private DNS Zone的解析情况，可以看到vm01已经自动注册到DNS：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2011.png)
  
  进入后就可以创建Private DNS Zone：
  如上一篇文章描述，Azure的默认DNS是基于主机名而非虚机名，修改主机名后，DNS会自动更新，测试在Private DNS Zone是否同样情况。先去vm01里修改主机名：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2012.png)
  
  进入后就可以创建Private DNS Zone：
  再检查DNS记录：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2013.png)
  
  进入后就可以创建Private DNS Zone：
  没有发生变化。
  再检查vm01的主机名配置文件，也没变化：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2014.png)
  
  进入后就可以创建Private DNS Zone：
  检查waagent配置文件，监控主机名变化的参数被设置为n：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2015.png)
  
  进入后就可以创建Private DNS Zone：
  现在修改waagent配置文件，再做一次修改主机名的测试：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2016.png)
  
  进入后就可以创建Private DNS Zone：
  OS层修改成功。
  
*注：新版waagent在Linux里的服务名是walinuxagent，不是waagent*
  再检查Private DNS Zone的记录：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2017.png)
  
  进入后就可以创建Private DNS Zone：
  从Azure将vm01取消分配并重新开机，再检查Private DNS Zone的记录，这次更新了：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2018.png)
  
  进入后就可以创建Private DNS Zone：
  通过以上测试可以发现，当vnet启用了DNS自动注册，附加到该vnet的VM将自动屏蔽对主机名修改的监控；如果希望修改主机名后自动更新DNS记录，需要修改waagent配置参数，并在修改主机名后从Azure重启VM才能更新。
#### 手工注册DNS
  创建一台VM，虚机名vm02，使用vnet02网络，内网ip是10.2.0.4（为了政治正确，这次忍痛割爱，创建一个windows的VM）：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2019.png)
  
  进入后就可以创建Private DNS Zone：
  由于vnet02没有启用DNS的自动注册，所以创建完VM后，DNS记录里没有自动添加：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2020.png)
  
  进入后就可以创建Private DNS Zone：
  在vm01上也无法查找到vm02：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2021.png)
  
  进入后就可以创建Private DNS Zone：
  现在手工为vm02添加一条解析：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2022.png)
  
  进入后就可以创建Private DNS Zone：
  添加完成，在DNS里可以看到：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2023.png)
  
  进入后就可以创建Private DNS Zone：
  稍待片刻，在vm01上解析到vm02：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2024.png)
  
  进入后就可以创建Private DNS Zone：
  当然，由于vnet01和vnet02是两个独立vnet，vm01和vm02之间虽然可以解析，但不能通讯：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2025.png)
  
  进入后就可以创建Private DNS Zone：
  创建vnet01和vnet02之间的peer：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2026.png)
  
  进入后就可以创建Private DNS Zone：
  现在vm01和vm02之间可以互通了：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2027.png)
  
  进入后就可以创建Private DNS Zone：
  
  *注：由于vm02是windows系统，所以要在防火墙允许icmp才能ping通*
  由此可见，通过Private DNS Zone可以实现多个vnet统一DNS解析，实现用域名互通，统一并简化了网络环境。
## 还是看看域后缀那点事
  在vm01上直接ping或查找vm02，还是无法解析：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2028.png)
  
  进入后就可以创建Private DNS Zone：
  这是因为如果解析主机名时，如果不是完整的fqdn名字，系统将自动在主机名后加上默认的搜索域。在linux里，搜索域的设置在/etc/resolv.conf文件里：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2029.png)
  
  进入后就可以创建Private DNS Zone：
  将搜索域修改为需要的域名即可正常：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/我的地盘我做主——Azure%20Private%20DNS%20Zone%2030.png)
  
  进入后就可以创建Private DNS Zone：
## 总结一下
  现在很多场合里，即使在内部网络里边，也需要通过域名方式来访问设备，特别是一些虚拟设备，由于内置程序的复杂，要求必须使用域名（例如EMC AVE）。传统解决方式可以通过在hosts文件里写记录来实现，但是这样操作需要在每个服务器里配置，比较繁琐，而且更新容易出错；而自己搭建DNS服务器管理配置复杂。
  Azure Private DNS Zone提供了一个很好的解决方案，不仅简单易用，而且价格便宜（相对于VM搭建DNS）。希望这个功能也能尽快在Azure China落地。
