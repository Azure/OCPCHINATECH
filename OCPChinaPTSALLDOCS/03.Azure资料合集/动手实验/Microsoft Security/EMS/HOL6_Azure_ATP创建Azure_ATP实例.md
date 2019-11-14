### HOL6：Azure ATP 创建Azure ATP实例
#### 前言：
本系列实验将引导用户完成O365 企业移动性和安全性（Enterprise Mobility Security）的常用操作和配置，本着实用性和安全性的原则，该系列实验会建议一些最佳实践。本系列实验主要分为以下几个阶段：
1.	将Azure AD 登陆和审核日志发送到Azure Monitor
2.	用户自助密码重设&条件访问策略强制用户使用MFA二次验证&启用标识保护配置风险检测
3.	使用 Privileged Identity Management建立管理角色的审批和授权
4.	使用Intune 管理设备和移动设备
5.	使用Azure Information Protection 保护云中数据
#### 6.	使用Azure Advanced Treat Protection保护混合环境的安全

#### 环境要求：
1.	Azure ATP 许可证。
2.	要访问 Azure ATP 门户，账户是租户的全局管理员或安全管理员，拥有对监视域中所有对象的读取访问权限。
3.	Azure ATP 传感器支持安装在运行 Windows Server 2008 R2 SP1（不包括 Server Core）、Windows Server 2012、Windows Server 2012 R2、Windows Server 2016（包括 Windows Server Core 但不包括 Windows Nano Server）、Windows Server 2019（包括 Windows Core 但不包括 Windows Nano Server）的域控制器上。
#### 实验说明：
Azure 高级威胁防护 (ATP) 是一个基于云的安全解决方案，可利用本地 Active Directory 信号识别、检测并调查针对组织的高级威胁、身份盗用和恶意内部操作。 Azure ATP 可以使 SecOp 分析员和安全专业人员能够在混合环境中检测高级攻击，以便：
1.	使用基于学习的分析监视用户、实体行为和活动
2.	保护存储在 Active Directory 中的用户标识和凭据
3.	识别并调查整个杀伤链中的可疑用户活动和高级攻击
4.	提供关于简单时间线的明确事件信息，以进行快速会审
在本次实验中，目的在于建立一个Azure ATP实例，通过该实例可以管理AD林。
#### 实验步骤：
1.	创建实例
转到Azure ATP门户，使用Azure Active Directory账户（必须是全局管理员或者局管理员和安全管理员）进行登录。点击“创建”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-1.jpg)
2.	第一次登录打开 Azure ATP 门户时，需要提供用户名和密码以连接到Active Directory林。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-2.jpg) 

需要输入的信息要求如下所示:

| 字段 | 注释 |
| ---- | ---- |
| 用户名（必需） | 输入只读的 Active Directory 用户名。 例如：ATPuser。 必须使用本地 AD 用户帐户。 请勿使用 UPN 格式作为用户名。 |
| 密码（必需） |	输入只读用户的密码。 例如：Pencil1。 |
| 域（必需） | 输入只读用户的域。 例如 contoso.com。 必须输入用户所在域的完整 FQDN。 例如，如果用户的帐户所在的域为 corp.contoso.com，则需输入 corp.contoso.com 而非 contoso.com |

![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-3.jpg)  


3.	在 Azure ATP 门户中，单击“下载传感器安装程序并安装第一台传感器”以继续。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-4.jpg)  

a)	单击“下载”。

b)	将程序包保存到本地。从 zip 文件中提取安装文件。 直接从 zip 文件中安装将失败。运行“Azure ATP Sensor Setup.exe”并按照安装向导执行操作 。在“欢迎”页中选择语言，然后单击“下一步”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-5.jpg)  
c)	该安装向导自动检查服务器是域控制器还是专用服务器。 如果是域控制器，则安装 Azure ATP 传感器。 如果是专用服务器，则安装 Azure ATP 独立传感器。例如，对于 Azure ATP 传感器，会显示以下屏幕，提示将在专用服务器上安装 Azure ATP 传感器（如果域控制器或专用服务器不符合安装的最低硬件要求，你会收到一条警告。 该警告不会妨碍你单击“下一步”继续进行安装 。 如果是在不需要太多数据存储空间的小型实验室测试环境中安装 Azure ATP，这仍是正确的选择。 对于生产环境，强烈建议使用 Azure ATP 的容量规划指南，确保域控制器或专用服务器符合必要的要求。）：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-6.jpg)  

d)	在“配置传感器”下，根据环境输入从上一步复制的安装路径和访问密钥 （但是安装路径和exe的存储路径中不要有中文，否则会报错）。复制“访问密钥”。 Azure ATP 传感器需要访问密钥才能连接到 Azure ATP 实例。 访问密钥是用于传感器部署的一次性密码，此后所有通信均使用供身份验证和 TLS 加密的证书执行。 如果需要再生成新的访问密钥，可使用“再生成”按钮；该按钮仅用于传感器的初始注册，不影响以前部署的任何传感器。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-7.jpg)  
e)	单击“安装”。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-8.jpg)  
f)	回到Azure ATP门户中，可以看到，传感器下已经配好了一个实例，到此Azure ATP实例即创建成功，可以继续进行Azure ATP的相关配置了。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL6-9.jpg) 

 
