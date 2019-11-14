### HOL1:将Azure AD 登陆和审核日志发送到Azure Monitor
#### 前言：
本系列实验将引导用户完成O365 企业移动性和安全性（Enterprise Mobility Security）的常用操作和配置，本着实用性和安全性的原则，该系列实验会建议一些最佳实践。本系列实验主要分为以下几个阶段：
#### 1.	将Azure AD 登陆和审核日志发送到Azure Monitor
2.	用户自助密码重设&条件访问策略强制用户使用MFA二次验证&启用标识保护配置风险检测
3.	使用 Privileged Identity Management建立管理角色的审批和授权
4.	使用Intune 管理设备和移动设备
5.	使用Azure Information Protection 保护云中数据
6.	使用Azure Advanced Treat Protection保护混合环境的安全

#### 环境要求：
1.	O365企业版 E1/E3/E5(有O365国际版许可即可)；
2.	EMS E3/E5（部分用到E5的部分会做说明）；
3.	Azure订阅
#### 实验说明：
客户拿到O365账号后，会设置全局管理员。通常我们建议至少分配两个永久性全局管理员账户，一个做日常的运维管理，另一个作为备份账户使用。假设主管理员启用MFA，在手机网络中断时无法进行二次验证时，就需要备用管理账户紧急登录，因此备份账户的设置要求避开所有MFA及条件访问控制策略，后续的实验中我们会渗透这点。
#### 实验步骤：
1.	登录https://www.office.com 选择登录，输入管理员账号和密码。
2.	在左侧的导航栏点击用户活跃用户添加用户，这里新建一个管理员账户，角色选择 全局管理员，分配许可包含EMS和O365，本实验配置admin@XXX.onmicrosoft.com为主要全局管理员，user0@XXX.onmicrosoft.com 为备用全局管理员。 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-1.jpg)
3.	将 Azure AD日志发送到Azure Monitor。
执行此步骤的原因有下：
1)	因为备用全局管理员账户是在紧急状态下使用，因此避开了MFA和条件访问控制等策略，且具有全局管理的权限。为避免账号泄露带来不必要的损失，我们需要对此账号进行监控，确保该账号在非紧急状况下处于安全状态；
2)	Azure Monitor是Azure上提供的一项监控服务，可以监控服务器各项指标及应用，AAD相关的日志内容也可以被监控起来，可以借助Azure Monitor实现对备用账号的监控和告警；
3)	除了备用管理员账号，其他账号的监控操作同理。

用管理员账号密码登录到https://portal.azure.com ，在左侧的导航栏中找到Azure Active Directory,点击“诊断设置”，如果是一个没有Azure订阅的账号，会显示如下（如果该账号已有Azure订阅，可跳到下一步），点击“从此处开始创建新的订阅”，这个链接会引导申请一个Azure的试用订阅，200美金，一个月的额度，申请过程中要求绑定一张Visa、MasterCard或者American Express，输入相关信息后会收到短信提示预授权1美元，无需担心，一个月到后如果没有手动升级为付费订阅，该订阅将自动停止。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-2.jpg) 
申请完Azure试用订阅后，左侧导航栏点击 所有服务，搜索“Log Analytics”，“Log Analytics”是Azure Monitor负责收集分析日志的工作单元，为了将我们要监控的AAD日志汇聚在一个专门的容器中管理，我们需要创建一个工作区（workspace）用于存放这些数据。点击搜索结果“Log Analytics”工作区。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-3.jpg) 
在弹出的如下界面中点击创建Log Analytics工作区。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-4.jpg) 
输入工作区的名字，并且新建一个资源组，位置选择一个离我们较近的位置（日本或者东南亚都可以），填入相关信息后点击“完成”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-5.jpg) 
如下是创建好的界面。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-6.jpg) 
为了方便我们查看AAD Log的原生数据，我们同时创建一个存储账号。点击左侧“所有服务”，搜索框中输入“存储账户”，找到如下图标，点击“创建”，与上一步创建Log Analytics工作区类似，输入相关信息，位置和资源组与创建“Log Analytics”时选择相同，直到完成创建。在这里需要注意的是，存储账户的选择一定要性能选择“标准”，性能为“高级”的存储账户在诊断设置当中没有办法导入。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-7.jpg) 
左侧的导航栏中找到“Azure Active Directory”，点击“诊断设置”，点击“添加诊断设置”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-8.jpg) 
存储账户选择之前创建的账户， 勾选发送到“Log Analytics”, 工作区选择之前创建的，LOG部分将“Audit”和“SignIn”勾选，且“保留期（天数）”一定不可以填“0”否则日志信息将不会被保存也没有办法进行报警。最后点击最上方的保存。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-9.jpg) 
保存后的界面如下：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-10.jpg) 
回到“Azure Active Directory”，点击诊断设置上面的日志，点击“架构”，可以看到之前创建的AADdemo工作区已经显示在这里，点击展开“LogManagement”, 滚动鼠标，在下面的表中找到“AuditLogs”和“SignInLogs”，可以看到上一步设置的两个log已经集成进来了。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-11.jpg) 
找到“SignInLogs”，点击“眼睛”图标，显示此表中的示例记录，可以看到新建了一个查询2，默认把前50条记录给查询出来。我们针对整个日志可以用Kusto语句查询，有兴趣的伙伴可以参考：https://docs.microsoft.com/zh-cn/azure/azure-monitor/log-query/get-started-queries 查询相关内容。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-12.jpg)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-13.jpg)
回到Azure Active Directory，点击“监视”下面的登陆和审核日志，也分别可以看到相关内容，这里的内容会更加直观，并提供了筛选和导出相关功能。有审计需要可以直接来这里导出。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-14.jpg) 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-15.jpg) 
也可以去之前创建的存储账号里查看日志内容：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-16.jpg) 
接下来我们针对要监控的备用全局管理员账户进行报警设置。回到“Azure Active Directory”，点击“用户”“所有用户”，选择你要监控的账号，点击“进入”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-17.jpg) 
在“配置文件”部分，找到“标识”“对象ID”，点击“对象ID”旁边的复制标志，将“对象ID”复制下来。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-18.jpg) 
在左侧导航栏“所有服务”“搜索”“Log Analytics”工作区（可以将搜索结果右侧的五角星点击收藏，这样“Log Analytics”工作区就会显示在左侧的导航栏里）中点击“警报”“新建预警规则”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-19.jpg) 
资源选择之前创建好的工作区名字， 条件选择点击“Custom Log Search”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-20.jpg) 
搜索查询 填入如下语句： 
SigninLogs 
| project UserId
| where UserId == "4d12a5e0-f52a-45a9-9fa7-39d78a9732d8"（这里的UserId就是刚才复制的 “对象ID”，同时请注意保留UserId的双引号）
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-21.jpg) 
点击完成后，再选择“操作”“添加操作组”，按下图配置，电子邮件和电话号码选填要接受警报的相关责任人联系方式。操作完成后，页面最下方创建后启用规则 选“是”，点击“保存”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-22.jpg) 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-23.jpg) 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL1-24.jpg) 
最后我们重新开启一个浏览器页面，以隐私模式打开，登录https://office.com 后用备用管理员账号（本实验用user0@XXX.onmicrosoft.com ）登录，查看手机和电子邮件是否收到警报通知。
参考文档：https://docs.microsoft.com/zh-cn/azure/active-directory/users-groups-roles/directory-emergency-access 
