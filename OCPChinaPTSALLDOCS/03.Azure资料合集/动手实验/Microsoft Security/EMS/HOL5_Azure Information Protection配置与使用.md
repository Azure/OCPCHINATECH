### HOL1:Azure Information Protection配置与使用
#### 前言：
本系列实验将引导用户完成O365 企业移动性和安全性（Enterprise Mobility Security）的常用操作和配置，本着实用性和安全性的原则，该系列实验会建议一些最佳实践。本系列实验主要分为一下几个模块：
本系列实验将引导用户完成O365 企业移动性和安全性（Enterprise Mobility Security）的常用操作和配置，本着实用性和安全性的原则，该系列实验会建议一些最佳实践。本系列实验主要分为以下几个阶段：
1.	将Azure AD 登陆和审核日志发送到Azure Monitor
2.	用户自助密码重设&条件访问策略强制用户使用MFA二次验证&启用标识保护配置风险检测
3.	使用 Privileged Identity Management建立管理角色的审批和授权
4.	使用Intune 管理设备和移动设备
#### 5.	使用Azure Information Protection 保护云中数据
1)	快速入门：在 Azure 门户中开始使用 Azure 信息保护
2)	快速入门：为用户配置标签以便轻松保护包含敏感信息的电子邮件
3)	快速入门：为特定用户创建新的 Azure 信息保护标签
4)	教程：配置 Azure 信息保护策略设置并创建新标签
5)	教程：配置协同工作的 Azure 信息保护策略设置
6)	教程：配置 Azure 信息保护以使用 Outlook 控制信息的过度共享
6.	使用Azure Advanced Treat Protection保护混合环境的安全

#### 必备条件：
1.	包含 Azure 信息保护（AIP）计划 1 或计划 2 的订阅；
2.	你已从下列类别之一登录到 Office 应用：
+ Office 应用最低版本 1805，Office 365 商业版或 Microsoft 365 商业版中的内部版本 9330.2078，前提是已为你分配了 Azure Rights Management（亦称为“适用于 Office 365 的 Azure 信息保护”）许可证。
+ Office 365 专业增强版。
+ Office 专业增强版 2019。
+ Office Professional Plus 2016。
+ Office Professional Plus 2013 Service Pack 1。
+ Office Professional Plus 2010 Service Pack 2。
3.	Azure 信息保护客户端（经典）安装在 Windows 计算机上（最低版本为 Windows 7 Service Pack1）
	https://www.microsoft.com/en-us/download/details.aspx?id=53018该页面可以下载Microsoft Azure Information Protection,下载完成之后可以直接安装。

#### 实验步骤：
1.	登录https://portal.Azure.com 选择登录，输入全局管理员账号和密码。
2.	在左侧的导航栏选择用户活跃用户添加用户，这里新建一个管理员账户，角色选择全局管理员，分配许可包含EMS和O365，本实验配置admin@XXX.onmicrosoft.com为主要全局管理员，user0@XXX.onmicrosoft.com 为备用全局管理员。 
3.	为了方便实验时不受原本域环境的干扰建议先建立一个计算机本地账户建立方法如下：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-1.png) 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-2.png)  
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-3.png)  
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-4.png)  
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-5.png) 

 
这里输入你要创建的用户名以及密码。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-6.png)  
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-7.png)  
+ 点击左下角的“其他用户”
+ 然后会出现一个用户名框和一个密码框
+ 用户名框请输入“.\+你的用户名”表示是本地用户。例如，用户名是Jalen就输入.\Jalen。
+ 输入完成之后登录到本地环境当中。
 

### 快速入门：在Azure门户中开始使用Azure信息保护
#### 1.	实验任务：确认AIP服务出于可用状态
现在已为新客户自动激活保护服务，但最好确认是否已经激活。
在“Azure 信息保护”边栏选项卡上，选择“管理”  “保护激活” 。
如果已经激活则在页面当中可以看到保护状态为“已激活”
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-8.png)  
如果保护尚未激活，请选择“激活”激活完成后则显示上图所示内容。
 
### 快速入门：为用户配置标签以便轻松保护包含敏感信息的电子邮件
#### 实验任务：为用户配置AIP标签，管理邮件
1.	配置现有标签以应用“不得转发”保护
+ 进入AIP点击边栏选项卡当中的“标签按钮”
+ 点击需要编辑的标签
+ 设置“为包含此标签的文档和电子邮件设置权限”为“保护”
+ 选择“设置用户定义的权限(预览)”
+ 取消勾选“在 Word、Excel、PowerPoint 和文件资源管理器中提示用户获取自定义权限”
+ 保存

![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-9.png)  
#### 2.	测试新标签
+ 在计算机上打开 Outlook并创建新的电子邮件。 如果 Outlook 已打开，请重新启动它以强制执行策略刷新。
+ 指定收件人、电子邮件的部分文本，然后应用刚刚创建的标签。
+ 电子邮件根据标签名称进行分类，并使用“不得转发”限制进行保护。
+ 发送电子邮件。

![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-10.png)   
 
### 快速入门：为特定用户创建新的 Azure 信息保护标签
#### 1.	实验任务：
+ 为特殊用户创建专属标签
#### 2.	创建新标签
+ 在AIP选项卡当中点击“标签”，单击“添加新标签”。
+ 设置标签显示名称：用户将看到的新标签名称，用于标识内容的分类。例如：Sales - Restricted。
+ 设置说明：工具提示，用于帮助用户确定何时选择此新标签。例如：Business data that is restricted to the Sales Team.
+ 设置已启用标签为“开”
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-11.png)    
#### 3.	创建新策略
+ 在“策略”选项卡当中选择“添加新策略”
+ 在“策略” 边栏选项卡上，对于“策略名称” 框，输入一个名称，用于标识哪组用户能够查看新创建的标签。 例如，Sales。
+ 选中“选择哪些用户或组可以获取此策略” 选项。
+ 在“AAD 用户和组” 边栏选项卡上，选择“用户/组”。 然后，在新的“用户/组” 边栏选项卡上，搜索并选择在先决条件中标识的组。 例如，“销售团队”。 单击该边栏选项卡上的“选择” ，然后单击“确定”。 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-12.png)    
+ 在“策略” 边栏选项卡上，选择“添加或删除标签”。
+ 在“策略:在“添加或删除标签” 边栏选项卡上，选择已创建的标签，例如，“销售-受限” ，然后选择“确定”。
+ 重新回到“策略” 边栏选项卡，选择“保存”。 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-13.png)    
#### 4.	测试新标签
+ 在第一台计算机上，以“销售团队”组的成员身份登录。 打开 Word，确认可以看到新标签。 如果 Word 已打开，请重新启动它以强制执行策略刷新。
+ 在第二台计算机上，以非“销售团队”组的成员身份登录。 打开 Word，确认看不到新标签。 与前面一样，如果 Word 已打开，则重新启动它。
+ Tips：这里只测试了一台计算机，如果时间有限可以只测试一台。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-14.png)    
 
### 教程：配置 Azure 信息保护策略设置并创建新标签
#### 1.	实验任务：
+ 配置策略设置
+ 创建新标签
+ 配置视觉标记、建议分类和保护的标签
+ 在实际操作中查看设置和标签
#### 2.	编辑 Azure 信息保护策略
+ 打开AIP
+ 打开“策略”选项卡，选择“Global”策略
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-15.png)    
+ 对于“选择默认标签” ，请选择其中一个标签，例如“General（常规）”。
+ “General（常规）” 标签是 Azure 信息保护可为你创建的默认标签之一。 快速入门中的创建和发布标签部分中介绍了此步骤，即将 Azure 信息保护添加到 Azure 门户。
+ 对于“用户必须提供设置较低分类标签、删除标签或删除保护的理由” ，请将此选项设置为“开”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-16.png)    
+ 另外，请务必将“在 Office 应用程序中显示信息保护栏”这一项 设置为“开” 。
+ 选择此“策略: Global”边栏选项卡上的“保存” ， 如果系统提示你确认操作，请选择“确定” 。 关闭此边栏选项卡。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-17.png)    
#### 3.	创建保护新标签、视觉标记和分类提示条件
+ 从“分类” “标签”菜单选项中 ：右键单击“Confidential”标签，然后选择“添加子标签” 。
+ 如果没有名为“Confidential” 的标签，可以选择另一个标签，也可以创建一个新标签，具体操作步骤仍与本教程相同，只存在细微差异。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-18.png)    
+ 在“子标签” 边栏选项卡上，指定“财务” 的标签名称，并添加以下说明：包含财务信息的机密数据仅限员工使用 。
+ 此文本说明应如何使用所选标签，并显示为一个工具提示，帮助用户确定要选择的标签。
+ 对于“为包含此标签的文档和电子邮件设置权限” ，选择“保护” ，这会在为你选择“保护”选项时，自动打开“保护” 边栏选项卡 ：
+ 在“保护”边栏选项卡中，确保选中“Azure (云密钥)” 。 此选项使用 Azure Rights Management 服务保护文档和电子邮件。 还请务必选择“设置权限”选项 。 然后选择“添加权限” 。
+ 在“添加权限”边栏选项卡上，选择“添加 <组织名称> - 所有成员” 。 例如，如果组织名称为 VanArsdel Ltd，则会看到以下选项可供选择：
+ 对于权限，请在预设选项中选择“审阅者” 。 可了解此权限级别如何自动授予部分列出的权限而不是所有权限：
+ 单击“确定”关闭“添加权限”边栏选项卡，可看到“保护”边栏选项卡如何更新以反映配置 。 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-19.png)    
+ 返回“子标签”边栏选项卡，找到“设置视觉标记”部分 ：
+ 对于“包含此标签的文档具有页脚”设置，请单击“开”，然后在“文本”框中键入“分类为机密” 。
+ 对于“使用该标签的文档具有一个水印” 设置：单击“开” ，然后在“文本” 框中键入你的组织名称。 例如，VanArsdel, Ltd。水印功能和页眉功能类似这里就没有截图。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-20.png)    
+ 定位到“配置条件以自动应用该标签” 部分：
+ 单击“添加新条件”，然后在“条件”边栏选项卡中选择以下选项 ：
a. 选择条件类型：保留默认值“信息类型” 。
b. 对于“选择行业” ：保留默认值“全部” 。
c. 在“选择信息类型” 搜索框中：键入“Credit（信用）” 。 然后，从搜索结果中选择“Credit Cards Number（信用卡号）” 。
d. 最少出现次数：保留默认值“1” 。
e. 仅计算唯一值的发生次数：保留默认值“关闭” 。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-21.png)   
+ 对于选择应用此标签的方式：保留默认设置“推荐”，并且不要更改默认策略提示。
+ 在“添加备注以供管理员使用”框中，键入“仅用于测试目的” 。
+ 在此“子标签”边栏选项卡上单击“保存”。如果系统提示你确认，请单击“确定”。将创建和保存新标签，但尚未将其添加到策略。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-22.png)   
+ 在此“子标签”边栏选项卡上单击“保存” 。 如果系统提示你确认，请单击“确定” 。 将创建和保存新标签，但尚未将其添加到策略。
+ 从“分类”  “策略”菜单选项中 ：再次选择“Global” ，然后选择标签后的“添加或删除标签” 链接。
+ 从“策略: 添加或删除标签”边栏选项卡中，选择刚刚创建的标签（名为“财务” 的子标签），然后单击“确定” 。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-23.png)   
#### 4.	在实际操作中查看分类、标签设置和保护
+ 在 Word 中打开一个新文档。 由于已安装 Azure 信息保护客户端，可以看到以下视图：
+ 在这个文档当中点击“（🗑）垃圾桶”符号，可以删除标签，如果选择“🖉（笔）”符号，再选择其他的标签，则可以更换标签。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-24.png)   
+ 在Word 文档中，键入有效的信用卡号，例如：4242-4242-4242-4242。
+ 使用任意文件名在本地保存文档。
+ 现在，检测到信用卡卡号时，将看到一条提示，提示用户使用针对保护配置的标签。 如果不同意这条建议，可通过选择“忽略” 来拒绝这一建议。 提供建议同时允许用户重写，可帮助减少使用自动分类时的误报。 在本教程中，请单击“立即更改” 。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-25.png)   
 
### 教程：配置协同工作的 Azure 信息保护策略设置
#### 1.	实验任务：
+ 配置协同工作的策略设置
+ 在实际操作中查看设置
#### 2.	编辑 Azure 信息保护策略
+ 打开新的浏览器窗口，以全局管理员身份登录到 Azure 门户。然后导航到“AIP” 。
+ 选择“分类”“策略” “Global（全局）” ，打开“策略: Global”边栏选项卡 。
+ “选择默认标签”选择为“General（常规）”
+ “对于强制所有文档和电子邮件都具有标签”设置“开”。
+ “对于带有附件的电子邮件，使用与这些附件的最高等级相匹配的标签”设置“推荐”。
+ “在 Office 应用程序中显示信息保护栏”设置为“开”
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-26.png)   
#### 3.	在实际操作中查看策略设置
+ 在 Word 中打开一个新文档。 你会看到文档自动标记为“General（常规）” ，而不是依赖用户选择标签。
+ 当带标签的附件添加到邮件当中是，邮件会自动增加相关的标签提示。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-27.png)   
 
### 教程：配置 Azure 信息保护以使用 Outlook 控制信息的过度共享
#### 1.	实验任务：
+ 配置在 Outlook 中实现警告、证明或阻止弹出邮件的设置
+ 在实际操作中查看设置
+ 查看事件日志中记录的用户消息和操作
#### 2.	标识用于测试的标签 ID
+ 打开新的浏览器窗口，以全局管理员身份登录到 Azure 门户。然后导航到“Azure 信息保护” 。
+ 例如，在中心菜单上单击“所有服务”，然后在筛选框中开始键入“信息” 。 选择“Azure 信息保护”。
+ 如果你不是全局管理员，请使用以下链接获取替代角色：登录到 Azure 门户
+ 选择“分类”“标签”，然后选择“General（常规）”边栏选项卡以打开“标签: General（常规）”边栏选项卡。
+ 找到边栏选项卡底部的标签 ID：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-28.png)   
#### 3.	创建作用域内策略以测试新的高级客户端设置
+ 在“Azure 信息保护 -策略”边栏选项卡上，选择“添加新策略” 。 然后，你会看到“策略”边栏选项卡，它显示现有全局策略中的标签和设置 。
+ 指定“过度共享教程”的策略名称，例如，这里使用的名称是 “共享策略”。
+ 选择“指定获取此策略的用户/组”，并使用后续边栏选项卡指定你自己的用户账户 。
+ 账户名显示在“策略”边栏选项卡上后，请选择“保存”且不在此边栏选项卡上的标签或设置进行其他更改。系统可能会提示你确认你的选择。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-29.png)   
#### 4.	配置并测试以下高级客户端设置：警告、提示提供理由或阻止具有“General（常规）”标签的电子邮件。
+ 返回到“Azure信息保护 - 策略”边栏选项卡，选择“共享策略”旁边的上下文菜单 (...) 。 再选择“高级设置” 。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-30.png)   
+ 在“高级设置”边栏选项卡上，键入高级设置名称“OutlookWarnUntrustedCollaborationLabel”，并为该值粘贴自己的标签 ID 。 使用示例标签 ID：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-31.png)   
+ 在客户端计算机上，打开 Outlook。
+ 如果 Outlook 已打开，则重启它。 需要重启才能下载我们刚刚进行的更改。
+ 创建新的电子邮件，并应用“General（常规）”标签 。 例如，在“文件”选项卡中，选择“保护”按钮，然后选择“General（常规）” 。
+ 为“收件人”字段指定自己的电子邮件地址，并为主题键入“测试警告消息的常规标签” 。 然后，发送电子邮件。
+ 作为高级客户端设置的结果，你会看到以下警告，要求在发送电子邮件之前进行确认。 例如：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-32.png)  
 
+ 我们将编辑现有的高级客户端设置以保留你的“General（常规）”标签 ID，但会将名称更改为“OutlookJustifyUntrustedCollaborationLabel” ：
+ 在“Azure信息保护 - 策略”边栏选项卡上，选择“过度共享教程”旁边的上下文菜单 (...) 。 再选择“高级设置” 。
+ 在“高级设置”边栏选项卡上，使用新名称“OutlookJustifyUntrustedCollaborationLabel”替换你先前创建的高级设置名称“OutlookWarnUntrustedCollaborationLabel” ：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-33.png)   
+ 在客户端计算机上，重启 Outlook 以下载我们刚刚进行的更改。
+ 创建新的电子邮件，并像以前一样，应用“General（常规）”标签 。 例如，在“文件”选项卡中，选择“保护”按钮，然后选择“General（常规）” 。
+ 为“收件人”字段指定自己的电子邮件地址，并为主题键入“测试证明消息的General（常规）标签” 。 然后，发送电子邮件。
+ 此时，你会看到以下消息，要求在发送电子邮件之前提供理由。 例如：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-34.png)   
+ 我们将再次编辑现有的高级客户端设置以保留你的“General（常规）”标签 ID，但会将名称更改为“OutlookBlockUntrustedCollaborationLabel” ：
+ Azure 门户中，在“Azure信息保护 - 策略”边栏选项卡上，选择“过度共享教程”旁边的上下文菜单 (...) 。 再选择“高级设置” 。
+ 在“高级设置”边栏选项卡上，使用新名称“OutlookBlockUntrustedCollaborationLabel”替换你先前创建的高级设置名称“OutlookJustifyUntrustedCollaborationLabel” ：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-35.png)   
+ 在客户端计算机上，我们现在将看到此新高级客户端设置的结果。
+ 在客户端计算机上，重启 Outlook 以下载我们刚刚进行的更改。
+ 创建新的电子邮件，并像以前一样，应用“General（常规）”标签 。 例如，在“文件”选项卡中，选择“保护”按钮，然后选择“General（常规）” 。
+ 为“收件人”字段指定自己的电子邮件地址，并为主题键入“测试阻止消息的General（常规）标签” 。 然后，发送电子邮件。
+ 此时，会显示阻止发送电子邮件的以下消息。 例如：

![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-36.png) 

+ 同时按下Win和X键

![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-37.png)   

+ 点击事件查看器

![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-38.png)  

+ 	对于执行的每个测试，都会创建信息事件以记录消息和用户响应：
+ 警告消息：信息 ID 301
+ 验证消息：信息 ID 302
+ 阻止邮件：信息 ID 303
+ 例如，第一个测试是警告用户，你选择了“取消”，因此第一个事件 301 中的“用户响应”显示为“已取消” 。 例如：

![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-39.png)   
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-40.png) 

+ Azure 门户中，在“Azure信息保护 - 策略”边栏选项卡上，选择“过度共享教程”旁边的上下文菜单 (...) 。 再选择“高级设置” 。
+ 在“高级设置”边栏选项卡上，键入高级设置名称“OutlookBlockTrustedDomains”，然后从电子邮件地址中粘贴域名以获取该值 。 例如：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-41.png)    
+ 根据测试结果可以看出，不在限定范围内的电子邮件已经被阻止，而在范围内的邮件可以正常发送。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-42.png)    
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-43.png)    
#### 5.	配置和测试以下高级客户端设置：警告、提示提供理由或阻止没有标签的电子邮件
+ 此名为“OutlookUnlabeledCollaborationAction”的新高级客户端设置不需要标签 ID，但指定了对未标记内容采取的操作 ：
+ Azure 门户中，返回到“Azure信息保护 - 策略”边栏选项卡上，选择“共享教程”旁边的上下文菜单 (...) 。 再选择“高级设置” 。
+ 在“高级设置”边栏选项卡上，键入高级设置名称“OutlookUnlabeledCollaborationAction”，并为值指定“警告” ：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-44.png)    
+ 在客户端计算机上，重启 Outlook 以下载我们刚刚进行的更改。
+ 创建新的电子邮件，这次不要应用标签。
+ 为“收件人”字段指定自己的电子邮件地址，并为主题键入“测试发送不带警告消息的标签的电子邮件” 。 然后，发送电子邮件。
+ 这次可看到“需要确认”消息，可选择“确认并发送”或“取消” ：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-45.png)    
+ 此名为“OutlookUnlabeledCollaborationAction”的新高级客户端设置不需要标签 ID，但指定了对未标记内容采取的操作 ：
+ Azure 门户中，返回到“Azure信息保护 - 策略”边栏选项卡上，选择“过度共享教程”旁边的上下文菜单 (...) 。 再选择“高级设置” 。
+ 在“高级设置”边栏选项卡上，键入高级设置名称“OutlookUnlabeledCollaborationAction”，并为值指定“警告” ：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-46.png)    
+ 在客户端计算机上，重启 Outlook 以下载我们刚刚进行的更改。
+ 创建新的电子邮件，这次不要应用标签。
+ 为“收件人”字段指定自己的电子邮件地址，并为主题键入“测试发送不带警告消息的标签的电子邮件” 。 然后，发送电子邮件。
+ 这次可看到“需要确认”消息，可选择“确认并发送”或“取消” ：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-47.png)    
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-48.png)    
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-49.png)    
+ 与以前一样，消息和用户响应记录在事件查看器“应用程序和服务日志” > “Azure 信息保护”中，并具有相同的事件 ID 。
+ 警告消息：信息 ID 301
+ 验证消息：信息 ID 302
+ 阻止邮件：信息 ID 303
+ 例如，电子邮件没有标签时，理由提示会显示以下结果：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-50.png)    
+ 如果你不想保留在本教程中所做的更改，请执行以下操作：
+ Azure 门户中，在“Azure信息保护 - 策略”边栏选项卡上，选择“过度共享教程”旁边的上下文菜单 (...) 。 然后选择“删除策略” 。
+ 如果系统提示你确认，请选择“确定” 。
+ 重启 Outlook，以便不再为我们为本教程配置的设置进行配置。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL5-51.png)    
