Office 365 作为一款SaaS服务，能够开箱即用的给到客户所需的各项协作产品的功能的同时，提供给了客户一系列安全的保障，例如，客户在使用邮箱服务时，就同时享受了国际顶尖的邮箱防钓鱼及垃圾邮件过滤等服务。

然而作为一款SaaS服务，有些企业可能会出于自身的一些企业规章制度，也会对SaaS产品之外提出一些额外的定制化要求。例如对于公司中的所有来往邮件，需要进行本地化管控；或者企业由于自身或行业的一些要求，需要在使用世纪互联版本的Office 365 的同时，希望能够拥有Global Microsoft 365中诸如EMS服务级别的安全性功能。这些要求，可能企业会误认为Office365作为一款成熟的SaaS产品。可能无法做到自定义的扩展。那因此，本文就希望通过介绍一个Office 365 中的邮箱服务与本地赛门铁克的本地产品相结合的一个解决方案来供大家参考，来满足企业中的一些特定要求。

那在具体来看方案，大家可能会对连接器这人还比较陌生，其实他是Office365中邮箱服务上的一个增值服务，由ExchangeOnline Protection这款产品SKU提供，包含与Exchange Online Plan 2中及企业版E3套包中。它其实是为用户提供了一个自定义进出Office365企业级邮箱邮件流的接口，比如可以用于跟组织内部部署的邮件服务器或者企业自身的业务合作伙伴或服务提供商之间的邮件交换。

最常用的一个场景就是企业在做邮箱的混合部署中，其中一种标准的做法就是部署连接器，来实现公司内部分属于云端和本地的这两部分用户之间的邮件交换。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87Exchange%20Online%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8%E5%AE%9E%E7%8E%B0%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1%E6%9C%AC%E5%9C%B0%E7%AE%A1%E6%8E%A701.webp)

而另外一个使用方法就是：连接外围设备，来做企业级邮箱的安全管控。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87Exchange%20Online%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8%E5%AE%9E%E7%8E%B0%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1%E6%9C%AC%E5%9C%B0%E7%AE%A1%E6%8E%A702.webp)

上图中方案就通过Office 365云端的连接器与本地的赛门铁克的Messaging Gateway相连接，对接客户本地的统一监控平台；此外还可以如方案中所示，再与赛门铁克的DLP平台进行协作，来对邮件内容进行检测，看是否与公司相定义的安全策略或敏感等级相关，来执行对应的响应动作如记录，警告，审批，或者拦截邮件等。如果邮件通过了DLP的验证，则继续返回到网关设备，根据MX记录发送到互联网。

类似的操作也同样适用于从internet发到公司的邮件，但入站的邮件自然不会经过DLP平台做内容管控。需要注意的是，在配置阶段，公司需要在域名托管商添加除了Office 365之外的另一个指向赛门铁克Messaging Gateway公网地址的MX记录，并将其优先级设为较高的那个。

接下来我们来看下，如何在Office 365端配置传出连接器及创建规则。

首先，需要通过管理员登录到Exchange管理中心，点击邮件流，选择添加连接器。并把邮件流指向本地服务器。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87Exchange%20Online%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8%E5%AE%9E%E7%8E%B0%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1%E6%9C%AC%E5%9C%B0%E7%AE%A1%E6%8E%A703.webp)

之后给连接器取名，并选择下图中的选项一来使用连接器，即将邮件重新定向到此连接器的方式。 

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87Exchange%20Online%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8%E5%AE%9E%E7%8E%B0%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1%E6%9C%AC%E5%9C%B0%E7%AE%A1%E6%8E%A704.webp)

之后需要您指定邮件的路由目的，这里将您本地赛门铁克的消息网关的IP地址作为智能主机添加到下图中：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87Exchange%20Online%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8%E5%AE%9E%E7%8E%B0%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1%E6%9C%AC%E5%9C%B0%E7%AE%A1%E6%8E%A705.webp)

之后根据您的情况来添加证书来启用TLS保护传输中的数据，这里可以选择自签名证书。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87Exchange%20Online%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8%E5%AE%9E%E7%8E%B0%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1%E6%9C%AC%E5%9C%B0%E7%AE%A1%E6%8E%A706.webp)

之后确认各项配置正确，点击“下一步”就完成了连接器的设置。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87Exchange%20Online%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8%E5%AE%9E%E7%8E%B0%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1%E6%9C%AC%E5%9C%B0%E7%AE%A1%E6%8E%A707.webp)

此外本地端赛门铁克的消息网关和其他配套软件的设置请咨询赛门铁克的技术人员。
