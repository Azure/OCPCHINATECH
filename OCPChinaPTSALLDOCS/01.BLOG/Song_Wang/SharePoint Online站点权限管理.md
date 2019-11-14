通过blog：https://www.cnblogs.com/wangsongshare/p/10609357.html 大家已经了解到如何添加和给外部用户分享SharePoint Online站点，但是对于分享的外部用户权限如何定义，是否存在数据泄露的风险，能否禁止已分享的客户的分享权限，这一篇blog给大家详细介绍。

1. 创建网站站点的时候一定要选择Private，如果Public，组织内的所有成员将都可以访问，public站点适合公共资料分享

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8601.png)

2. 点击“网站集”和“立即试用”进入新的管理界面，可以看到对于站点有四种选择，因为21v版本不能够直接添加外部活动用户，所以一般分享指定外部用户都是选择第二种：新的和现有来宾，如果此网点要求对所有外部用户公开，那就设置为第一种：任何人，这样所有人都能访问到站点。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8602.png)

3. 接下来进入站点权限管理，点击“访问请求设置”

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8603.png)

4. 点击后会弹出，如果将第一项“允许成员共享网站以及个别文件和文件夹”，如果勾选此项，你所分享的用户将没有权限分享给站点成员外的其他用户

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8604.png)

5. 如果分享给外部用户，将看到如下错误，第一个是外部用户，第二个是组织内的用户，都没有权限分享
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8605.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8606.png)

6. 如果为站点成员，就可以直接找到对应联系人分享
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8607.png)

7. 在管理中可以把各站点的信息自定义添加，这样可以直接看到哪些站点是可以共享的

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8608.png)

8. 该站点访问记录，可以通过右上角站点使用情况进行访问，如下图距离没有外部用户访问，所以没有记录

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8609.png)

9. 站点权限用，如果误操作或者在使用过程中，可以随时修改访问用户的权限，甚至移除该用户。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%8610.png)
