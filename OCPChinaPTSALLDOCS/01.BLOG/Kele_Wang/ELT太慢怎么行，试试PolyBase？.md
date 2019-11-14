传统的数仓项目，我们会用ETL把数据Extract Transform然后再Load到目标数据平台。

现在到了云和大数据时代，各种不同的数据分析需求太多，也没有任何单一的数据平台能够满足所有的要求，因此我们会有各式各样的数据平台来应对不同的需求。这个时候我们通常会倾向于采用ELT（Extract Load and Transform)，顾名思义，先把未处理的数据放在一个集中的数据湖(Data Lake或者对象存储Blob Storage)里面，需要处理的时候再去数据湖取数处理分析。那么这个时候数据的加载速度，就显得尤为重要。

对于MS SQL系的产品，我们有PolyBase，并行的加载能够大大提升数据的加载速度。比如我们这里有一个100G的CSV格式源文件存在Azure Blob Storage里，需要把它导入到SQL DW里面，使用起来也非常简单。只需要把Blob Storage里的源文件当成外表创建在SQL DW然后再通过CTAS导入进数据仓库。

接下来我们一步一步来看怎么这个过程如何实现。

1. 定义好Blob Storage的Credential，在下面的SQL里的Secret里面填上Storage的Key

```
/*
CREATE IDENTITY
*/
CREATE DATABASE SCOPED CREDENTIAL AzureStorageCredential
WITH
    IDENTITY = 'user',
    SECRET = '<填上您的Blob Storage的密钥>'
;
```


2. 定义Data Source，把Blob的URL填到下面SQL的Location。

```
/*
Create External Data Source
*/
CREATE EXTERNAL DATA SOURCE AzureStorage_DataSource
WITH 
(  
    TYPE = Hadoop 
,   LOCATION = 'wasbs://<Container>@<AccountName>.blob.core.chinacloudapi.cn'
,   CREDENTIAL = AzureStorageCredential
); 
GO
```


3. 定义文件格式，我们这里使用的是CSV文件，字段用逗号隔开

```
/*
Create External File FORMAT
*/
CREATE EXTERNAL FILE FORMAT csvdelimitedfile
WITH (FORMAT_TYPE = DELIMITEDTEXT,
      FORMAT_OPTIONS (FIELD_TERMINATOR = ','));
GO
```


4. 创建外表

```
/* 
Create External Table 
*/
DROP External TABLE [dbo].[DEAL_DETAILS_EXT];
CREATE External TABLE [dbo].[DEAL_DETAILS_EXT](
    [REGION] [nvarchar](50) ,
    .....
)
WITH (
    LOCATION='/DEAL/',   --文件地址
    DATA_SOURCE=AzureStorage_DataSource, 
    FILE_FORMAT=csvdelimitedfile
);
```


5. 建好外表之后，还需要使用CTAS(Create Table As Select)把数据导入SQL DW

```
CREATE TABLE [dbo].[DEAL_DETAILS]
WITH (
    DISTRIBUTION = ROUND_ROBIN
) 
AS SELECT * FROM [dbo].[DEAL_DETAILS_EXT]             
OPTION (
    LABEL = 'CTAS : Load [dbo].[DEAL_DETAILS]'
);
```

下图是用最基础的配置DWU400的SQL Data Warehouse加载完这100G的Raw Data，时间只要12分钟不到

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/ELT%E5%A4%AA%E6%85%A2%E6%80%8E%E4%B9%88%E8%A1%8C%EF%BC%8C%E8%AF%95%E8%AF%95PolyBase%EF%BC%9F01.webp)


