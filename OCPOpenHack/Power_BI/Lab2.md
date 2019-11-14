# 云端数据仓库及其数据展现


使用 Power BI 可以创建引人注目的视觉对象和报表。 本模块介绍如何讲云端数据仓库中的数据连接到 Power BI 中，并生成视觉对象。

## 在本模块中，将执行以下操作：

* 在 Azure中创建示例的SQL数据仓库服务 
* 将数据仓库中的数据通过 Power BI 进行展现和分析

## 先决条件
1. 对PowerBI的产品框架和定位有基本的认识，了解什么是 Power BI，其构建基块以及它们如何协同工作。如果对这些概念还不是很清楚，请先完成[热身课程](https://docs.microsoft.com/zh-cn/learn/modules/get-started-with-power-bi/index)。
2. [注册](https://signup.microsoft.com/signup?sku=a403ebcc-fae0-4ca2-8c8c-7a907fd6c235&email&ru=https%3A%2F%2Fapp.powerbi.com%3Fpbi_source%3Dweb%26redirectedFromSignup%3D1%26noSignUpCheck%3D1)或[登录](https://app.powerbi.com)PowerBI账户
3. [注册](https://azure.microsoft.com/zh-cn/free/)或[登录](portal.azure.com)微软云Azure账户 （Azure账号申请可以参考[这里](http://www.cnblogs.com/meowmeow/p/7773226.html?from=groupmessage&isappinstalled=0)）
   

## 动手实践

### 创建Azure SQL Data Warehouse
1. 登录Azure的[管理界面](portal.azure.com)
2. 新建一个数据仓库服务，选择“创建资源”，搜索“SQL Data Warehouse”，选择并创建
<img width="500" height="200" src="./Images/1-1.png"/>

3. 配置选项，选择从 Sample 创建数据库
<img width="400" height="450" src="./Images/1-2.png"/>
4. 创建，并等待部署完成。部署完成后，进入 SQL Data Warehouse Overview 界面，获取服务器名称，并复制。
<img width="450" height="450" src="./Images/1-3.png"/>

### PowerBI获取数据
1. 打开PowerBI Desktop，获取数据——选择Azure——选择Azure Data Warehouse。
<img width="500" height="300" src="./Images/2-1.png"/>
2. 填写刚刚复制的服务器名称，点击确定。
<img width="500" height="300" src="./Images/2-2.png"/>
3. 填写创建数据仓库时设置的用户名和密码，链接到数据库，并加载数据。 
如遇到IP访问限制而无法连接数据库，请回到Azure数据仓库管理界面，并配置防火墙。
<img width="400" height="300" src="./Images/2-3.png"/>
<img width="500" height="300" src="./Images/2-4.png"/>
4. 配置保存后，重新回到PowerBI连接数据仓库，并加载所需数据。
<img width="500" height="300" src="./Images/2-5.png"/>

### 在PowerBI中分析和展现数据
1. 等待数据加载，直到 Power BI Service 左侧 Data Set 中，出现与 SQL Data warehouse 数据库同名的数据集。
<img width="500" height="200" src="./Images/3-1.png"/>
2. 快速创建展现“收入与地区”关系图。点击右侧的 Aggregate Sales, 选择 PostalCode 和 SalesAmount，选择 Map Visual 并生成报表。 
<img width="500" height="300" src="./Images/3-2.png"/>
3. 点击报表空白处，创建收入历史变化关系图。
<img width="500" height="300" src="./Images/3-3.png"/>
4. 点击报表空白处，创建“Revenue 与 Customer Income”关系图。
<img width="500" height="300" src="./Images/3-4.png"/>
5. 如上述方法，继续丰富你的报表。








