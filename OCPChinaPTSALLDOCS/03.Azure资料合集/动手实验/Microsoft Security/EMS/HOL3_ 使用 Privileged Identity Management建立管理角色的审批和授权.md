### HOL3: 使用 Privileged Identity Management建立管理角色的审批和授权
#### 前言：
本系列实验将引导用户完成O365 企业移动性和安全性（Enterprise Mobility Security）的常用操作和配置，本着实用性和安全性的原则，该系列实验会建议一些最佳实践。本系列实验主要分为以下几个阶段：
1.	将Azure AD 登陆和审核日志发送到Azure Monitor
2.	用户自助密码重设&条件访问策略强制用户使用MFA二次验证&启用标识保护配置风险检测
#### 3.	使用 Privileged Identity Management建立管理角色的审批和授权
4.	使用Intune 管理设备和移动设备
5.	使用Azure Information Protection 保护云中数据
6.	使用Azure Advanced Treat Protection保护混合环境的安全

#### 环境要求：
1.	O365企业版 E1/E3/E5(有O365国际版许可即可)；
2.	EMS E3/E5（部分用到E5的部分会做说明）；
3.	Azure订阅
#### 实验说明：
在一个企业环境中，通常管理角色分很多种，除了全局管理员，还有账户管理员，服务管理员，安全管理员，计费管理员等等管理角色的细分，当企业分支机构庞大，业务部门复杂起来之后，我们希望对这些管理角色的申请有一个监督过程，Privileged Identity Management（PIM）就是解决这个问题的，本篇实验将带你了解PIM的功能和设置过程。
#### 实验步骤：
实验开始前，我们仍然要顺着前面的习惯理一下现在的用户情况：
主要全局管理员：admin@M365n634099.onmicrosoft.com 
备用全局管理员：user0@M365n634099.onmicrosoft.com 
用户：meganb@M365n634099.onmicrosoft.com（属于组mfagroup）  
组：mfagroup@M365n634099.onmicrosoft.com 
本实验需要再创建一个用户julia@M365n634099.onmicrosoft.com,赋予她全局管理员权限和计费管理员权限。

1.	启用PIM，设置
全局管理员账户登录到https://portal.azure.com，搜索框搜索Azure AD Privileged Identity Management ，点击搜索结果，进入AAD PIM管理界面：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-1.png)
打开之后可能会检查你的身份信息，要求输入账号和密码及二次认证，按指示完成即可。完成后看到如下页面，点击【许可】。这一步是根据PIM服务的逻辑，先启用了该服务。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-3.png) 
启用服务后，PMIAzure AD 角色我的角色，如下页面，点击注册。这一步是PIM服务的注册逻辑：只有全局管理员有权限注册PIM服务角色，从而有资格去管理其他管理员角色的审核等流程。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-5.png)
PMI->Azure AD 角色->向导，点击【发现特权角色】
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-7.png) 
下图我们可以看到，这里罗列了当前活动目录中所有管理角色的数目和人员，与我们实验开始时设置的角色一致。【永久】和【符合条件】的区别：【永久】是长时间爵位，除非被贬为庶民，否则永远是爵，【符合条件】是认为你有这个资格，给你一个爵位的暂任券，你得亲自拿着这个暂任券来报道，阐明你能胜任的理由，准备在位的时间等等细节，老大觉着没问题，批准了，你就可以拿官印了，但是你在系统中的身份仍然是【暂任】。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-9.png) 
点击【全局管理员】，对于Julia这个用户，我们认为她做计费管理员没问题，有些时候她可能需要全局管理员的权限，有时候不需要，因此，我们把她从全局管理员的角色从永久设为【符合条件】，单击下一步，之后如下勾选：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-11.png) 
完成后可以看到如下结果，这样我们就把Julia同志转为暂任管理员了。 
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-13.png)
这时候别忘了备用管理员user0,虽然是备用，也应该拥有姓名，该有的权限不能少，因此我们这里把他添加为【特权管理员】：PIMAzure AD 角色 - 角色添加成员，如下选好角色，最后记得把他从【符合条件】提为【指定永久】。

授予用于管理 PIM 的访问权限：
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-15.png)   
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-17.png)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-19.png)
管理员侧操作完了，我们再从Julia的视角看下发生了什么。用Julia的账号登录portal后，在PIM我的角色Azure AD角色，因为被设置为“暂任”，如上面说过的，需要自己手动【激活】完成领“官印”的过程，如下点击【激活】，这里会要求你输入时间，理由等信息。这个信息页可以由管理员自定义设置需要填什么东西，先按下面图片操作完。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-21.png)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-23.png)
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-25.png)
最后我们讲一下上面提到的管理员自定义要求部分，以管理员账号登录Portal，PIMAzure AD角色设置角色，尝试自己对这些条目做一些设置，设置完之后再验证一下结果。
![image](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/03.Azure资料合集/动手实验/image/EMS%20HOL3-27.png) 
2.	定期审核这些角色
1)	按照https://docs.microsoft.com/zh-cn/azure/active-directory/privileged-identity-management/pim-how-to-start-security-review 中的步骤设置评审条目；
2)	完成评审：
https://docs.microsoft.com/zh-cn/azure/active-directory/privileged-identity-management/pim-how-to-complete-review 
参考文档：
https://docs.microsoft.com/zh-cn/azure/active-directory/privileged-identity-management/pim-how-to-change-default-settings 

