### HOL4: 使用Intune 管理设备和移动设备
#### 前言：
本系列实验将引导用户完成O365 企业移动性和安全性（Enterprise Mobility Security）的常用操作和配置，本着实用性和安全性的原则，该系列实验会建议一些最佳实践。本系列实验主要分为以下几个阶段：
1.	将Azure AD 登陆和审核日志发送到Azure Monitor
2.	用户自助密码重设&条件访问策略强制用户使用MFA二次验证&启用标识保护配置风险检测
3.	使用 Privileged Identity Management建立管理角色的审批和授权
#### 4.	使用Intune 管理设备和移动设备
5.	使用Azure Information Protection 保护云中数据
6.	使用Azure Advanced Treat Protection保护混合环境的安全

#### 环境要求：
1.	O365企业版 E1/E3/E5(有O365国际版许可即可)；
2.	EMS E3/E5（部分用到E5的部分会做说明）；
3.	Azure订阅
#### 实验说明：
企业管理中，无论是BYOD的个人设备，还是设备上一系列O365办公组件，涉及到公司数据（邮箱、会议）的信息，从安全的角度讲都需要进行有效管控，Microsoft Intune可以帮助管理移动设备和应用。本次实验将引导完成对设备的管控。
#### 实验步骤：
1.	配置条件访问控制策略
登录Azure门户搜索“Intune”;
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-2.jpg)
 
进入后，如发现有以下红框内的提示，则需要启用设备管理，点击框住的部分。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-34.jpg)  
在划出的页面上，选择“Intune MDM机构”，保存。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-36.jpg)   
然后在Intune的页卡上，选择租户状态，当“MDM机构“变成图示状态时，则说明设置生效，才可以继续进行下一步。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-38.jpg)   
 

Intune条件访问新建策略
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-4.jpg)    
输入对应的名称。【分配】的【用户和组】选项，【包括】选所有，【排除】这里勾选之前设置的全局管理员。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-6.jpg)    
【云应用与操作】【条件】按照如下配置：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-8.jpg)    
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-12.jpg)      
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-16.jpg)    
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-14.jpg)    
 
访问控制配置如图：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-18.jpg)    
设置完成后，【启用策略】选择【打开】，【创建】。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-40.jpg)    
2.	配置win10设备的自动注册
回到https://portal.azure.com，点击【Azure Active Directory】-> 移动性（MDM和MAM）-> Microsoft Intune
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-20.jpg)    
红框部分选择要启动自助注册的用户或组（这里可以自定义一个组，把除了全局管理员之外的其他用户都放在同一个组里进行一键勾选）
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-22.jpg)    
其余值选择默认，【保存】。
该策略创建成功后，会要求除了两位全局管理员之外的所有用户在设备上登录O365 应用的时候启用设备注册和认证。
3.	验证。
此处我们用虚拟机建一台win 10（不必是服务器，系统满足即可）来模拟BYOD的设备。VM建好之后，使用之前选择的mdm组中的任意一个账户登陆https://office.com ，会发现如下告警：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-24.jpg)   
 
点击“设置>账户>访问工作或学校”根据指引我们输入账号相关信息进行验证：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-26.jpg)  
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-28.jpg)  
配置完成后需要后台同步一段时间，我们回到Intune的管理界面看一下：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-30.jpg)    
当出现如上信息，表明刚刚的win10已经注册上来了，此时它已是一个符合策略的设备。点击这个设备：我们可以进行远程控制。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL4-32.jpg)   
另：做完以上操作后，我们如果是登录移动端，会要求你先下载【公司门户】的app进行设备注册，注册完之后方可登录O365 Apps。 

参考文档：
https://docs.microsoft.com/zh-cn/intune/enrollment/quickstart-enroll-windows-device 
https://docs.microsoft.com/zh-cn/intune/protect/app-based-conditional-access-intune-create 
https://docs.microsoft.com/zh-cn/intune/fundamentals/tutorial-walkthrough-intune-portal 
