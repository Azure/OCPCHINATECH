在我们看完如果通过DLP，ATP，防钓鱼等安全保护功能后，我们来接着看下监视中十分重要的一环，“响应DSR”。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9401.webp)

这一环十分重要的原因在于，根据一般数据保护条例 (GDPR)，用户（在条例中称为“数据主体”）有权管理由雇主或其他类型机构或组织（称为“数据控制者”或简称为“控制者”）收集的个人数据。其中数据主体有权对自己的个人数据执行以下操作：获取个人数据副本、请求更改个人数据、限制个人数据处理、删除个人数据或接收电子格式个人数据（以便于转移给其他控制者）。数据主体为了对自己的个人数据执行操作而向控制者发出的的正式请求，称为“数据主体请求”(DSR)。控制者有义务及时审议各个 DSR，并提供实质性响应，具体是通过执行所请求的操作，或解释控制者为什么无法接纳 DSR。控制者应咨询自己的法律或合规性顾问，商讨如何妥善处置任何来自数据主体的请求。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9402.webp)

这里将会是以后公司管理所有来自数据主体请求的门户，我们紧接着尝试来新建一个数据查看的请求，点击“新建DSR案例”：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9403.webp)

再填写完毕名称后，需要选择具体的数据主体。从公司角度出发，这里的数据主体自然是针对公司内部的任职人员，不论是出于监管部门的抽查要求，还是数据主体自身的要求，这都将成为GDPR生效后的企业常规合规操作之一：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9404.webp)

再选择完毕数据主体后，就可以查看该数据主体存在于企业Exchange 电子邮件和公共文件夹、Skype 和 Teams 对话、微软待办任务、MyAnalytics、SharePoint 和 Teams 网站以及 OneDrive 帐户中的数据了：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9406.webp)

点击“显示搜索结果”以后，将会把这个请求通过设置对应的查询逻辑和范围，到Office 365中的“核心电子数据展示”（eDiscovery）中生成查询：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9407.webp)

可以看到目前针对我个人的账号，他把所有参与人，或者创作者为我作为关键字进行查询，查询数据的类型定义为针对电子邮件，文档和即时消息这三块。查询位置目前有以下这些模块是可选的：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9408.webp)

那针对一个来自公司的外部用户的请求，我们也可以通过“核心电子数据展示”（eDiscovery）来完成搜索。比如，您可以将用户的个人可识别信息，比如身份证号，驾驶证号等这些唯一可识别的号码作为关键词，并根据数据主体的需求，添加对应的条件：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9409.webp)

首先关键词可以根据对应的数据类型进行逻辑设计。其次，你也可以通过设定对应的查询条件来对应数据主体的具体需求。再得到整个完整的查询结果后，您可以选择直接导出到文件，将这个标准化的查询内容交给数据主体。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9410.webp)

另一方面，企业除了需要应对来自数据主体的请求，还需要在特殊的时刻，例如可能发生数据泄露的情况下，给到数据保护机构或相关单位事故的情况。这样的情况，也可以通过GDPR工具箱中的“响应法律调查”这个入口来完成。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9411.webp)

同样的，这里的查询请求也是通过电子数据展示来完成的：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9412.webp)

在创建好服务案例以后，就会被导航来到“核心电子数据展示”的界面中：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9413.webp)

这里，您就可以根据您的需要设置新的搜索项以及对应的保留项。我们先来看下如何设置保留项，首先点击“保留”，进入到添加保留案例的界面：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9414.webp)

取完名字后，针对Exchange邮箱或者Sharepoint站点，您可以选择需要针对保留的用户，组或者是网站：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9415.webp)

在选定需要保留的对象和范围后，我们接下来需要定义需要保留的具体内容和内容的类别：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9416.webp)

这里，我们可以通过最直接的设定需要保留内容的关键信息作为搜索的最直接的索引词。您可以指定关键字、 消息属性或文档属性，例如文件的名称。您还可以使用布尔运算符，例如AND、 OR，或NO来创建更复杂的查询。

当然您也可以针对需要保留的类别来做进一步的定位，比如指定针对的具体的收件人，发件人，或者是某一个主题。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9417.webp)

当然，您也可以选择添加多个条件来更精确的完成整个搜索：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9418.webp)

最后在确认您创建的查询的逻辑和条件符合您的需求，点击“创建此保留项”即可。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9419.webp)

而在接下来建立搜索的环节，就可以参考上文提到的响应DSR的搜索过程，不同点在于，你可以进行引导师搜索或者按ID列表进行搜索，其中引导式搜索就是把旧版的搜索界面从逻辑上做了改良，提供给用户可以按步骤进行设定的环节，比如先选择搜索区域，再填写关键词，最后添加条件之类的；按ID列表搜索则可以允许用户上传CSV路径，可以直接把对应关键词中的变量进行导入，一键完成搜索的设定：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9420.webp)

再建立完搜索后，您可以选择将整个搜索结果导出成CSV文件，给到有需要的同事或者用户。

另外，为了提高用户更好的理解微软中所存储的数据，提高电子数据展现的效率，我们在更高级的Office 365套包中，提供了高级电子数据展示。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9421.webp)

通过高级电子数据展示，企业可以对搜索出的数据进行冗余信息的剔除，之后可以对搜索出的整个数据集进行分析，甚至在搜索过程中，高级电子数据展示可以实现从图片中提取出文字来与关键词进行匹配的功能。鉴于篇幅的原因，这次不便拉开进行具体的介绍。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Microsoft%20365%20GDPR%20%E4%BB%AA%E8%A1%A8%E6%9D%BF%E4%B8%BA%E4%BC%81%E4%B8%9A%E5%87%BA%E6%B5%B7%E4%BF%9D%E9%A9%BE%E6%8A%A4%E8%88%AA%20%E7%B3%BB%E5%88%97%E5%9B%9B--GDPR%E5%B7%A5%E5%85%B7%E7%AE%B1%E4%B9%8B%E5%93%8D%E5%BA%9422.webp)

今天，我们通过GDPR面板中的“响应DSR”以及“响应法律调查”这两个功能，利用电子数据展示，完成了应对企业内部来自数据主体的请求以及来自比如第三方机构的合规检查。再下一篇中，我们会继续从“监视及响应”的部分再接着做介绍。


