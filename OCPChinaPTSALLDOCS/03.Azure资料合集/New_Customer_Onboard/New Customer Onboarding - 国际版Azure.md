## 新客户 Onboard 需要了解的 Azure 基础概念及最佳实践

---
本白皮书面向的群体，是刚刚接触云服务知识或者刚刚购买Azure准备使用的客户。第一章主要介绍Azure的各种体系，各种门户使用方法，以及资源确认和支持情况。第二章包含各种动手实践，旨在熟悉Portal和资源的情况。第三章是各种常用链接。请各位按需读取。

## 1. Azure资源管理

### 1.1. 购买的账号对应的账号体系

#### 1.1.1. Azure Mooncake(Azure中国区)购买账号及对应的账号体系

在中国，可通过两种方式采购由世纪互联运营的 Microsoft Azure 服务：在线服务标准协议（Online Service Standard Agreement，OSSA），以及在线服务高级协议（Online Service Premium Agreement，OSPA）。

- OSSA 是一种可供客户直接在线购买的在线签约过程。
- OSPA 主要适用于可做出最低货币承诺的大型企业客户。OSPA主要适用于企业型客户通过线下合同方式完成。

**在线服务标准协议（OSSA）**

任何希望通过 Azure.cn 在线购买 Azure 的客户均可选择 OSSA 方式。这是一种预付费模式，对购买金额有最低要求。目前 OSSA 提供两种类型的服务：

- 1 元人民币试用：新用户可支付 1 元人民币，获得有效期 1 个月，价值人民币 1,500 元的 Azure 额度。在到期删除前，这种订阅可随时升级为预付费（PIA）订阅。
- 预付费：用户也可直接购买预付费订阅。所购买 Azure 额度等同于预先支付的金额，每次购买所获得额度有效期 12 个月。

按照法律规定，OSSA 客户需通过实名身份认证。因此用户必须预先准备好自己的身份证号码和复印件，企业客户需提供注册营业执照编号和营业执照复印件。在注册 Azure 帐户过程中还需具备中国的移动电话号码。

OSSA实际对应于Web Direct。

**在线服务高级协议（OSPA）**

OSPA 适用于需要签署三年期合约，具备最低年度额度承诺，通过合约流程购买 Azure 的企业客户。OSPA 协议需要由世纪互联和企业客户共同签署。OSPA 支持两种业务模式：Direct OSPA（直接 OSPA）和 Indirect OSPA（间接 OSPA）。

- Direct OSPA 由世纪互联与客户直接签约，客户直接向世纪互联付款。

- Indirect OSPA 是指企业通过能满足自己需求的合作伙伴购买 Azure 在线服务高级协议这种协议需要由世纪互联、微软 Indirect 合作伙伴，以及中国的企业客户三方共同签署。Indirect OSPA 的条款与 OSPA 一致，通常是一种三年期承诺，费用按年支付。Indirect OSPA 合作伙伴可为客户的购买提供多种帮助，如售前咨询、根据采购方案提供报价，并可能将合作伙伴的解决方案与 Microsoft Azure 集成，计费和发票等支持。

OSPA则对应于Azure EA账号。

#### 1.1.2. Azure Global购买账号及对应的账号体系

目前 Azure 全球服务的购买渠道有以下三种（本指南将详细介绍线上购买和企业合同两种购买渠道）：

- 线上购买：通过 Azure 官网在线购买 Azure 服务
- 企业合同：与微软代表签订企业合同购买 Azure 服务
- 通过合作伙伴购买：通过微软云解决方案合作伙伴购买 Azure 服务与购买渠道相对应的 Azure 

全球服务付费方式目前有以下三种：
1. 即用即付（Pay-As-You-Go, PAYG）:客户按照实际使用量付款。没有最低使用数量限制或预付款。特点是客户在 Azure 网站上可以灵活地开始或终止服务。
  - 此付费方式适用于线上购买 Azure 服务和 Azure 市场中的服务的客户
  - 此付费方式适用于签订企业合同客户的超额使用部分
2.	金额承诺（Monetary Commitment, MC）: 客户在签署企业协议后, 需要提前预付他们承诺的 Azure 服务购买金额，然后自行分配资金使用。此付费方式仅适用于签订企业合同和通过合作伙伴购买 Azure 服务的客户。

3.	Azure 计划（Azure Plans: prepay for committed services）：在成为 Azure 服务的付费用户后，客户可以额外购买特定的服务或者服务组，称为 Azure 计划。 Azure 计划包括一些非消费性产品，比如 Azure 客户支持服务，以及一些提前预配置好的服务，比如 Azure Active Directory 服务。 此外还有 OMS，EMS，IoT 套件等服务都属于 Azure 计划之列。
  - 线上购买 Azure 服务的用户可以额外购买 Azure 计划中的 Azure 客户支持服务
  - 签订企业合同和通过合作伙伴购买 Azure 服务的客户可购买任意 Azure 计划

#### 1.1.3. 平滑迁移资源
如果已经测试或者部分使用了Azure资源后，需要进行资源迁移，那么怎么样进行平滑的迁移也是一个很重要的问题。通过使用 Azure 门户、Azure PowerShell、Azure CLI 或 REST API可以将 Azure 资源移动到另一 Azure 订阅，或移动到同一订阅下的另一资源组。

在移动操作过程中，源组和目标组都会锁定。 在完成移动之前，将阻止对资源组执行写入和删除操作。此锁意味着无法添加、更新或删除资源组中的资源。 这并不意味着资源已冻结。例如，如果将 SQL Server 及其数据库移动到新的资源组中，则使用该数据库的应用程序将不会遇到停机的情况。 它仍可读取和写入到数据库。锁定时间最长可达四小时，但大多数移动完成的时间将少得多。移动资源仅能够将其移动到新的资源组或订阅中。但不会更改该资源的位置。

对于跨订阅移动，资源及其从属资源必须位于同一资源组中，并且必须一起移动。 例如，具有托管磁盘的 VM 需要将 VM 和托管磁盘与其他依赖资源一起移动。

将资源从一个订阅移到另一个订阅的过程分为下图三个步骤，出于说明目的，图中只有一个从属资源。

 - 步骤1：如果从属资源分布在不同的资源组中，请先将它们移到一个资源组中。
 - 步骤2：将资源和相关资源与源订阅一起移动到目标订阅。
 - 步骤3：（可选）将从属资源重新分发给目标订阅中的不同资源组。
 ![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding1.png?raw=true)
 

如果要将资源移到新订阅，请检查该资源是否有任何依赖资源，以及这些资源是否位于同一资源组中。 如果资源不在同一资源组中，请检查资源是否可以合并到同一个资源组中。如果是这样，请使用跨资源组的移动操作将所有这些资源置于同一资源组中。

有关详细信息，请参阅[跨订阅移动方案](https://docs.microsoft.com/zh-cn/azure/azure-resource-manager/management/move-resource-group-and-subscription#scenario-for-move-across-subscriptions)。

对于资源是否支持迁移，请参阅[支持移动的资源](https://docs.microsoft.com/zh-cn/azure/azure-resource-manager/management/move-support-resources)，里面列出了 Azure 资源类型是否支持移动操作。 它还提供有关移动资源时要考虑的特殊情况的信息。

当订阅迁移发生问题时，请参阅[常见问题](https://docs.microsoft.com/zh-cn/azure/azure-resource-manager/management/move-resource-group-and-subscription)，对于资源迁移时间长、在资源移动过程中，源和目标资源组的锁定有哪些、错误代码 "MissingMoveDependentResources" 的含义是什么等，都进行了解答。

---

### 1.2. 管理及使用Azure资源过程中涉及到的两个重要的访问地址
#### 1.2.1. EA Portal 及其作用 
- Azure Mooncake : https://ea.azure.cn
- Global Azure : https://ea.azure.com

Azure EA （Azure Enterprise Agreement）门户是一个在线管理门户，可帮助客户管理其 Azure EA 服务的结构和成本。 使用该门户可以创建 Azure EA 层次结构，包括部门、帐户和订阅。 使用它还可以核对所用服务的成本、下载使用情况报告，以及查看价目表。

#### 1.2.2.	Azure Portal 及其作用
- Azure Mooncake : https://portal.azure.cn
- Global Azure : https://portal.azure.com

Azure门户是基于Web的统一控制台，它提供了命令行工具的替代方法。借助Azure门户，用户可以使用图形用户界面管理Azure订阅。用户可以构建，管理和监视简单的从Web应用程序到复杂的云部署的所有内容。创建自定义仪表板，以获得组织化的资源视图。配置可访问性选项以获得最佳体验。

Azure门户旨在实现弹性和持续可用性。它存在于每个Azure数据中心中。此配置使Azure门户能够抵御单个数据中心的故障，并通过靠近用户来避免网络运行缓慢。Azure门户不断更新，无需停机即可进行维护活动。

---

### 1.3. Azure EA 管理 
Azure EA 门户是一个在线管理门户，可帮助你管理 Azure EA 服务的成本。 使用该门户可以创建 Azure EA 层次结构，包括部门、帐户和订阅。

使用它还可以核对所用服务的成本、下载使用情况报告，以及查看价目表。

#### 1.3.1.	EA 层次结构及角色
Azure EA 门户的层次结构包括：

**部门** - 创建部门有助于将成本细分为逻辑分组，然后在部门级别设置预算或配额。

**帐户** – 帐户是 Azure EA 门户中用于管理订阅的一个组织单位。 帐户也用于报告。

**订阅** – 订阅是 Azure EA 门户中的最小单位。 它们是服务管理员管理的 Azure 服务的容器。

下图演示了简单的 Azure EA 层次结构。

![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding2.png?raw=true)

由图片可以看到，根据职能、商业角度和地理位置等，可以针对一个企业结构进行不同的部门划分，不同的部门由不同的负责人进行管理，而针对更细化的项目或者应用需求，还可以划分出不同的订阅，进行更细化的管控。

若要在注册中管理 Azure服务，EA账户体系提供五个不同的企业管理用户角色来帮助用户进行管理：

**企业管理员**

企业管理员角色拥有最高级别的访问权限。 具有该角色的用户可以：

- 管理帐户和帐户所有者
- 管理其他企业管理员
- 管理部门管理员
- 管理通知联系人
- 查看所有帐户的使用情况
- 查看所有帐户的未开单费用

可以在一个企业注册中分配多个企业管理员。可以向企业管理员授予只读访问权限。这些管理员全部继承部门管理员角色。

**部门管理员**

具有该角色的用户可以：

- 创建和管理部门
- 创建新的帐户所有者
- 查看他们所管理的部门的使用情况详细信息
- 查看成本（如果已获取所需权限）

可为每个企业注册分配多个部门管理员。可向部门管理员授予只读访问权限。若要授予只读访问权限，请编辑或新建部门管理员，并将只读选项设置为“是”。

**帐户所有者**

具有该角色的用户可以：

- 创建和管理订阅
- 管理服务管理员
- 查看订阅的使用情况

每个帐户需要唯一的工作、学校或 Microsoft 帐户。

**服务管理员**

服务管理员有权在 Azure 门户中管理服务，以及将用户分配到共同管理员角色。

- 通知联系人

通知联系人接收与注册相关的使用通知。

上述五个角色用于在两个不同的 Microsoft Azure 门户中完成任务。 Azure EA门户用于帮助管理计费和成本。 Azure 门户用于管理 Azure 服务。为了验证用户真实性，每个用户必须具有有效的工作、学校或 Microsoft 帐户。

怎样构建合理的EA体系结构，利用各种角色进行细化的资源管理，怎样激活EA账号并添加订阅等操作可以参见附件，或者参考[EA门户入门](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/ea-portal-get-started)。

#### 1.3.2.	EA账单解读
企业管理员可以在 Azure EA 门户中查看其使用情况数据、货币承诺消耗量，以及与其他用途相关的费用的摘要。费用以摘要形式显示，适用于所有帐户和订阅。

**查看使用情况摘要报表步骤和示图**

1.	在 Azure EA 门户的左侧导航区域中，单击“报告”并查看“使用情况摘要”选项卡。
2.	选择承诺条款。
3.	在页面右上角的“M”（每月）和“C”（自定义）之间切换可以根据自定义的开始日期和结束日期查看“使用情况摘要”。
4.	在图表上选择某个时段或月份可以查看更多详细信息。
5.	图表显示了每月的使用情况，其中细分了使用量、服务额外费用、单独计收的费用和市场费用。
6.	对于选定的月份，可在图表下方按部门、帐户和订阅进行筛选。
7.	在“按服务列出的费用”与“按层次结构列出的费用”之间切换。
8.	展开和折叠“Azure 服务”、“单独计收的费用”和“Azure 市场”可查看详细信息。

![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding3.png?raw=true)

**下载 CSV 报告**

企业管理员可以使用“月份报告下载”页将多份报告下载为 CSV 文件。 其中包括：
- 余额和费用
- 使用情况详细信息
- 市场费用
- 价目表

若要下载报告：
- 在 Azure EA 门户中单击“报告”。
- 单击页面顶部的“下载使用情况”。
- 选择月份报告旁边的“下载”。

从使用日期开始算起，最长可能需要延迟五天，其费用才会显示在报告中。

CSV报告中包含有大量的字段信息，下面是每个字段代表的含义：

中文字段名 | 英文字段名 | 说明 | 是否常用
:---|:--- | :---|:---
账户所有者 | AccountOwnerId | 表示该订阅创建的账户id | -
账户名称 | Account Name | 账户名称 | -
服务管理员 | Live Id |Service Administrator Id|-	 	
订阅ID|SubscriptionId| |	- 	
订阅GUID|	SubscriptionGuid|	表示订阅的GUID	| - 
订阅名称|	AccountOwnerId|	表示订阅的显示名称|	是
日期|	Date|	表示该计费资源的计费时间，比如2019-06-01	|是
月	|Month|	表示该计费资源，所属的月份，比如6|	是
日|	Day	|表示该计费资源，所属的日期，比如1	|是
年|	Year|	表示该计费资源，所属的日期，比如2019|	是
产品|	Product|	计费单元所属的产品|	
资源GUID|	Meter ID	|资源的GUID |-	
服务|	Meter Category |	服务的一级分类	|-
服务类型|	Meter Sub-Category| 	服务的 二级分类	|-
服务区域|	Meter Region |	服务所在的区域	|-
服务资源|	Meter Name |	服务资源	|-
已消耗的资源数量|	Consumed Quantity |	计费的资源数量,比如虚拟机计算资源，是按照小时来收费的。如果虚拟机开了24小时，则该列会显示24。对于存储来说，是按照GB来收费的。如果存储用了1GB，则改了会显示1。计费数量的单位，请参考列：Unit of Measure |	是
资源费率|	Resource Rate |	计费单价，比如虚拟机计算资源，是按照小时来收费的。该列会显示虚拟机每小时费用的单价。对于存储来说，是按照GB来收费的。该列会显示每GB每月费用单价|	是
扩展的成本|	ExtendCost |	等于，列：已消耗的资源数量 (乘以) 列：资源费率是单个计费资源产生的费用|	是
服务子区域|	Resource Location 	|不经常使用 |-	
服务信息|	Consumed Service |	不经常使用  |-	
组件|	Instance ID|	资源的唯一ID，对于ARM资源来说，组件展现的形式如下：/subscriptions/{订阅ID}/resourceGroups/{资源组名称}/providers/Microsoft.Compute/virtualMachines/{虚拟机名称}	|-
服务信息1 |	ServiceInfo1|	不经常使用 	|-
服务信息2|	ServiceInfo2 |	不经常使用 	|-
附加信息|	AdditionalInfo 	|不经常使用 	|-
Tags|	Tag	|资源的标签TAG |	是
Store Service Identifier	| | 不经常使用 	|-
Department||资源所属的部门，部门只在EA Portal里面定义|	是
Cost Center	 ||	资源所属的Cost Center成本中心 ，成本中心只在EA Portal里面定义	|是
Unit of Measure	 ||	列：已消耗的资源数量的单位，比如虚拟机计算资源，是按照小时来收费的，则该列显示为Hour。对于存储来说，是按照GB来收费的。则该列会显示GB|	是
资源组|Resource Group|	资源所属的资源组名称|	是

下面以Azure Mooncake出发，实际看一下EA CSV报告解读。

Azure可以通过下载Excel表格，将一段时间内Azure的详细账单，通过CSV文件格式进行下载，然后用户可以通过透视表的方式进行自定义查询。

1.	点击报表，下载使用量。
![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding4.png?raw=true)
2.	点击上图的按钮，就可以下载使用量的详细数据。如果未显示下载按钮，则点击下图的“刷新”按钮
![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding5.png?raw=true)
3.	下载完毕后，打开下载的CSV文件。

如果想查看每个订阅每个月产生的费用情况，用户需要关心的列有：
- 订阅名称
- 年
- 月
- 扩展的成本 
    
如果想查看每个资源组每天产生的费用情况，需要关心的列有：
+ 年
+ 月
+ 日
+ 扩展的成本
+ Resource Group

用户还可以通过编辑数据透视表，来对CSV文件进行统计。打开CSV文件，全选第3行的列明，然后按CTRL + SHIFT + END，选中所有的表格内容。然后点击，插入，数据透视表。如下图：

![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding6.png?raw=true)

在透视表中，拖动资源。
![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding7.png?raw=true)
即可以得到分析示图：
![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding8.png?raw=true)

---

### 1.4. Azure资源的订阅限制及配额、价格查询
#### 1.4.1.	订阅限制及配额
针对每个订阅，Azure中所提供的资源默认是有Quota限制的，此限制可根据实际需要，通过提交工单的方式调整，请根据实际需要，提前预估并做好相应的准备。

- Azure Mooncake 订阅限制及配额：https://docs.azure.cn/zh-cn/azure-subscription-service-limits
  >如：在Azure Mooncake，每个订阅的 vCPU 数量的默认限制是20个，经过调整后，最大可以提升到10,000个。
- Global Azure 订阅限制及配额：https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits
 > 如：每个订阅在每个区域中的存储帐户数，默认和最大都是250个。

#### 1.4.2.	Azure 资源价格
Azure 资源的价格相对透明，查询Azure资源的价格及其计费方式，可参见如下，可以查询到资源的价格，与本地服务的价格对比，或者是Support计划的价格等等。
- Azure Mooncake ：https://www.azure.cn/pricing/
- Global Azure ：https://azure.microsoft.com/en-us/pricing/

---

### 1.5.	Azure资源优惠信息 
#### 1.5.1.	Azure Mooncake
企业客户可以通过购买包年虚机（CPP），获得优惠的价格，实现更高的性价比，具体CPP的介绍请参见：https://docs.azure.cn/zh-cn/enterprise-agreement-billing/enterprise-agreement-billing-check-cpp，关于CPP的购买及价格，请咨询销售。

#### 1.5.2.	Global Azure
企业客户可以通过购买 RI （保留实例），获得资源更为优惠的价格，实现更高的性价比。Azure 预留承诺预付适用于虚拟机、Azure Blob 存储或 Azure Data Lake Storage Gen2、SQL 数据库计算容量、Azure Cosmos DB 吞吐量或其他 Azure 资源的一年或三年计划，为用户节省资金。 通过承诺预付，能够以折扣价购买所用资源。 预留可显著将资源的成本，最多减少至即用即付价格的 72%。 预订提供计费折扣，并且不会影响资源的运行时状态。

如果使用大容量/高吞吐量或者长时间运行的虚拟机、Blob 存储数据、Azure Cosmos DB 或 SQL 数据库，那么购买预留项可以获得最实惠价格。 例如，如果持续运行四个服务实例，在不购买预留项的情况下，需按即用即付价格付费。 如果购买这些资源的预留项，则将立即获得预留折扣。 这些资源不再按即用即付费率收费。

预留项涵盖的计划：
- 虚拟机预留实例 - 预留项仅涵盖虚拟机计算成本。 而不涵盖软件、网络或存储等其他费用。
- Azure 存储预留容量 - 该预留项涵盖用于 Blob 存储或 Azure Data Lake Gen2 存储的标准存储帐户的存储容量。 不涵盖带宽或事务费率。
- Azure Cosmos DB 预留容量 - 预留项涵盖为资源预配的吞吐量的费用。 但它不涵盖存储和网络费用。
- SQL 数据库预留 vCore - 预留项仅包含计算成本。 许可证单独计费。
- SQL 数据仓库 - 预留项涵盖 cDWU 用量。 它不涵盖与 SQL 数据仓库用量相关的存储或网络费用。
- 应用服务印花费 - 预留项涵盖印花使用费。 它不适用于辅助角色，因此与印花相关的任何其他资源将单独收费。
- Azure Database for MySQL
- Azure Database for PostgreSQL
- Azure Database for MariaDB
- Azure 数据资源管理器
- 高级 SSD 托管磁盘

具体支持保留实例购买的资源请参见[Azure预留实例](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/reservations/save-compute-costs-reservations#charges-covered-by-reservation) 。

保留实例的购买，退改等操作均通过Azure Portal自助完成，具体信息可参见：https://docs.microsoft.com/zh-cn/azure/cost-management-billing/reservations/manage-reserved-vm-instance

关于保留实例的匹配策略，请参见各资源对应说明文档，如下为虚拟机部分的说明：https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/understand-vm-reservation-charges

---

### 1.6. Azure资源可用性确认 
在部署前，检查资源的可用性是至关重要的，它关系着项目的顺利进行。比如：检查sku 是否支持某个region或者az区域，可以通过一下几种方式进行查询：
- 产品对地区的支持性: https://azure.microsoft.com/en-us/global-infrastructure/services/?products=virtual-machines&regions=europe-west
- 利用az命令查询某个sku支持的az，例如，查询虚机在西欧az的支持性：
  > az vm list-skus -l westeurope --all --zone -o table
- 利用powershell命令查询某个sku支持的az ，同样查询虚机在西欧az的支持性：
  > Get-AzComputeResourceSku | where {$_.Locations.Contains("westeurope")}

在迁移开始之前，需要为为后续迁移做好准备。 这个阶段主要在以下两个方面完成：组织就绪情况和环境（技术）就绪情况。 每个方面都可能需要技术参与者和非技术参与者掌握新技能。 这个阶段，可以参考[技能就绪](https://docs.microsoft.com/zh-cn/azure/cloud-adoption-framework/ready/suggested-skills)，包括技术学习路径和资源管理相应知识。

---

### 1.7.	Azure Support Plan & Support 模式 
#### 1.7.1.	Azure Mooncake Support 模式
![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding9.png?raw=true) 
技术case：
1.	客户通过在线网站或者支持热线提交问题，case 随即生成并会被自动分派到对应 的技术支持 POD。 
2.	由微软 CSS （微软全球技术支持中心）和 21V 的工程师共同组成 POD 支持团队，其中，21V 工程师将作为客 户联系的唯一接口；CSS 的 Technical Advisor (TA) 和 Support Escalation Engineer (SEE) 负责后端技术升级支持。 
3.	经由客户的许可，21V 可以引入微软 CSS 与客户进行三方沟通，形式可以是邮件、 电话或者远程协助。 
4.	如确定为产品导致的影响客户生产环境的紧急问题，21V 工程师或者微软 CSS 将给 21V WASU 提交紧急程度为 2 的内部工单，使其安排微软后端产品开发团队进行平 台排查。 
5.	如问题需要产品团队协助排查，但问题本身并不紧急或者已有 workaround，微软 CSS 将向后端产品开发团队提交紧急程度为 3 的内部工单。
6.	微软 CSS 将提供原厂技术支持服务，包括问题排查和咨询，TAM 也将全程参与。
商务case：
支持全过程适用于所有类别客户，如上面图中下方流程所示。

#### 1.7.2.	Global Azure Support Plan标准及定价


基本 | 开发人员 | 标准 |专业直接支持|	顶级支持
---|---|---|---|---
技术支持|	|	在营业时间1通过电子邮件联系支持工程师	|全天候通过电子邮件和电话访问支持工程师	|全天候通过电子邮件和电话访问支持工程师	|全天候通过电子邮件和电话访问支持工程师
谁能解决案例|	|	无限制的沟通次数/无限制的案例|	无限制的沟通次数/无限制的案例|	无限制的沟通次数/无限制的案例	|无限制的沟通次数/无限制的案例
案例严重性/响应时间| |	最低业务影响 (Sev C)：<8 营业时间	最低业务影响 (Sev C):<8 营业时间<br>中等业务影响 (Sev B):<4 小时<br>关键业务影响 (Sev A):<1 小时|	最低业务影响 (Sev C):<4 营业时间<br>中等业务影响 (Sev B):<2 小时<br>关键业务影响 (Sev A):<1 小时|最低业务影响 (Sev C):<4 营业时间<br>中等业务影响 (Sev B):<2 小时<br>关键业务影响 (Sev A)：<1 小时<15 分钟（借助 Azure Rapid Response 或 Azure 事件管理）
定价|	$29/月|	$100/月|	$1,000/月|	联系销售

如遇到问题，请第一时间开Case，让后台帮助解决。根据实际业务影响程度，选择适合的case等级开出，后台人员会在响应时间与用户取得联系。

---

### 1.8. Azure 资源的组织形式 
Azure中的资源众多，怎样进行有效的管理也是一个重要的问题，Azure提供了多个模块，可以很好的对于资源进行分级管理。

**订阅**

订阅是与 Microsoft 就使用一个或多个 Microsoft 云平台或服务签订的协议，其费用基于每个用户许可证费用或云资源使用累计。

- Microsoft 基于软件即服务 (SaaS) 的云服务（Office 365、Intune/EMS 和 Dynamics 365）按用户收取许可证费用。
- Microsoft 的平台即服务 (PaaS) 和基础设施即服务 (IaaS) 云服务 (Azure) 根据云资源使用量收取费用。

**许可证**

对于 Microsoft 的 SaaS 云服务，许可证允许特定用户帐户使用云产品的服务。 作为订阅的一部分，你可以每月支付固定的费用。 管理员将许可证分配给订阅中的各个用户帐户。 对于图 2 中的示例，Contoso 公司订阅了具有 100 个许可证的 Office 365 企业版 E5，允许最多 100 个单个用户帐户使用 Office 365 企业版 E5 的功能和服务。

对于基于 Azure PaaS 的云服务，软件许可证是服务定价的一部分。

对于基于 Azure IaaS 的虚拟机，使用在虚拟机映像上安装的软件或应用程序可能需要其他许可证。某些虚拟机映像安装了授权版软件，并且成本包括在服务器的每分钟费率中。例如，SQL Server 2014 和 SQL Server 2016 的虚拟机映像。

**用户帐户**

所有 Microsoft 云服务的用户帐户均存储在 Active Directory (Azure AD) 租户中，其中包含用户帐户和组。 通过使用基于 Windows 服务器的服务 Azure AD Connect，Azure AD 租户可与你现有的 Active Directory 域服务 (AD DS) 帐户同步。 这叫做目录同步。

**Tenant**

对于 SaaS 云服务，租户是承载提供云服务的服务器的区域位置。例如，Contoso 公司选择欧洲地区为其巴黎总部的 15,000 名工作人员托管其 Office 365、EMS 和 Dynamics 365 租户。

Azure PaaS 服务和在 Azure IaaS 中托管的基于虚拟机的工作负荷可以在世界范围内的任何 Azure 数据中心拥有租户。在创建 Azure PaaS 应用或服务或 IaaS 工作负荷的元素时，应指定 Azure 数据中心（称为位置）。

Azure AD 租户是包含帐户和组的 Azure AD 的特定实例。Office 365、Dynamics 365 或 Intune/EMS 的付费或试用版订阅包括免费的 Azure AD 租户。此 Azure AD 租户不包括其他 Azure 服务，且与 Azure 试用版或付费订阅不同。

以下是快速回顾：
- 组织可进行多个订阅
- 订阅可具有多个许可证
- 许可证可分配给各个用户帐户
- 用户帐户存储在 Azure AD 租户中

**Management Group**

如果你的组织有多个订阅，则可能需要一种方法来高效地管理这些订阅的访问权限、策略和符合性。 Azure 管理组提供订阅上的作用域级别。 可将订阅组织到名为“管理组”的容器中，并将管理条件应用到管理组。 管理组中的所有订阅都将自动继承应用于管理组的条件。 不管使用什么类型的订阅，管理组都能提供大规模的企业级管理。 单个管理组中的所有订阅都必须信任同一个 Azure Active Directory 租户。

例如，可将策略应用到限制创建虚拟机 (VM) 的区域的管理组。 此策略将应用到该管理组下面的所有管理组、订阅和资源，只允许在该区域中创建 VM。

**Resource Group**

资源组是用于保存 Azure 解决方案相关资源的容器。 资源组可以包含解决方案的所有资源，也可以只包含想要作为组来管理的资源。 根据对组织有利的原则，决定如何将资源分配到资源组。 通常可将共享相同生命周期的资源添加到同一资源组，以便将其作为一个组轻松部署、更新和删除。

---

### 1.9. Azure资源命名的最佳实践 
在大型云采用工作中，以有助于运营管理和支持会计要求的方式来组织基于云的资产是一项常见挑战。通过将明确定义的命名和元数据标记约定应用于云托管资源，IT 人员可以快速查找和管理资源。通过使用退款和报销计帐机制，明确定义的名称和标记还有助于与业务团队协调云使用成本。

资源名称可能很难更改。 在开始进行任何大型云部署之前，应参考最佳实践，结合实际情况确定建立综合命名约定的优先级。

---

## 2.	动手实践
### 2.1.	Azure Portal页面及组件
![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding10.png?raw=true)

![image](https://github.com/ChinaOcpPTS/OCPChinaPTSALLDOCS/blob/master/03.Azure%E8%B5%84%E6%96%99%E5%90%88%E9%9B%86/New_Customer_Onboard/files/images/onboarding11.png?raw=true)
下表是各个组件及其说明：

组件 |	说明
:---|:---
1	|页眉。 显示在每个门户页面的顶部并保存全局元素。
2	|全局搜索。 使用搜索栏快速查找特定的资源、服务或文档。
3	|全局控件。 与所有全局元素一样，这些功能在门户中保持不变，包括： Cloud Shell、订阅筛选器、通知、门户设置、帮助和支持，并向我们发送反馈。
4	|你的帐户。 查看有关你的帐户、切换目录、注销或使用其他帐户登录的信息。
5	|门户菜单。 门户菜单是一个全局元素，可帮助您在服务之间导航。 有时也称为边栏，门户菜单模式可以在门户设置中进行更改。
6	|资源菜单。 许多服务都包含一个资源菜单，可帮助您管理该服务。 你可能会看到此元素称为左窗格。
7	|命令栏。 命令栏上的控件与当前焦点相关。
8	|工作窗格。 显示有关当前处于焦点的资源的详细信息。
9	|导航. 您可以使用痕迹链接在工作流中上移。
10	|用于在当前订阅中创建新资源的主控件。 展开或打开门户菜单，查找 " + 创建资源"。 搜索或浏览 Azure Marketplace，了解要创建的资源类型。
11	|收藏夹列表。 若要了解如何自定义列表，请参阅添加、删除和排序收藏夹。

### 2.2. 动手练习
- 练习如何通过 Azure Portal 及 CLI，创建并管理虚拟机：https://docs.microsoft.com/zh-cn/learn/paths/administer-infrastructure-resources-in-azure/
- 练习创建各种Azure资源 ：https://github.com/MicrosoftLearning/AZ-103-MicrosoftAzureAdministrator/tree/master/Instructions/Labs
- Workshop 如何在云端构建 Enterprise Ready 的系统 ：https://github.com/Microsoft/MCW-Enterprise-Ready-Cloud

---

## 3.	参考资料及Tips
- [Azure 概览](https://microsoftapc.sharepoint.com/:b:/t/OCPPRCPTSTeam/EbM6PUPPSgtIhHsjD7dSBpABq8BKHnd7KVHfb_YKu4SWnQ?e=M5l9S7) 
- Azure 基础知识 ：https://docs.microsoft.com/zh-cn/learn/paths/azure-fundamentals/
- Azure 技术文档：
Azure Mooncake ：https://docs.azure.cn/zh-cn/ 
Global Azure ：https://docs.microsoft.com/zh-cn/azure/
- 微软学习网站 （涵盖了包括Azure / O365 / D365在内多个产品内容）：https://docs.microsoft.com/zh-cn/learn/
- 针对典型的Workload相关的Workshop ：https://microsoftcloudworkshop.com/
