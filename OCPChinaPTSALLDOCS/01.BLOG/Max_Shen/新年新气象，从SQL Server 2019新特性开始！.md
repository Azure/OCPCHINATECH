# SQL Server 2019新特性开篇概述

2019年了，新年伊始，SQL Server 2019已经到CTP 2.1 ，一直没有认真的学习SQL Server 2019 ，既然是新年新气象，就从新的SQL Server 2019开始，完成一系列的SQL Server 2019的学习。

SQL Server 2019在新的功能上可以看到有几个重大方向的内容。

* 大数据群集

* 数据库引擎更多功能

* 新的工具Azure Data Studio

# 大数据群集

* SQL Server 2019 预览 [大数据群集](https://docs.microsoft.com/zh-cn/sql/big-data-cluster/big-data-cluster-overview?view=sql-server-ver15)支持新方案，包括以下内容：

* [部署 Python 和 R 应用](https://docs.microsoft.com/zh-cn/sql/big-data-cluster/big-data-cluster-create-apps?view=sql-server-ver15)。 (CTP 2.1)

* 在 Kubernetes 上部署带 SQL Server 和 Spark Linux 容器的大数据群集 (CTP 2.0)

* 从 HDFS 访问大数据 (CTP 2.0)

* 使用 Spark 运行高级分析和机器学习 (CTP 2.0)

* 使用 Spark 将数据流式传输到 SQL 数据池 (CTP 2.0)

* 在 [Azure Data Studio](https://docs.microsoft.com/zh-cn/sql/azure-data-studio/what-is?view=sql-server-ver15) 中运行提供 notebook 体验的查询书籍。 (CTP 2.0)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%96%B0%E5%B9%B4%E6%96%B0%E6%B0%94%E8%B1%A1%EF%BC%8C%E4%BB%8ESQL%20Server%202019%E6%96%B0%E7%89%B9%E6%80%A7%E5%BC%80%E5%A7%8B%EF%BC%8101.png)

大数据群集主要有几个重要的特性：

* 数据虚拟化

* 数据湖

* 集成AI和机器学习

* 利用新工具 Azure Data Studio 实现良好的管理和监视

# 数据库引擎更多功能

数据库引擎上有更多的功能提供如：

* 智能查询处理添加标量 UDF 内联

* 截断错误消息已改进，包括表名和列名以及截断值

* SQL Server 安装中支持 UTF-8 排序规则

* 在图形匹配查询中使用派生表或视图别名

* 改进了用于统计信息阻塞的诊断数据

* 混合缓冲池

* 静态数据掩码

* UTF-8 支持

* 可恢复联机索引创建允许索引创建，以在发生中断后恢复

* 聚集列存储联机索引生成和重新生成

* 具有安全 Enclave 的 Always Encrypted

* 智能查询处理

* Java 语言可编程性扩展

* SQL 图形功能

* 针对联机和可恢复 DDL 操作的数据库范围的配置设置

* AlwaysOn 可用性组 - 辅助副本连接重定向

* 数据发现和分类 - 本机内置于 SQL Server

* 对永久性内存设备的扩展支持

* 支持 DBCC CLONEDATABASE 中的列存储统计信息

* 向 sp_estimate_data_compression_savings 添加的新选项

* SQL Server 机器学习服务故障转移群集

* 默认情况下启用轻量查询分析基础结构

* 新 PolyBase 连接器

* 新 sys.dm_db_page_info 系统函数返回页面信息

# [Linux 上的 SQL Server](https://docs.microsoft.com/zh-cn/sql/sql-server/what-s-new-in-sql-server-ver15?view=sql-server-ver15#sqllinux)

Linux SQL Server也带了更多的新的功能

* 复制支持

* 支持 Microsoft 分布式事务处理协调器 (MSDTC)

* Docker 容器上使用 Kubernetes 的 AlwaysOn 可用性组

* OpenLDAP 支持第三方 AD 提供商

* Linux 上的机器学习

* 新建容器注册表

* 新的基于 RHEL 的容器映像

* 内存压力通知

# 新的工具Azure Data Studio
Azure Data Studio是新工具，之前的名字叫做 SQL Operation Studio 。未来实现所有的数据管理，跨平台的使用。链接不同的数据源，之前我的blog已经有相关介绍，下面链接是官方介绍

https://docs.microsoft.com/zh-cn/sql/azure-data-studio/download?view=sql-server-2017

**SQL Server 2019 会变得无比强大，而且更加易于，好玩，本篇只是一个序，开启SQL Server 2019之旅，更多内容敬请期待！**
