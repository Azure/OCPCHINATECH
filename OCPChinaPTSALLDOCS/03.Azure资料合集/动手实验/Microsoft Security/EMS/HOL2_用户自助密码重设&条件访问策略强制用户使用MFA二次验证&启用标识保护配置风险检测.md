### HOL2:用户自助密码重设&条件访问策略强制用户使用MFA二次验证&启用标识保护配置风险检测
#### 前言：
本系列实验将引导用户完成O365企业移动性和安全性（Enterprise Mobility Security）的常用操作和配置，本着实用性和安全性的原则，该系列实验会提供案例最佳实践。本系列实验主要分为以下几个阶段：
1.	将Azure AD 登陆和审核日志发送到Azure Monitor
#### 2.	用户自助密码重设&条件访问策略强制用户使用MFA二次验证&启用标识保护配置风险检测
3.	使用 Privileged Identity Management建立管理角色的审批和授权
4.	使用Intune 管理设备和移动设备
5.	使用Azure Information Protection 保护云中数据
6.	使用Azure Advanced Treat Protection保护混合环境的安全

#### 环境要求：
1.	O365企业版 E1/E3/E5(有O365国际版许可即可)；
2.	EMS E3/E5（部分用到E5的部分会做说明）；
3.	Azure订阅
#### 实验说明：
在企业IT管理中，通常要求用户可以在忘记密码的时候自助重置密码，并且要求用户（所有或者部分）在登录是强制进行二次认证（短信或电话），本篇实验将引导完成相关配置。
#### 实验步骤：
1.	用户自助密码重设
实验开始前，我们再次梳理下现在的账户状态：
主要全局管理员：admin@M365n634099.onmicrosoft.com 
备用全局管理员：user0@M365n634099.onmicrosoft.com 
本实验需要额外创建：
用户：meganb@M365n634099.onmicrosoft.com  
组：mfagroup@M365n634099.onmicrosoft.com 
密码重置属性将针对组mfagroup设置。
在https://admin.microsoft.com/Adminportal/Home?source=applauncher#/homepage 登录管理员账号创建如下，将组管理员设置为meganb@M365n634099.onmicrosoft.com，组成员也设置为：
meganb@M365n634099.onmicrosoft.com。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-1.png)
 
登录https://portal.azure.com 管理员账号，找到Azure Active Directory密码重置属性，在已启用自助服务密码重置，选择选定“mfagroup”。 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-3.png) 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-5.png) 
当我们设定好这些信息之后需要先给测试用户设定一个初始密码，点击“用户名”，再点击“钥匙”标志即可重置用户密码。这里我们需要设定一个我们已知的密码，因为我们需要通过这个密码登录该账户，补充用于自助重置密码所需的通讯信息。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-7.png) 
在密码重置，将“要求用户在登录时注册？”按钮置选为“是”，“保存”。因为当你要自助重置密码，大多数情况是你忘记了现在的密码，这种情况下如果要重置，后台需要确认你是你自己，所以要求你在系统中先注册你的电话号码和邮件，这样你重置密码的时候可以通过电话接收验证码来验证你是你自己。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-9.png) 
在“密码重置-通知”中，按如下配置保存。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-11.png) 
在“密码重置-自定义”中，电子邮件可填写重置密码有障碍时寻求支持的管理员邮件地址。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-13.png)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-15.png) 
配置完成后，保存。保存成功后，再回到https://office.com登录，使用meganb@M365n634099.onmicrosoft.com 输入账号后选择“忘记了密码”，会出现如下提示：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-17.png)  
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-19.png) 
这里无法自助重置密码是因为我们之前在登录时并没有输入用于重置密码的通讯信息，因此无法自助重置服务密码。如果用户在自助重置密码的组中，首次登录时会要求用户进行通讯信息的补充。
因此我们先使用刚刚给该用户重置的初始密码登录该账户。
按照提示点击“set it up now”，设置电话号码和邮箱，点击完成。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-21.png) 
设置好之后，我们再重复刚才的步骤“忘记了密码”即可自助重置密码
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-23.png) 
输入邮件或者短信中的验证码后成功修改密码。
再回到https://portal.azure.com 用管理员账号登录查看，AAD用户所有用户，点击meganb@M365n634099.onmicrosoft.com 这个用户，身份验证方法，查看这里的身份验证信息就是上一步set up it now中填写的信息，这个用于验证你的身份。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-25.png) 
设置密码时通常需要考虑如何避免设置过于简单的密码，企业需要配置自定义禁止密码列表（需要 Active Directory Premium P1 或 P2 许可证）。
在“AAD”“身份验证方法”“密码保护”，“保存”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-27.png) 
继续验证：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-29.png) 
如需配置用户密码过期时间等，可参考https://docs.microsoft.com/zh-cn/azure/active-directory/authentication/concept-sspr-policy#set-a-password-to-never-expire 用Power Shell做相应配置。
2.	条件访问策略强制用户使用MFA二次验证。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-31.png)
再次梳理下现在的账户状态：
主要全局管理员：admin@M365n634099.onmicrosoft.com  
备用全局管理员：user0@M365n634099.onmicrosoft.com  
用户：meganb@M365n634099.onmicrosoft.com   
组：mfagroup@M365n634099.onmicrosoft.com ，该组内的用户已配置自助密码设置。
接下来实验要对除了管理员账户以外的所有用户实施强制MFA策略。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-33.png)
先看下传统做法：在“AAD”“用户”“所有用户”中，如下，点击多重身份验证 ，可以到一个多重身份验证的页面，有选择的针对某个客户 启用或者禁用 MFA，如下： 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-35.png) 
这样做的弊端是，开始MFA需要客户有一个电话或邮箱信息，第1个实验中用户重置密码也需要电话或邮箱信息做认证，从安全角度讲，我们希望这两套电话/邮箱信息是一致的，也就是配置了密码自助的用户在配置MFA的时候不需要重复输入这些信息，EMS中现在有一个处于public preview的功能叫做“密码和MFA的联合注册”，配置步骤如下：“AAD”“用户设置”“管理用户功能预览设置”，选择“全部”，“保存”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-37.png)  
做好以上配置后，我们来到“AAD”“条件访问” “新建策略”，为该策略起一个名称，“分配”下面，“用户和组”里，“包括”选择“所有用户”，排除“备用管理员账户”；“云应用或操作”选择“所有应用”，“访问控制”选择“要求多身份验证”，保存之前会提示要不要避开自己（当前管理员账号），这里选择避开，保存。这样就强制要求除了两个全局管理员之外的所有用户登录时启动MFA做验证。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-39.png)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-41.png)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-43.png)
回到https://office.com
使用用户meganb@M365n634099.onmicrosoft.com 登录后提示：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-45.png)  
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-47.png) 
由于开启了联合注册，二次认证时自然向第1步实验中注册的电话号码发送了短信验证码，成功登录。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-49.png) 
风险检测说明 https://docs.microsoft.com/zh-cn/azure/active-directory/reports-monitoring/concept-risk-events 
3.	启用标识保护配置风险检测
AAD风险检测使用自适应机器学习算法和试探法来检测与用户账户相关的可疑操作，需要使用
使用“Azure Active Directory 标识保护”功能（需要 Azure AD Premium P2 许可证），首先在Azure Portal上搜索“Azure AD标识保护”，搜索结果点击第二个（不带预览版的字样）。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-51.png) 
进入“MFA注册策略”“用户”，设置包括所有人，排除user0（之前设置的备份全局管理员）。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-53.png) 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-55.png)
强制执行策略“开”，“保存”。此时admin账户也会被强制执行MFA。下面设置一个“登录风险”的条件控制：条件选择“中等及以上”（此处风险级别的划分可参考：https://docs.microsoft.com/zh-cn/azure/active-directory/reports-monitoring/concept-risk-events ），按如下配置，最终设置为，监测到有登录风险存在时，立即强制修改密码。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-57.png)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL2-59.png) 
 

参考文档：
https://docs.microsoft.com/zh-cn/azure/active-directory/authentication/tutorial-risk-based-sspr-mfa 
https://docs.microsoft.com/zh-cn/azure/active-directory/authentication/howto-mfa-getstarted 
