最近碰到一个客户要用IaaS搭建Cloudera，本来还想这产品这么多年也应该成熟了，安装总归三下五除二就能搞定吧，没想到用习惯了HDInsight之后，再回去搞这个，还真有些不习惯。而且CDH都已经这么多年了，没想到bug也还真是不少啊，Troubleshooting起来也费劲。
搭建本身倒没什么好说的，就是看着这么多步骤有点惆怅。
https://www.cloudera.com/documentation/enterprise/6/6.1/topics/install_cm_cdh.html

准备集群，关掉SELinux关掉防火墙，配好Host NTP，大概有下面这么多步：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用惯了PaaS%EF%BC%8C再回去搭Cloudera一言难尽啊1.png)


准备完了开始安装，又大概有这么多步，手动惊恐。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用惯了PaaS%EF%BC%8C再回去搭Cloudera一言难尽啊2.png)

这么多步骤不知道为什么不搞成一个wizard..照理很多都是可以脚本搞定的，尤其是数据库那块，不知道为什么明明给了他数据库信息，还要自己去创建数据库给权限（一不小心还给错一个，troubleshooting了半年），此刻无比怀念一个命令下去然后去倒杯咖啡等安装完成的HDInsight
好了总算完成了安装，他们要Hive on Spark，那么试一下吧，火速弄完TPC-DS的数据，开始倒到Hive表里，刚跑两分钟，OOM了。。我这可是64G内存的机器啊。。一看默认配置。。只给了Spark 1G，有点黑人懵圈。当然这都是小问题~，改完之后总算成功跑起来了。
数据每天导入怎么搞呢，他们的习惯是Hue里面去建Oozie的Workflow. 好，三下五除二去Hue里配好一个sqoop任务的workflow开始跑起来。好了，又报错了。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用惯了PaaS%EF%BC%8C再回去搭Cloudera一言难尽啊3.png)

这个Error Message。。看了半天Error Log完全没有任何有用的信息。。
最后搜了好久，居然是一个Bug
https://issues.cloudera.org/browse/HUE-8717

看完他的Fix目瞪狗呆，并不是我的配置有什么特殊，而是他的一段python代码写错了，Hue配置一个Sqoop的workflow不是一个基本的功能么，给我的感觉，好像产品发布之前都没测试这个。
好按照他的Fix来，要升级Hue到4.4，那么问题来了，怎么升

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用惯了PaaS%EF%BC%8C再回去搭Cloudera一言难尽啊4.png)

看到这个消息我的内心是绝望的。。
怎么办，只能按照这个bug上提供的Fix手动workaround，好在并不繁琐。改完后大功告成啦。。
此刻无比怀念傻瓜安装，碰到问题可以开工单的HDInsight.
