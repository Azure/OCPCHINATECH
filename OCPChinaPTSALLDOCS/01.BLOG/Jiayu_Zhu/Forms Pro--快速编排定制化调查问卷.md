作为Office 365全家桶里的小弟，Forms就像一个沿途不经意间所看到的美景，总是在人不抱有任何预期的时候，给人以意想不到的惊喜。
从最初发现可以很方便的生成各类不同方式的问题，统计公司内部的需求，到实时生成各种不同类型的统计，所见即所得地导出你所需要地统计结果。一站式的提供了你在制作问卷中所需要的元素。到现在全家桶中又把Forms做了升级，现在提供了Form Pro的preview，进一步满足大家对于问卷制作中的需求：
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%201.jpg)

    如果已经使用了global的office 365，可以通过以下的链接获取预览版进行试用：
https://formspro.microsoft.com/en-us
Forms Pro相对于Forms标准版最亮眼的提升就在于，您可以按照您所需要的需求，定制化您所需要的表格。例如：您需要给公司内部不同职级的员工进行定制化的问题提问，但同时又希望通过一张问卷完成所有的反馈，而不再是为了很小一部分客制化的问题，而重复的相似制作表格，这样后期的反馈统计及总结就会比较繁琐。
正是为了应对以上的需求，Forms Pro添加了“分支规则”这一功能，来让你轻松克制你的问卷，轻轻松松就能通过同一张问卷完成不同维度的调查。接下来我们就来通过以下的场景来演示表格制作的整个过程：
公司在举办完年度晚会后，需要搜集不同职级的员工对于晚会的满意度调查，从而能够更精确的搜集到更精准，更容易执行的改善方案。例如针对公司CXO级别的领导，如果有不满意的地方，希望他们从他们的角度提供可行的改善方案；或者是从经理的角度，代表各自的部门给出意见；当然所有参与员工，也可以从自身的感受上提供建议。
针对这一需求，我们来一起制作一份满意度调查问卷。首先，我们自然跟使用普通的Forms一样，按文本，选择，多选等方式罗列出所有涉及到的问题：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%202.jpg)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%203.jpg)

     这里，我们暂且先列出CXO这个选项所触发的所有问题，即问题 1 ，问题 2 ，问题 5 。触发逻辑则是，当问题 1 中的回答为CXO，则显示问题 2 ，隐藏问题 3 及 4 ；如果问题 2 的答案为“不满意”，则显示问题 5 ，否则就让用户触发提交问卷作为结束。
    需要注意的是，对于问题 1 之后所有的后续问题，逻辑上应该都是用户在拿到的第一时间是不可见的，因此再添加问题的时候，需要将该问题，设置为“不可见”。
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%204.jpg)

    接下来，我们就需要按照之前的逻辑来定义分支规则，点击“分享”右边的“…”，选择分支规则：
    
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%205.png)

    点击创建规则：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%206.jpg)

    对你所创建的规则进行命名，这里，你所创建的每一条规则对应给到客户的就是一份全新的问卷的概念。例如在我们的场景中，CXO其实会先后看到三份问卷，第一份只包含问题 1 ，第二份是由特定条件触发的包含问题 1 及问题 2 ，第三份则是在特定条件下所触发的包含问题 1 ，问题 2 及问题 5 的问卷。因此这个示例中将会需要建立五个规则对应五份不同的问卷。
       上述图中的逻辑，就是当问题 1 的答案选择为“Manager Level”，则会将默认隐藏的问题 3 “作为公司Manager，您对晚会是否满意”显示出来。
       
 ![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%207.jpg)

        以此类推，对于问题 1 ，需要建立三个规则对应用户不同的回答。
        设置完毕后，我们回到问卷进行预览：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%208.jpg)
    如预期的一般，所有人看到的问卷的一开始只会看到一个问题，即问题1：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%209.jpg)

        可以看到，当选择职责为CXO是，则会跳出带有CXO关键词的问题2。
        接下来，我们继续把问题 2 触发问题 5 的逻辑创建对应的分支规则：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%2010.jpg)

        在实际设计中，您也可以选择“添加条件”来定义更为复杂的逻辑，比如只有在问题X和问题Y分别选择不同的答案的情况下，才会触发显示某一个问题的方式来设计分支规则。这里，我们只需要一个条件就可以完成触发：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%2011.jpg)

        完成后，我们继续回到问卷进行预览，可以看到针对职责选择为CXO的整个问卷，可以很流畅的进行逻辑推进供相关人员作答：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%2012.gif)


        在设计完问卷后，则需要选择不同的方式分享给用户，那在公司中，最常见的就是通过邮件方式进行发送，另外，在会议场合，可能二维码会更适合现场人员进行使用，此外，有些网站或者公司的业务系统中也会面临需要嵌入的情况。这些场景，其实都能够很方便的通过“SendSurvey”这边轻松完成整合：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%2013.jpg)

        例如，我们如果选择通过“电子邮件“的形式进行发送，Forms就能自动生成一个邮件的模板，您只需填写对应的收件人，就能一键完成发送：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%2014.jpg)


        员工收到以后，就能通过链接，方便的完成问卷：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%2015.jpg)

        当收件人完成问卷以后，问卷发起人就可以一如既往的进行统计结果的查看：
        
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Forms%20Pro--快速编排定制化调查问卷%2016.jpg)

    除了智能的解析之外，Forms还会根据每个用户的完成度及结果，给出NPS（Net Promoter Score），即净推荐值这个市面上较为流行的顾客忠诚度分析指标，来辅助市场调查问卷进行统计及分析。
     以上便是一个简单的通过Forms Pro完成用户所需要的高度客制化的调查问卷，此外，您也可以再此基础上深入使用更多的辅助功能，例如再问卷中引入变量，加入到你的问题中，或者使用Flow或者嵌入等方式将问卷分发到不同的系统或者网页中。
       只要每天几分钟，哪里不会点哪里，就能够迅速成为高阶的市场调研选手，赶快行动吧。
