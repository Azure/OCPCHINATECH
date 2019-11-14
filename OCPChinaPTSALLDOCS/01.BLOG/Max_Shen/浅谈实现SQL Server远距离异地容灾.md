SQL Server 从2012 推出 SQL Alwayson 以来，使我们对SQL Server数据库容灾产生翻天覆地的变化。 其优点很明显

1、不依赖于特殊硬件

2、可以跨越子网

3、现在已经可以支持到9个副本，包括一个主副本和两个同步提交辅助副本。

 ![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%B5%85%E8%B0%88%E5%AE%9E%E7%8E%B0SQL%20Server%E8%BF%9C%E8%B7%9D%E7%A6%BB%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BE01.png)

于是我们诞生了像如下图的容灾方案，跨越数据中心的方案，如异地容灾。 也有用户使用此方案实现云端和本地的数据容灾，并且还可以实现故障转移。

看起来也是很完美的方案，实施的过程中很多用户发现alwayson会无缘无故的出现故障。在配置过程中可以配置HealthCheckTimeout 属性以放宽SQL Server的check 时长。

此属性的默认值为 60,000 毫秒（60 秒）。 最小值为 15,000 毫秒（15 秒）。

但是设置了这个参数也会出现问题。因为在通常的alwayson的依赖于windows 群集WSFC运行，WSFC虽然现象可以跨越子网，实现多子网的群集，但是WSFC也需要依赖于心跳进行CHECK系统是否正常。而这个对网络要求稳定性较高。心跳的时间要求如下 。

| Parameter | Default | Range | 
| ---- | ---- | ---- |
| SameSubnetDelay | 1000 milliseconds | 250-2000 milliseconds |
| CrossSubnetDelay | 1000 milliseconds | 250-4000 milliseconds |
| SameSubnetThreshold | 5 | 3-10 |
| CrossSubnetThreshold | 5 | 3-10 |

因此会出现情况，由于物理距离，云上和本地的延迟不可避免，再由于网络的波动，会导致windows群集心跳认为对方故障，而出现alwayson故障。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%B5%85%E8%B0%88%E5%AE%9E%E7%8E%B0SQL%20Server%E8%BF%9C%E8%B7%9D%E7%A6%BB%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BE02.png) 

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%B5%85%E8%B0%88%E5%AE%9E%E7%8E%B0SQL%20Server%E8%BF%9C%E8%B7%9D%E7%A6%BB%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BE03.png)

因此在运维层面来讲，会出现很多的问题。虽然alwayson解决了数据的容灾备份的问题，但是网络很难实现远距离的高质量的要求。

SQL 2016 有了新的功能，来帮助实现新的构架，满足跨区域容灾备份的要求，并且实现性能横向的扩展。

# 分布式可用性组
这个功能就是 ：分布式可用性组

分布式可用性组可为跨多个数据中心的可用性组提供更加灵活的部署方案。 对于过去在灾难恢复等方案中使用日志传送等功能的情况，现在甚至可以使用分布式可用性组。 不过，与日志传送不同，分布式可用性组不得包含延迟的事务应用程序。 这意味着，对于错误更新或删除数据的人为过失事件，可用性组或分布式可用性组无法提供帮助。

分布式可用性组是松散耦合的，在这种情况下，这意味着它们无需单个 WSFC 群集，并且它们由 SQL Server 维护。 由于 WSFC 群集是单独进行维护的，且最初在这两个可用性组之间异步同步，因此很容易在其他站点配置灾难恢复。 每个可用性组中的主要副本都同步其自己的次要副本。

* 分布式可用性组仅支持手动故障转移。 在切换数据中心的灾难恢复情况下，不应配置自动故障转移（除极少数例外）。

* 很可能无需为多站点或子网 WSFC 群集设置某些传统项或参数（如 CrossSubnetThreshold），但仍需了解数据传输的另一层的网络延迟。 不同之处在于，每个 WSFC 群集都维护其自身的可用性；群集并非包含四个节点的大型实体。 如上图所示，实际有两个单独的双节点 WSFC 群集。

* 建议采用异步数据移动，因为此方法将用于灾难恢复目的。

* 如果在主要副本和第二个可用性组的至少一个次要副本之间配置同步数据移动，并在分布式可用性组上配置同步移动，则分布式可用性组将等待，直到所有同步副本确认它们具有数据。

单个分布式可用性组最多可拥有 16 个次要副本，具体视需要而定。 因此，它最多可拥有 18 个副本供读取，包括不同可用性组的两个主要副本。 此方法意味着，多个站点可实现近实时访问，以便向各应用程序报告。与仅使用单个可用性组相比，分布式可用性组可帮助扩大只读场。 分布式可用性组可通过两种方式扩大可读副本：可使用分布式可用性组中第二个可用性组的主要副本来创建另一个分布式可用性组，即使数据库未处于恢复状态。还可以使用第一个可用性组的主要副本来创建另一个分布式可用性组。换句话说，就是主要副本可以参与两个不同的分布式可用性组。 下图显示 AG 1 和 AG 2 均参与分布式 AG 1，而 AG 2 和 AG 3 参与分布式 AG 2。 AG 2 的主要副本（或转发器）是分布式 AG 1 的次要副本和分布式 AG 2 的主要副本。

 ![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%B5%85%E8%B0%88%E5%AE%9E%E7%8E%B0SQL%20Server%E8%BF%9C%E8%B7%9D%E7%A6%BB%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BE04.png)

下图显示 AG 1 为两个不同分布式可用性组的主要副本：分布式 AG 1（包含 AG 1 和 AG 2）和分布式 AG 2（包含 AG 1 和 AG 3）。

 ![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%B5%85%E8%B0%88%E5%AE%9E%E7%8E%B0SQL%20Server%E8%BF%9C%E8%B7%9D%E7%A6%BB%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BE05.png)

 ![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%B5%85%E8%B0%88%E5%AE%9E%E7%8E%B0SQL%20Server%E8%BF%9C%E8%B7%9D%E7%A6%BB%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BE06.png)


在前面两个示例中，三个可用性组中至多可以具有 27 个副本，这些副本可用于只读查询。

**无论是那种分布式的方案，好处都显而易见，每个环境中都有一个群集，因此群集的检测可靠性能够解决，而远程的容灾由alwayson去完成，在数据库层完成,这样更加稳定。**

分布式可用性组是一种特殊类型的可用性组，它跨两个单独的可用性组。 加入分布式可用性组的可用性组无需处于同一位置。 它们可以是物理也可以是虚拟的，可以在本地、公有云中或支持可用性组部署的任何位置。 这包括跨域甚至跨平台 - 例如一个可用性组托管在 Linux ，一个托管在 Windows 上。 只要两个可用性组可以进行通信，就可以使用它们配置分布式可用性组。

在SQL 2017 里面创建alwayson时候可以有三个选项：widows 故障转移群集、external、None

* Windows Server 故障转移群集

当可用性组托管在属于 Windows Server 故障转移群集的  SQL Server 的实例上时使用，以实现高可用性和灾难恢复。 适用于所有受支持的  SQL Server 版本。

* EXTERNAL

当可用性组托管在由外部群集技术（例如 Linux 上的 Pacemaker）管理的  SQL Server 的实例上时使用，以实现高可用性和灾难恢复。 适用于 SQL Server 2017 (14.x) 及更高版本。

* NONE

当可用性组托管在不由群集技术管理的  SQL Server 的实例上时使用，以实现读取缩放和负载均衡。 适用于 SQL Server 2017 (14.x) 及更高版本。

因此在SQL 2017 环境中是可以不依赖于windows 群集，也可以跨越操作系统，提供了更多的容灾的方案。 特别是私有云和公有云之间的数据同步和容灾实现。
