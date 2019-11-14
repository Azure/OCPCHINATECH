[Dynamics 365的市场营销](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/marketing/overview)是一个丰富的应用程序, 以支持您的营销自动化目的。您可以构建客户旅程、细分、电子邮件、访问页、活动等。

Dynamics 365 还可以收集有关个人访问者如何使用您的网站的信息。为了启用该功能, dynamics 365 生成您必须添加到要监视的每个页面的 javascript 代码 (通常管理员会使用 cms 系统在站点范围内执行此操作)。跟踪功能与丰富的[构建细分](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/marketing/create-segment) 能力为营销提供的 dynamics 365 为一个有用的自动化场景打开了-构建重复网站访问者的动态细分。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8601.jpg)

在本博客中, 我们将在网站上设置跟踪, 并构建一个片段来捕获重复访问者。

 

# 设置跟踪

1. 将您的联系人访问的网站的 url 复制到剪贴板

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8602.jpg)

2. 导航到Marketing -> Websites并创建一个新的网站记录
3. 将剪贴板的 url 粘贴到Url字段 (1) 和命中 Save 生成跟踪脚本 (2)
4. 将跟踪脚本复制到剪贴板
5. 请注意网站记录的 url, 尤其是右侧 (3) 的 id--在设置段时, 您需要该 url

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8603.jpg)

6. 导航到您的联系人访问的网站的管理界面 (1)
7. 打开Header(2) 本网站
8. 将跟踪脚本粘贴到标头的Header (3)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8604.jpg)

# 建立部分

1. 导航到Marketing -> Segments并创建一个新的细分市场
2. DESIGNER 选项卡选择 Contact(1) 然后Link between WebsiteVisited interaction and contact(3)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8605.jpg)

3. 指定条件Having count (1) 和Sliding window(2), 分别访问了多少次, 在什么时期。我将使用大于零的第一个只是为了演示的目的 (如果段是一个真正的重复游客段显然, 我会使用更大的一个Having count)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8606.jpg)

4. 选择WebsiteVisited字段 (1), 然后是websiteid属性 (2)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8607.jpg)

5. 将上述SET UP TRACKING bullet #1的网站记录 id 粘贴到值字段 (1) 中

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8608.jpg)

6. Save, Check for Errors和 Go Live细分-细分暂时为空

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8609.jpg)

# 要测试

1. 打开另一个浏览器
2. 登录到例如作为用户在市场营销中匹配联系人的邮件
3. 在浏览器中打开新选项卡
4. 从上面访问网站

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8610.jpg)

5. 现在导航到Marketing -> Segments并验证是否按预期添加了新的细分成员

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8611.jpg)

6. 为什么它的值得-您还可以导航到联系人, 并验证网站访问是跟踪联系人

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%A6%82%E4%BD%95%E5%9C%A8Dynamics365%E4%B8%AD%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E9%87%8D%E5%A4%8D%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE%E8%80%85%E7%9A%84%E5%B8%82%E5%9C%BA%E7%BB%86%E5%88%8612.jpg)

因此, 现在您已经了解了如何跟踪网站访问并基于这些内容构建细分。你可以有一个动态的细分就在那里, 只是等待联系人访问你网站, 然后通过客户之旅采取自动化行动。

说明：（本博客引用自Microsoft Lystavlen的文档。）
