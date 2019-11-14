# SQL Server 2019 新特性系列一：数据虚拟化

最新更新 SQL Server已经到了CTP2.2版本，主要更新了如下功能：

* 大数据集群：在大数据群集上使用 azure 数据工作室中的 sparkr

* 数据库引擎：在 sql server 复制中使用 utf-8 字符编码。

SQL Server 2019 CTP 2.0 开始的重要方案之一是能够虚拟化数据。 此过程允许将数据保留在其原始位置。 可以虚拟化 SQL Server 实例中的数据，以便可以对这些数据进行查询，如同 SQL Server 中的任何其他表一样。 此过程可以最大限度地减少对 ETL 进程的需求。 此过程可通过使用 PolyBase 连接器来实现。

借助 PolyBase，SQL Server 实例可处理从外部数据源中读取数据的 Transact-SQL 查询。 SQL Server 2016 及更高版本可以访问 Hadoop 和 Azure Blob 存储中的外部数据。 自 SQL Server 2019 CTP 2.0 起，现在可以使用 PolyBase 访问 SQL Server、Oracle、Teradata 和 MongoDB 中的外部数据。

访问外部数据的相同查询还可以定位 SQL Server 实例中的关系表。 这样可以将外部源中的数据与数据库中的高价值关系数据合并。 在 SQL Server 中，外部表或外部数据源提供对 Hadoop 的连接。

PolyBase 将一些计算推送到 Hadoop 节点，以优化总体查询。 不过，PolyBase 外部访问不仅限于 Hadoop。 其他未结构化的非关系表也受支持，如带分隔符的文本文件。

# 支持的 SQL 产品和服务

PolyBase 对以下 Microsoft SQL 产品提供这些相同功能：

* SQL Server 2016 及更高版本（仅限 Windows）

* 分析平台系统（旧称为“并行数据仓库”）

* Azure SQL 数据仓库

# Azure 集成

借助 PolyBase 的基础帮助，T-SQL 查询还可以将数据导入和导出 Azure Blob 存储。 此外，借助 PolyBase，Azure SQL 数据仓库还可以将数据导入和导出 Azure Data Lake Store 和 Azure Blob 存储。

# 为什么要用 PolyBase？

过去联接 SQL Server 数据与外部数据的难度更大。 具体有下列两种不方便的方法：

* 传输一半数据，这样所有数据都采用一种格式或其他格式。

* 查询两个数据源，然后编写自定义查询逻辑，以在客户端一级联接和集成数据。

PolyBase 使用 T-SQL 来联接数据，因此可避免使用这两种不方便的方法。
为了简单起见，PolyBase 不要求在 Hadoop 环境中安装其他软件。 查询外部数据所用的 T-SQL 语法也是用于查询数据库表的语法。 PolyBase 实现的所有支持操作全都以透明方式发生。 查询作者无需对 Hadoop 有任何了解。

# PolyBase 用法

PolyBase 支持在 SQL Server 中使用以下方案：

* 通过 SQL Server 或 PDW 查询 Hadoop 中存储的数据。 用户将数据存储在经济高效的分布式、可扩展系统中，例如 Hadoop。 PolyBase 使得使用 T-SQL 查询数据更加容易。

* 查询存储在 Azure Blob 存储中的数据。 Azure blob 存储是一个方便存储供 Azure 服务使用的数据的位置。 PolyBase 使得使用 T-SQL 访问数据变得更加容易。

* 导入 Hadoop、Azure Blob 存储或 Azure Data Lake Store 中的数据。 通过将 Hadoop、Azure Blob 存储或 Azure Data Lake Store 中的数据导入到关系表中，利用 Microsoft SQL 的列存储技术和分析功能的速度优势。 不需要单独的 ETL 或导入工具。

* 将数据导出到 Hadoop、Azure Blob 存储或 Azure Data Lake Store。 将数据存档到 Hadoop、Azure Blob 存储或 Azure Data Lake Store，以获得经济高效的存储，并使数据保持联机以便于访问。

* 与 BI 工具集成 结合使用 PolyBase 和 Microsoft 的商业智能和分析堆栈，或使用任何与 SQL Server 兼容的第三方工具。

# “性能”

* 将计算推送到 Hadoop。 查询优化器制定了基于成本的决策，以在执行此操作将提升查询性能时将计算推送到 Hadoop。 它使用外部表上的统计以制定基于开销的决策。 推送计算会创建 MapReduce 作业并利用 Hadoop 的分布计算资源。

* 缩放计算资源。 若要提高查询性能，可以使用 SQL Server PolyBase 横向扩展组。 这使并行数据可以在 SQL Server 实例和 Hadoop 节点之间传输，并为处理外部数据添加计算资源。

# PolyBase的安装

1、安装SQL Server 需要选择功能，针对外部数据的PloyBase查询服务。安装之前需要安装JAVA的运行环境，Oracle Java SE Runtime Environment (JRE)。 支持版本 7（从 7.51 开始）和版本 8。 [JRE](https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) 和 [Server JRE](https://www.oracle.com/technetwork/java/javase/downloads/server-jre8-downloads-2133154.html) 都可以正常工作。 转到 [Java SE](https://www.oracle.com/technetwork/java/javase/downloads/index.html) 下载。 如果 JRE 不存在，则安装程序失败。 不支持 JRE9 和 JRE10。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9601.png)

2、在服务器配置页上，将“SQL Server PolyBase 引擎服务”和“SQL Server PolyBase 数据移动服务”配置为在同一域帐户下运行。

3、在“PolyBase 配置页”上，选择两个选项之一。 有关详细信息，请参阅 [PolyBase 横向扩展组](https://docs.microsoft.com/zh-cn/sql/relational-databases/polybase/polybase-scale-out-groups?view=sqlallproducts-allversions)。 

* 将 SQL Server 实例用作已启用 PolyBase 的独立实例。  选择此选项可将 SQL Server 实例用作独立的头节点。 

* 将 SQL Server 实例作为 PolyBase 横向扩展组的一部分使用。 此选项将打开防火墙以允许传入连接。 允许与 SQL Server 数据库引擎、SQL Server PolyBase 引擎、SQL Server PolyBase 数据移动服务和 SQL Browser 建立连接。 防火墙还允许来自 PolyBase 横向扩展组中其他节点的传入连接。 

此选项还将启用 Microsoft 分布式事务处理协调器 (MSDTC) 防火墙连接并修改 MSDTC 注册表设置。 

4、在 PolyBase 配置页上，指定具有至少六个端口的端口范围。 SQL Server 安装程序分配该范围中的前六个可用端口。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9602.png)

启用 PolyBase

安装完成后，必须启用 PolyBase 来获取其功能。 若要连接到 SQL Server 2019 CTP 2.0，必须在安装后启用 PolyBase。 使用以下 Transact-SQL 命令。

```
---启用PolyBase
exec sp_configure @configname = 'polybase enabled', @configvalue = 1;
RECONFIGURE ;
```

```
--检查PolyBase是否安装
SELECT SERVERPROPERTY ('IsPolyBaseInstalled') AS IsPolyBaseInstalled;  
```
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9603.png)

# PloyBase使用

PloyBase 可以连接 Azure Blob、SQL Server、Oracle、TeraData、MongoDB等，也看支持ODBC 泛型类型。

# 连接SQL Server

下面测试连接SQL  Server ,使用Azure Data Studio创建外部表，在Azure Data Studio，点击Extensions（Ctrl+Shift+X）搜索SQL 2019,下载sql-vnext-0.8.0-win-x64.vsix

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9604.png)

点击文件，选择Install Extension From VSIX Package，选择到 sql-vnext-0.8.0-win-x64.vsix ，安装 SQL Server 2019 preview组件 

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9605.png)

安装成功后，重新引导，点击数据库右键可以看到 create external table的选项。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9606.png)

默认选择data source 为sql server

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9608.png)

创建主秘钥

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9609.png)

输入需要链接的服务器和创建的认证信息。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9610.png)

选择需要创建的数据源信息

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9611.png)

相关信息，点击创建既可以创建完成。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9612.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9613.png)

原始数据表

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9614.png)

外部表信息

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9616.png)

**可以看到可以使用外部表实现数据并不在本数据库，通过polybase实现同样的查询和使用**

# 连接Azure Blob

由于上面的向导只能使用SQL  Server 和Oracle 作为数据源，使用Azure Blob需要使用代码来完成。

在Azure Blob上放了一个测试数据

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9617.png)

数据类似这样的数据，**特别提示 文件存放格式要用utf-8格式**

```
1,非忠诚,在线,配件,装饰,0,0,0,0,0,0,0,0
2,非忠诚,在线,配件,装饰,0,0,0,0,0,0,0,0
3,非忠诚,在线,配件,装饰,0,0,0,0,0,0,0,0
4,非忠诚,在线,配件,装饰,0,0,0,0,0,0,0,0
5,非忠诚,在线,配件,装饰,96628.8,0,107142.01,4920,3092.12,93536.68,28061,0
6,非忠诚,在线,配件,装饰,0,0,0,0,0,0,0,0
7,非忠诚,在线,配件,装饰,0,0,0,0,0,0,0,0
8,非忠诚,在线,烤盘,餐饮与娱乐,0,0,0,0,0,0,0,0
9,非忠诚,在线,烤盘,餐饮与娱乐,0,196.4,0,-10,0,0,0,-1
10,非忠诚,在线,烤盘,餐饮与娱乐,0,392.8,0,-20,0,0,0,-1
```

```
--1、运行 sp_configure，将“hadoop 连接”设置为 Azure Blob 存储提供程序。 若要查找提供程序的值，请参阅 PolyBase 连接配置。 默认情况下，Hadoop 连接设置为 7。
sp_configure @configname = 'hadoop connectivity', @configvalue = 7;
GO
RECONFIGURE
GO

--2、在数据库上创建主密钥。上面已经创建了，这步在这里不需要完成。如果是新数据库需要创建
SQL
 
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'S0me!nfo';  
--3、为 Azure Blob 存储创建数据库范围的凭据。

-- IDENTITY: any string (this is not used for authentication to Azure storage).  
-- SECRET: your Azure storage account key.  
CREATE DATABASE SCOPED CREDENTIAL AzureStorageCredential
WITH IDENTITY = 'user', Secret = '<azure_storage_account_key>';
--4、使用 CREATE EXTERNAL DATA SOURCE 创建外部数据源。
-- LOCATION:  Azure account storage account name and blob container name.  
-- CREDENTIAL: The database scoped credential created above.  
CREATE EXTERNAL DATA SOURCE AzureStorage with (  
      TYPE = HADOOP,
      LOCATION ='wasbs://demo1@testsqlex.blob.core.windows.net',  
      CREDENTIAL = AzureStorageCredential  
);  
--5、使用 CREATE EXTERNAL FILE FORMAT 创建外部文件格式。

-- FORMAT TYPE: Type of format in Hadoop (DELIMITEDTEXT,  RCFILE, ORC, PARQUET).
CREATE EXTERNAL FILE FORMAT TextFileFormat WITH (  
      FORMAT_TYPE = DELIMITEDTEXT,
      FORMAT_OPTIONS (FIELD_TERMINATOR =',',
            USE_TYPE_DEFAULT = TRUE))  
--6、使用 CREATE EXTERNAL TABLE 创建指向 Azure 存储中存储的数据的外部表。 
-- LOCATION: path to file or directory that contains the data (relative to HDFS root).  
  
CREATE EXTERNAL TABLE [dbo].[demo_Data] (
      [序号] int ,
      [客户细分市场] varchar(20),
      [通道] varchar(20),
      [产品] varchar(20),
      [产品类别] varchar(20),
      [销售总额] float,
      [预算] float,
      [预测] float,
      [毛利润] float,
      [折扣] float,
      [销售额] float,
      [利润] float,
      [预测差额比] float
)  
WITH (LOCATION='/测试数据.csv',
      DATA_SOURCE = AzureStorage,  
      FILE_FORMAT = TextFileFormat  
);  


--7、创建统计信息，实际测试，创建统计信息和不创建统计信息的速度差别很大。
CREATE STATISTICS StatsForSensors on demo_Data([序号])  
```




完成后，创建成功的表和执行 select语句的结果。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BA%91%E4%B8%96%E7%95%8C%EF%BC%8C%E4%B8%80%E5%88%87%E5%A6%82%E6%A2%A6%E5%B9%BB%EF%BC%8C%E6%95%B0%E6%8D%AE%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E5%8C%96%E3%80%82%20SQL%20Server%202019%20%E6%96%B0%E7%89%B9%E6%80%A7%E7%B3%BB%E5%88%97%E4%B8%80%EF%BC%9A%E6%95%B0%E6%8D%AE%E8%99%9A%E6%8B%9F%E5%8C%9618.png)

本文测试了2种数据源，其他数据源也用类似的方法进行连接查询。

**综上， 使用PloyBase实现了数据存放在自己的环境中，需要查询的时候进行查询，这样的可以减少ETL的工作，SQL Server 2019 中大大的加强了PloyBase 的能力，可以对更多的数据源（ Azure Blob、SQL Server、Oracle、TeraData、MongoDB）进行查询，并且此能力也可以在 Azure DW 上使用**
