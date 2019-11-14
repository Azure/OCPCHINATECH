通过blog：https://www.cnblogs.com/wangsongshare/p/10609518.html 大家已经了解到如何创建列表，因为收集信息，需要后台审核，当合作伙伴创建一个case时候，会自动发送邮件，并抓取列表中附件作为邮件附件一并发送给该客户相关负责人，确保所有人第一时间能够知道交流信息，便于下一步的根据。抓取附件没有相关的文档，我自己看了flow相关论坛，根据论坛上的一些解决方案尝试的，最后成功了，供大家参考。因为只有O365国际版中有flow功能，所以如下操作使用flow演示。

1. 点击Flow，然后去flow的界面新建一个

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B601.png)

2. 因为需要抓取附件，所以从空白创建，Flow有很多模板，一般基本的功能用模板可以使用，不用单独创建

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B602.png)

3. 给自己的Flow定义一下名字，然后选择相关的功能
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B603.png)

4. 根据SharePoint站点，选择自己已经创建的列表名称

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B604.png)

5. 我们选择了当列表创建时候会发送邮件，但是需要发送邮件前抓取附件，选择添加Step

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B605.png)

6. 选择list信息，如果没有ID这个内容，点击“see more”

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B606.png)

7. 然后点击添加：get attachment content，
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B607.png)

8. 固定格式填写ID和id
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B608.png)

9. 这样就获取到了附件的内容，点击add an action，发送邮件

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B609.png)

10. 邮件中可以定义发件人和收件人，邮件正文的格式内容，注意把附件内容添加上，如下格式
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B610.png)

11. 点击保存，一个邮件流就创建完成了，当在站点里创建一个case后，会自动收到如下邮件。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Flow%E8%87%AA%E5%8A%A8%E6%8A%93%E5%8F%96SharePoint%E7%AB%99%E7%82%B9%E5%88%97%E8%A1%A8%E5%B9%B6%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E5%92%8C%E9%99%84%E4%BB%B611.png)
