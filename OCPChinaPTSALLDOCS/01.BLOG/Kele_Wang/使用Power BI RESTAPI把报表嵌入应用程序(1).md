Power BI本身已经提供了很好的互动报表操作，但是在很多情况下我们会需要把报表嵌入到网页或者app里，和公司现有的办公应用集成在一起并且互相交互，这时候我们就可以通过SDK或者RESTAPI的方式在App里调用操作报表了。

Power BI目前提供C#的SDK已经封装好了可以直接调用。有兴趣的可以移步https://docs.microsoft.com/zh-cn/power-bi/developer/embed-sample-for-your-organization参考

其他语言没有封装好的SDK也还是可以使用Power BI RESTAPI来进行调用，本文主要使用测试工具Postman来进行RESTAPI的测试，一旦RESTAPI跑通了，后续的开发也就容易了。

# 在 Azure Active Directory (Azure AD) 中注册应用程序
要使用SDK调用Power BI, 首先我们需要一个 Power BI Pro 帐户（作为主帐户）和 Microsoft Azure 订阅。

* 如果未注册 Power BI Pro，请在开始之前注册以获得免费试用。
* 如果没有 Azure 订阅，请在开始之前先创建一个免费帐户。
* 你需要具有自己的 Azure Active Directory 租户。

首先我们需要在Azure AD里注册一个应用，并且赋上相应的权限。


1. 登陆http://portal.azure.com，找到Azure Active Directory

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)01.webp)

2. 点击新应用程序注册

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)02.webp)

3. 创建完成，依次如下图选择，设置，所需权限，添加

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)03.webp)

4. 依次添加如下权限

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)04.webp)

5. 新建一个密钥

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)05.webp)

这个时候我们的程序注册已经完成，接下来可以在Postman进行Rest API的调用了

# Power BI 用户OAuth2.0认证
要用RESTAPI访问我们的Power BI报表资源，首先要通过前面我们注册的应用程序在Azure AD上进行用户认证。AAD使用的认证方式是OAuth2.0，我们可以使用Postman来进行


1. 打开Postman， Authorization里面Type选择OAuth 2.0，点击Get New Access Token.

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)06.webp)

2. 填写相应信息，点击Request Token
Callback URL: http://localhost:15236 (要和前面在AAD注册应用的callback url一致)<br>
Auth URL: https://login.windows.net/common/oauth2/authorize?resource=https://analysis.windows.net/powerbi/api<br>
Access Token URL: https://login.windows.net/common/oauth2/authorize?resource=https://analysis.windows.net/powerbi/api<br>
Client ID: 前面步骤3图中的应用程序ID<br>
Client Secret: 前面步骤5中创建的密钥

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)07.webp)

获得了Access Token之后就可以进行Power BI RESTAPI的调用了

# Power BI RESTAPI调用
按照下图所示我们调用了https://api.powerbi.com/v1.0/myorg/groups 获取该用户下所有的workspace

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)08.webp)

# 把Power BI报表嵌入现有网页应用
首先需要获得报表的Group ID，登陆Power BI Pro，打开想嵌入的报表，下图URL里红圈内即为Group ID和Report ID(report id在后面有用).

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)09.webp)

使用 https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports 获得report的具体信息，记下embedUrl。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)10.webp)

接下来可以使用Power BI Javascript SDK来把报表嵌入html了。首先去https://github.com/Microsoft/PowerBI-JavaScript/releases 下载最新的release，在dist目录找到powerbi.js文件。按照下图建立文件把powerbi.js放到scripts目录，编辑pbiembed.html，修改对应的embedUrl和accessToken参数，用浏览器打开pbiembed.html即可看到报表成功嵌入了。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)11.webp)

```
<!DOCTYPE html>
<title>Power BI - Web sample</title>
<html lang="en">
<body>        
    <script type="text/javascript" src="scripts/powerbi.js"></script>
    <div id="reportContainer" style="width: 900px; height: 500px">
    </div>
    <script type="text/javascript">
    var embedUrl = "前面获得的EmbedURL" 
   
    // get the access token.
    accessToken = "前面获得的Access Token"

    var models = window['powerbi-client'].models;
    
    var permissions = models.Permissions.All;
    // Embed configuration used to describe the what and how to embed.
    // This object is used when calling powerbi.embed.
    // You can find more information at https://github.com/Microsoft/PowerBI-JavaScript/wiki/Embed-Configuration-Details.
    var config = {
        type: 'report',
        tokenType: models.TokenType.Embed,
        accessToken: accessToken,
        embedUrl: embedUrl,
        id: "03d9a889-c26c-4268-a2cc-91af00eb2ab8",
        permissions: permissions,
        settings: {
            filterPaneEnabled: true,
            navContentPaneEnabled: true
        }
    };

    // Grab the reference to the div HTML element that will host the report.
    var reportContainer = document.getElementById('reportContainer');

    // Embed the report and display it within the div container.
    var report = powerbi.embed(reportContainer, config);
    </script>
</body>
</html>
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E4%BD%BF%E7%94%A8Power%20BI%20RESTAPI%E6%8A%8A%E6%8A%A5%E8%A1%A8%E5%B5%8C%E5%85%A5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F(1)12.webp)

# 参考资源
https://docs.microsoft.com/zh-cn/azure/active-directory/develop/v1-protocols-oauth-code <br>
https://docs.microsoft.com/en-us/rest/api/power-bi/
