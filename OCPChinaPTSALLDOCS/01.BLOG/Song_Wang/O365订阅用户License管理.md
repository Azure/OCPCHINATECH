对于很多O365大客户，可能拥有几百，几千甚至上万坐席数 ，对于IT运维，这将是很大的工作量，今天给大家介绍一个方便实用的小工具可以统一管理所有用户，包括分配License，导出用户等很多操作，尤其是买了几千坐席需要批量分配license的时候，并不是每个客户都会使用powershell进行操作，所以UI界面会让IT运维事半功倍。

如下给大家介绍，如何安装使用Office 365 License Reporting and Management Tool 这个工具。这个文档仅仅介绍O365管理，Exchange，Hybrid，Sharepoint on premise都是可以管理的。

一． 安装

1. 建议直接开一台新的winserver机器，已经测试没有问题。

2. https://gallery.technet.microsoft.com/office/Office365-License-cfd9489c ，进入网站直接下载，这是第三方工具，该工具并非微软开发，因此没有独立的技术支持。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8601.png)

3. 根据测试，该工具与新版本的Windows Azure Active Directory Module for Windows PowerShell无法兼容。需要安装老版本的AAD Module。

4. 老版本的AAD module可以同时支持国内和国际版O365管理员账号，如果是国际版，那工具可以下载使用，不需要在安装老版本AAD模块。这一点需要注意。

5. https://bposast.vo.msecnd.net/MSOPMW/Current/amd64/AdministrationConfig-EN.msi ，点击直接下载老版本AAD module，可以同时支持国际国内版本。直接点击可以会提示错误，没有安装Microsoft  Online Services Sign-In Assistant，https://www.microsoft.com/en-my/download/details.aspx?id=39267 ，直接点击安装即可

6. 安装完成后就可以直接打开就可以使用
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8602.png)



二． 使用

1. 直接打开就会有登录界面，也可以从如下界面登录，输入管理员账号密码即可

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8603.png)

2. 登录完成过后点击Generate就可以形成report，可以下载到本地

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8604.png)

3. 分配license，弹出来的窗口点击“+”，选择从report里导入用户
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8605.png)

4. 选择相应的用户，选择下一步
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8606.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8607.png)

5. 然后进入license分配窗口，该用户已经具有E3 License，可以看到，能分配的有PowerBI Pro等，对比下面是管理员界面截图，可以看出来信息是一致的。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8608.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8609.png)

6. 右下角点击update，就可以看到成功提示，就表示分配完成了。再点击进入查看，发现三个用户已经更新完成。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/O365%E8%AE%A2%E9%98%85%E7%94%A8%E6%88%B7License%E7%AE%A1%E7%90%8610.png)

三． 总结

如上介绍的是简单的使用，如果你有几千个用户需要更新，这样使用就会非常方便了。
