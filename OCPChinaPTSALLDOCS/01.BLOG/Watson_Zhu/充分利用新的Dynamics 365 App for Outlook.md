每个人都喜欢 Outlook。我们的日常沟通和规划大多发生在Outlook 中。有人认为, Outlook 是你在一天开始时打开的第一件事, 也是你在一天结束时关闭的最后一件事。

我们中的许多人还与业务关系 (客户、潜在客户、联系人、客户、等)每天都有.跟踪我们收到的电子邮件发送到我们的业务关系, 创建和更新潜在客户, 机会, 案例等。

它一直是非常调谐到 Microsoft 用户, 您可以直接在 Outlook 中使用 Dynamics 365 (crm)。毕竟, 这一天大部分时间都在这里度过。你哪一个 必须切换应用程序, 以完成您需要做的事情。应用切换非常耗时。

在许多年此功能由 com 外接程序处理-在最近几年中, 我们的建议是利用零足迹 Dynamics 365 的平板电脑和手机应用程序, 现在称为Dynamics 365 App for Outlook.

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2001.png)

随着新的统一用户界面(UI) 在 Dynamics 365 (crm) 中, 用户体验变得更好。新的 UI 性能高, 响应迅速, 并且非常用户友好.

Dynamics 365 App for Outlook利用新的UI。您可以从字面上使用最好的 Dynamics 365 (crm), 而无需离开 outlook。两全其美。

作为一个例子，点击刚刚在 Outlook 中收到的邮件, 然后单击Dynamics 365图标 (1) 中打开Dynamics 365 App for Outlook。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2002.jpg)

Dynamics 365 App for Outlook在右侧的任务窗格中打开 (您可以更改宽度此任务窗格, UI 将采用精美的新宽度)。

在本例中, 看到邮件被跟踪到商机 "社交参与" (1), 看到的是发件人的联系信息 (2)、账户信息 (3)-以及如果向下滚动或单击应用程序中的记录, 则更多信息。可以在 Outlook 中创建、读取、更新和删除记录和活动。

如果单击站点地图图标 (4)..。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2003.jpg)

...收到了应用程序的开箱即用 (OOB) 站点地图，那就可以导航到仪表 板(1)。那是它的 oob 网站地图。

当你开始使用应用程序时, 您可能需要更多的站点地图选项-例如能够轻松导航到 "客户"、"联系人" 和 "商机" 列表。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2004.jpg)

幸运的是可以非常直白地使用新的 PowerApps 应用编辑任何Dynamics 365 应用的站点地图。在这个博客文章的其余部分, 会告诉你如何在浏览器中打开Dynamics 365, 单击左上角的 "应用程序导航器" (1), 然后单击PowerApps (3)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2005.jpg)

在 " PowerApps " 中, 单击Apps(1), 单击Dynamics 365 App for Outlook(2) 然后编辑(3) 打开应用设计器

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2006.jpg)

在应用设计器中, 单击编辑图标 (1), 以打开网站地图设计器

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2007.jpg)

在站点地图设计器中单击Home(1), 点击 Components (2), 然后拖动Group(3) 到画布上 (4)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2008.jpg)

命名Group,例如"Sales", 然后将三个子区域 (2) 拖到画布上 (3)。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2009.jpg)

对于每个子区域指定 type = Entity并指出所需的实体 (例如客户、联系人和商机)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2010.jpg)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2011.jpg)

保存并发布自定义后, 返回到 Outlook 并再次打开Dynamics 365 App for Outlook。

现在在Sitemap (1) 中有了新的Group "Sales"。这个应用程序现在更适合我的日常工作任务。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2012.jpg)

我可以轻松地导航到例如中。My Active Accounts列表 (显示在网格中)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2013.jpg)

如果我减少的宽度Dynamics 365 App for Outlook任务窗格响应式 UI，可以很好地调整以显示卡片中的每个记录。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%85%85%E5%88%86%E5%88%A9%E7%94%A8%E6%96%B0%E7%9A%84Dynamics365AppforOutlook%2014.jpg)

这个不错的应用程序将增加你日常在Outlook工作的使用价值。
