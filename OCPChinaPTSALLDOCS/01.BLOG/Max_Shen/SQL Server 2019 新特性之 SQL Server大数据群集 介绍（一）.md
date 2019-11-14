从开始SQL Server 2019 预览，SQL Server 大数据群集允许你部署的 Kubernetes 上运行的 SQL Server、 Spark 和 HDFS 容器的可缩放群集。 并行运行这些组件，以使您能够读取、 写入，并处理从 TRANSACT-SQL 或 Spark 的大数据、 使您轻松合并和分析大数据大容量高价值关系数据。

SQL Server 大数据群集是有Linux 容器的群集[Kubernetes](https://kubernetes.io/docs/concepts/)进行协调。

# Kubernetes （k8s）概念

**Kubernetes**的名字来自希腊语，意思是“舵手” 或 “领航员”。K8s是将8个字母“ubernete”替换为“8”的缩写。

Kubernetes 是开放源代码容器业务流程协调程序，可以缩放容器部署，根据需求。 下表定义了一些重要的 Kubernetes 术语：

|      |      |
| ---- | ---- |
| Cluster |	Kubernetes 群集是一组计算机，称为节点。 一个节点控制群集，并指定主节点;剩余的节点是辅助角色节点。 Kubernetes 主机是负责分发在辅助角色之间的工作，并监视群集的运行状况。 |
| Node |	节点运行容器化应用程序。 它可以是物理机或虚拟机。 Kubernetes 群集可以包含的物理机和虚拟机节点的组合。 |
| Pod |	Pod 是 Kubernetes 的原子部署单位。 Pod 是一个或多个容器的逻辑组-和关联的资源需要运行应用程序。 每个 pod 的节点; 上运行节点可以运行一个或多个 pod。 Kubernetes 主机会自动分配到群集中节点的 pod。 |



在 SQL Server 大数据群集中，Kubernetes 负责 SQL Server 大数据群集; 的状态Kubernetes 构建和配置群集节点，将 pod 分配给节点，并监视群集的运行状况。

 

# 大数据群集体系结构

在群集中的节点分为三个逻辑平面： 控制平面、 计算平面和数据平面。 每个平面群集中具有不同的职责。 在 SQL Server 大数据群集中的每个 Kubernetes 节点托管组件的至少一个平面的 pod。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E4%B9%8B%20SQL%20Server%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%BE%A4%E9%9B%86%20%E4%BB%8B%E7%BB%8D%EF%BC%88%E4%B8%80%EF%BC%8901.png) 

# 控制平面

控制平面提供管理和安全的群集。 它包含 Kubernetes 主机SQL Server 主实例，和其他群集级别服务，例如 Hive 元存储和 Spark 驱动程序。

# 计算平面

计算平面提供到群集的计算资源。 它包含在 Linux pod 上运行 SQL Server 的节点。 计算平面中的 pod 分为计算池特定处理任务。 计算池可以充当[PolyBase](https://docs.microsoft.com/zh-cn/sql/relational-databases/polybase/polybase-guide?view=sqlallproducts-allversions)横向扩展组中通过不同数据源如作为 HDFS、 Oracle、 MongoDB 或 Teradata 的分布式查询。

# 数据平面

数据平面用于数据暂留和缓存。 它包含的 SQL 数据池和存储池。 SQL 数据池包含在 Linux 上运行 SQL Server 的一个或多个 pod。 它用于从 SQL 查询或 Spark 作业引入数据。 SQL Server 大数据群集的数据集市将保留在数据池。 存储池包含的存储池 pod 组成 Linux、 Spark 和 HDFS 上的 SQL Server。 在 SQL Server 大数据群集中的所有存储节点都是 HDFS 群集的成员。

 

# 由于需要使用 Azure Kubernetes 服务 (AKS) 来创建SQL Server 2019 的大数据群集。

AKS是容器的集群，下面先解释下容器是什么

# 什么是容器

[容器](https://www.redhat.com/zh/topics/containers)是与系统其他部分隔离开的一系列进程。运行这些进程所需的所有文件都由另一个镜像提供，这意味着从开发到测试再到生产的整个过程中，Linux 容器都具有可移植性和一致性。因而，相对于依赖重复传统测试环境的开发渠道，容器的运行速度要快得多。

* 更高效的利用系统资源

* 更快速的启动时间

* 一致的运行环境

* 持续交付和部署

* 更轻松的迁移

* 更轻松的维护和扩展

* 对比传统虚拟机总结

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E4%B9%8B%20SQL%20Server%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%BE%A4%E9%9B%86%20%E4%BB%8B%E7%BB%8D%EF%BC%88%E4%B8%80%EF%BC%8902.png) 

| 特性 | 容器 | 虚拟机 |
| ---- | ---- | ---- |	
| 启动 | 秒级 |	分钟级 |
| 硬盘使用 |	一般为 MB | 一般为 GB |
| 性能 | 接近原生 |	弱于 |
| 系统支持量 |	单机支持上千个容器 |	一般几十个 |

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E4%B9%8B%20SQL%20Server%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%BE%A4%E9%9B%86%20%E4%BB%8B%E7%BB%8D%EF%BC%88%E4%B8%80%EF%BC%8903.png) 

传统的应用部署方式是通过插件或脚本来安装应用。这样做的缺点是应用的运行、配置、管理、所有生存周期将与当前操作系统绑定，这样做并不利于应用的升级更新/回滚等操作，当然也可以通过创建虚机的方式来实现某些功能，但是虚拟机非常重，并不利于可移植性。

新的方式是通过部署容器方式实现，每个容器之间互相隔离，每个容器有自己的文件系统 ，容器之间进程不会相互影响，能区分计算资源。相对于虚拟机，容器能快速部署，由于容器与底层设施、机器文件系统解耦的，所以它能在不同云、不同版本操作系统间进行迁移。

容器占用资源少、部署快，每个应用可以被打包成一个容器镜像，每个应用与容器间成一对一关系也使容器有更大优势，使用容器可以在build或release 的阶段，为应用创建容器镜像，因为每个应用不需要与其余的应用堆栈组合，也不依赖于生产环境基础结构，这使得从研发到测试、生产能提供一致环境。类似地，容器比虚机轻量、更“透明”，这更便于监控和管理。最后，

容器优势总结：

* **快速创建/部署应用**：与VM虚拟机相比，容器镜像的创建更加容易。

* **持续开发、集成和部署*：提供可靠且频繁的容器镜像构建/部署，并使用快速和简单的回滚(由于镜像不可变性)。

* **开发和运行相分离**：在build或者release阶段创建容器镜像，使得应用和基础设施解耦。

* **开发，测试和生产环境一致性**：在本地或外网（生产环境）运行的一致性。

* **云平台或其他操作系统**：可以在 Ubuntu、RHEL、 CoreOS、on-prem、Google Container Engine或其它任何环境中运行。

* **Loosely coupled，分布式，弹性，微服务化**：应用程序分为更小的、独立的部件，可以动态部署和管理。

* **资源隔离**

* **资源利用**：更高效

 

# 使用Kubernetes能做什么？

可以在物理或虚拟机的Kubernetes集群上运行容器化应用，Kubernetes能提供一个以**“容器为中心的基础架构”**，满足在生产环境中运行应用的一些常见需求，如：

* [多个进程（作为容器运行）协同工作](http://docs.kubernetes.org.cn/312.html)。（Pod）

* 存储系统挂载

* Distributing secrets

* 应用健康检测

* [应用实例的复制](http://docs.kubernetes.org.cn/314.html)

* Pod自动伸缩/扩展

* Naming and discovering

* 负载均衡

* 滚动更新

* 资源监控

* 日志访问

* 调试应用程序

* [提供认证和授权](http://docs.kubernetes.org.cn/51.html)

# 什么是Azure Kubernetes 服务 (AKS)

Azure Kubernetes 服务 (AKS) 管理托管的 Kubernetes 环境，使用户无需具备容器业务流程专业知识即可快速、轻松地部署和管理容器化的应用程序。 它还通过按需预配、升级和缩放资源，消除了正在进行的操作和维护的负担，而无需使应用程序脱机。

 

# 下一集：在 Azure Kubernetes 服务 (AKS)部署SQL Server 大数据群集

尽请期待！
