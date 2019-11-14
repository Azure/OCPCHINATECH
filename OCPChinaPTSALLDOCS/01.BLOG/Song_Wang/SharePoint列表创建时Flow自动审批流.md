通过blog：https://www.cnblogs.com/wangsongshare/p/10609547.html 大家已经了解到创建列表如果自动发送邮件，那么收集合作伙伴的相关材料需要后台人审核，这个也可以自动实现提醒批复，设置Approved/Reject邮件格式进行审批，因为只有O365国际版中有flow功能，所以如下操作使用flow演示。

1. 点击Flow，然后去flow的界面新建一个
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8101.png)

2. 因为自动审批，所以从空白创建

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8102.png)

3. 给自己的Flow定义一下名字，然后选择相关的功能

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8103.png) 

4. 根据SharePoint站点，选择自己已经创建的列表名称

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8104.png)

5. 选择创建一个审批流

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8105.png)

6. 如下选择对应信息，选择审批人和格式

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8106.png)

7. 然后点击下一步condition
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8107.png)

8. 点击Response是Approve，当yes的时候，自动发送邮件通知相关人员，并且更新SharePoint列表

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8108.png)

9. 发送邮件，可以设置格式内容，然后更新列表，并且把Approved Status那列置成：Yes，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8110.png)

10. 如果是Reject，会自动抓取到审批人给的comments
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8111.png)

11. 此时，自动审批流创建完成，创建case后，审批人会收到邮件，如下是reject+comments
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8112.png)

12. 当批复完成后就会自动收到如下邮件，同时站点列表同步更新comments

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SharePoint%E5%88%97%E8%A1%A8%E5%88%9B%E5%BB%BA%E6%97%B6Flow%E8%87%AA%E5%8A%A8%E5%AE%A1%E6%89%B9%E6%B5%8114.png)


 
