通过blog：https://www.cnblogs.com/wangsongshare/p/10609451.html 大家已经了解到如何添加和给外部用户分享SharePoint Online站点和进行权限管控。接下来给大家介绍SharePoint站点中另一个特别方便的收集信息统计的工具：列表功能，站点管理员可以在后台定义收集相关数据的格式，选项、数字、Yes/No，Link，图片等，直接利用SharePoint站点收集，将极大的提高Operation效率，不用再一封封邮件分别统计汇总。

1. 在站点Home页，然后点击新建列表

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE01.png)

2. 创建完成后，进入列表，然后点击右上角“设置”按钮，进入“List Setting”界面，这里注意，只有点击进入该列表界面，才能显示出列表设置，如果没有显示，请refresh一下界面

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE02.png) 

3. 进入列表设置界面，可以在此界面定义列表，虽然大家发现在列表首页，可以自己添加列，但是还是要进入此页面设置，因为只有在列表设置界面创建“列”，才有选项“默认添加到列表”，否则可能出现你添加了列表，但是界面并没有显示，需要按照Best Practice去做。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE03.png)

4. 接下来向下拉进行列的创建，此项列表的目的为了让合作伙伴提交case信息，信息里包含了合作伙伴名称，客户名称，销售和技术，相关文档证明资料的link，这里按照顺序依次创建，虽然最下方有设置order的顺序，但是还是建议大家一次性设置完按次序创建，因为创建完再调整顺序不一定会立刻生效，对工作效率产生了影响。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE04.png)

5. Title这一个是系统默认自带的第一列，默认是单行文本，因为有客户list，所以选择“choice”，将此列设置为必填列，将客户列表对应填上去，每个客户一行，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE05.png)

6. 如下就是刚才提到的添加到默认视图，只有勾选才会默认出现在列表视图中，如果直接添加，有可能已添加，但是页面看不到。确认后

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE06.png)

7. 按照如下方式，可以根据需求选择Choice和日期还有link，关于URL的添加我给大家强调一下，如果大家的link很少，那就可以选择“Hyperlink/Picture”模式，但是这种link中字符最大250个

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE07.png)

8. 大家知道SharePoint的link一般都特别的长，会超过此限制，这种情况下就会需要多行文本模式添加URL，如下流程。在列表页面，新加case时候会出现如下界面，这个就是我们自定义的列，让合作伙伴提交信息，点击POE Link右侧的编辑按钮

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE08.png)

9. 进入如下界面，然后右击鼠标，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE09.png)

10. 右击鼠标后，会自动弹出如下“Insert”，点击“Link”，输入名字和网站地址，点击保存
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE10.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE11.png)

11. 然后回到“Edit”，点击保存，就添加完成了。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE12.png)

12. 一个case填写完成后点击save就可以了。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE13.png)

13. 最后可以统一导出相关case列表，点击如下，会有一个query，点击打开，注意：此时能够打开此query的用户也必须是该列表的成员或者已经具有权限的外部用户，负责是打不开的，侧面应证了O365权限管理的优势，时时刻刻保护数据。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE14.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%20Online%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E8%AE%BE%E7%BD%AE15.png)

14. Excel另存为本地就可以转换成自己的Excel文件了。
