# 概述

在Power BI报表服务器身份认证体系上，我们默认使用AD作为认证体系，AD即活动目录体系来说，是微软整个平台的核心，可以说是倚天剑。默认情况下， Power BI 报表服务器 接受指定 Negotiate 或 NTLM 身份验证的请求。 如果部署中包括使用这些安全提供程序的客户端应用程序和浏览器，则可以使用这些默认值，而无需附加配置。 如果要使用不同的安全提供程序来获取 Windows 集成安全性（例如，如果要直接使用 Kerberos）或者修改了默认值并且要还原原始设置。

但是很多用户不使用AD作为验证，希望用自己的认证程序来进行验证，比如使用数据库用户名和密码进行验证。 Power BI 报表服务器也支持自定义安全认证，这是一把屠龙刀，实现你对验证的无限需求 。

Power BI 报表服务器提供了可扩展的体系结构，该体系结构允许您插入自定义的或基于窗体的身份验证模块。 如果部署要求不包含 Windows 集成安全性或基本身份验证，则可考虑实现自定义的身份验证扩展插件。 使用自定义身份验证的最常见情形是支持对 Web 应用程序的 Internet 或 Extranet 访问。 使用自定义身份验证扩展插件替换默认的 Windows 身份验证扩展插件，可更好地控制如何授予外部用户访问报表服务器的权限。

利用 Power BI 报表服务器 安全扩展插件，可以对用户或组进行身份验证和授权；这样，不同的用户便可登录至同一台报表服务器，并基于他们的标识执行不同的任务或操作。 默认情况下，Power BI 报表服务器 使用基于 Windows 的身份验证扩展插件，该插件使用 Windows 帐户协议来验证声明在系统上拥有帐户的用户的标识。 Power BI 报表服务器 使用基于角色的安全系统为用户授权。 Power BI 报表服务器 基于角色的安全模型与其他技术的基于角色的安全模型类似。

因为安全扩展插件基于可扩展的开放式 API，所以您可以在 Power BI 报表服务器 中创建新的身份验证和授权扩展插件。 下面的示例为使用基于窗体的身份验证和授权的典型安全扩展插件实现：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8101.gif)

如图所示，身份验证和授权将按以下所示发生：

1. 用户尝试使用 URL 访问 Web 门户，然后被重定向至为客户端应用程序收集用户凭据的窗体。
2. 用户向该窗体提交凭据。
3. 用户凭据通过 LogonUser 方法提交至 Reporting Services Web 服务。
4. Web 服务调用客户提供的安全扩展插件，并验证相应的用户名称和密码是否存在于自定义安全机构中。
5. 进行身份验证之后，Web 服务创建一个身份验证票证（称为“cookie”），管理票证，然后为 Web 门户的主页验证用户角色。
6. Web 服务将此 cookie 返回至浏览器，然后在 Web 门户中显示相应的用户界面。
7. 对用户进行身份验证之后，在 HTTP 标头中传送此 cookie 的同时浏览器向 Web 门户发出请求。 这些请求用于响应 Web 门户中的用户操作。
8. 此 cookie 在 HTTP 标头中与请求的用户操作一起传送至 Web 服务。
9. 对此 cookie 进行验证，如果有效，则报表服务器从报表服务器数据库中返回安全描述符及与请求的操作有关的其他信息。
10. 如果此 cookie 有效，报表服务器将调用安全扩展插件检查用户是否有权执行特定操作。
11. 如果用户已有相应权限，则报表服务器将执行请求的操作，并将控制权返回调用方。
12. 用户经过身份验证后，报表服务器进行 URL 访问都会使用此 cookie。 此 cookie 在 HTTP 标头中传送。
13. 用户继续请求对报表服务器的操作，直到会话结束为止。

# 如何实现

Power BI 报表服务器 引入了一个新的 Web 门户以托管新的 Odata API，并也托管新的报表工作负载，例如移动报表和 KPI。 此新门户依赖于更新的技术，并通过在单独的进程中运行与熟悉的 ReportingServicesService 分隔开来。 此进程不是 [ASP.NET](https://dotnet.microsoft.com/apps/aspnet) 托管的应用程序，因此中断了现有自定义安全扩展插件中的假设。 此外，自定义安全扩展插件的当前接口不允许传入任何外部上下文，留给实现者唯一的选择来检查熟知的全局 [ASP.NET](https://dotnet.microsoft.com/apps/aspnet) 对象，这要求对接口进行一些更改。

引入了可实现的一个新接口，此接口提供一个 IRSRequestContext，提供扩展插件用于做出与身份验证相关决定的更常见属性。

在以前的版本中，报表管理器位于前端，并且可以使用其自定义登录页面进行配置。 在 Reporting Services 2016 中，仅支持 reportserver 托管的一个页面，并且应对两个应用程序都进行身份验证。

大多数泛型示例访问 HttpContext.Current 来读取如标头和 Cookie 等请求的信息。 为了使扩展插件能够做出相同的决策，我们在提供请求信息的扩展中引入了一个新方法，并在从门户进行身份验证时调用该方法。

扩展插件必须实现 [IAuthenticationExtension2]((https://msdn.microsoft.com/library/microsoft.reportingservices.interfaces.iauthenticationextension2(v=SQL.130).aspx)) 接口才能利用此方法。 扩展插件需要实现 [GetUserInfo](https://docs.microsoft.com/en-us/dotnet/api/microsoft.reportingservices.interfaces.iauthenticationextension.getuserinfo?redirectedfrom=MSDN&view=sqlserver-2016#Microsoft_ReportingServices_Interfaces_IAuthenticationExtension_GetUserInfo_System_Security_Principal_IIdentity__System_IntPtr__) 方法的两个版本，正如 reportserver 上下文所调用的方法，以及其他在 webhost 进程中所使用的方法。 以下示例展示了此门户的一个简单实现，其中使用了 reportserver 解析的标识。

```
public void GetUserInfo(IRSRequestContext requestContext, out IIdentity userIdentity, out IntPtr userId)
{
    userIdentity = null;
    if (requestContext.User != null)
    {
        userIdentity = requestContext.User;
    }

    // initialize a pointer to the current user id to zero
    userId = IntPtr.Zero;
}
```

# 配置部署和Demo

需要实现自定义扩展认证，需要有几个步骤。在github上有一个demo https://github.com/Microsoft/Reporting-Services/tree/master/CustomSecuritySample

如果你安装demo的步骤，数据库和Power BI 服务器在一个服务器上，那么基本上很简单就搞定，我在进行测试中遇到了几个问题，给大家分享下。

1、先下载此Demo 打开后，可以进行编译，如果不能通过，可能需要添加 Microsoft.ReportingServices.Interfaces 这可以在 C:\Program Files\Microsoft Power BI Report Server\PBIRS\PowerBI 目录下找到 Microsoft.ReportingServices.Interfaces.DLL进行引用

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8102.png)

2、对于需要对身份验证 Cookie 进行解密的窗体身份验证，需要使用相同的计算机密钥和解密算法对这两个进程进行配置。 所以我们需要生成一个强密钥和使用一些工具来生成密钥，例如 Internet Information Services 管理器 (IIS)。 在 Internet 上可以找到其他工具。

首先，使用 Visual Studio 开发人员命令提示符 来进行创建密钥

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8103.png)

打开后，跳转到需要的目录，如cd c:\test ,然后输入： sn -k SampleKey.snk

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8104.png)

生成的samplekey.snk需要和程序关联，点击应用程序的属性，选择签名，选择强签名密钥文件为刚生成的samplekey.snk

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8105.png)

3、生成密钥，生成密钥理论有很多方法实现，我的这台服务器安装了IIS 我使用IIS进行生成密钥，打开IIS 选择计算机密钥。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8106.png)

点击后选择 验证方法AES，加密方法AES。生成的密钥记录下来备用。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8107.png)

4、编译项目。生成相应的文件。部署项目：

* Copy the Logon.aspx 部署到 C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer 目录
* Copy Microsoft.Samples.ReportingServices.CustomSecurity.dll and Microsoft.Samples.ReportingServices.CustomSecurity.pdb to the C:\Program Files\Microsoft Power BI Report Server\PBIRS\ \ReportServer\bin 目录
* Copy Microsoft.Samples.ReportingServices.CustomSecurity.dll and Microsoft.Samples.ReportingServices.CustomSecurity.pdb to the C:\Program Files\Microsoft Power BI Report Server\PBIRS\ \Portal` 目录.
* Copy Microsoft.Samples.ReportingServices.CustomSecurity.dll and Microsoft.Samples.ReportingServices.CustomSecurity.pdb to the C:\Program Files\Microsoft Power BI Report Server\PBIRS\ \PowerBI` 目录.

5、修改 C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer\ RSReportServer.config

在 `<AuthenticationTypes>` 节下修改为

```
<Authentication>
	<AuthenticationTypes> 
		<Custom/>
	</AuthenticationTypes>
	<RSWindowsExtendedProtectionLevel>Off</RSWindowsExtendedProtectionLevel>
	<RSWindowsExtendedProtectionScenario>Proxy</RSWindowsExtendedProtectionScenario>
	<EnableAuthPersistence>true</EnableAuthPersistence>
</Authentication>
```

在元素中找到 `<Security>``<Authentication>``<Extensions>` 修改如下： 这里的username是管理员的名称，比如我这里设置为maxbiuser

```
<Security>
	<Extension Name="Forms" Type="Microsoft.Samples.ReportingServices.CustomSecurity.Authorization, Microsoft.Samples.ReportingServices.CustomSecurity" >
	<Configuration>
		<AdminConfiguration>
			<UserName>maxbiuser</UserName>
		</AdminConfiguration>
	</Configuration>
	</Extension>
</Security>
```

```
<Authentication>
	<Extension Name="Forms" Type="Microsoft.Samples.ReportingServices.CustomSecurity.AuthenticationExtension,Microsoft.Samples.ReportingServices.CustomSecurity" />
</Authentication> 
```

下面加入：

```
<MachineKey ValidationKey="[YOUR KEY]" DecryptionKey="[YOUR KEY]" Validation="AES" Decryption="AES" />
```

下加入，配置直通 cookie

```
<UI>
   <CustomAuthenticationUI>
      <PassThroughCookies>
         <PassThroughCookie>sqlAuthCookie</PassThroughCookie>
      </PassThroughCookies>
   </CustomAuthenticationUI>
</UI>
```

6、修改 rssrvpolicy. config 文件

* 需要为自定义安全扩展添加一个代码组, 该代码组将授予您的扩展的 fulltrust 权限。为此, 可以将代码组添加到 rssrvpoligy. config 文件中。

* 打开位于目录中的 rssrvpolicy. config 文件。 C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer`

* 在安全策略文件中的现有代码组之后添加以下元素, 如下所示, 然后添加一个条目, 如下所示, 以 rssrvpolicy. config。请确保根据您的 reportserver 安装目录更改以下路径:`<CodeGroup>`

```
<CodeGroup
	class="UnionCodeGroup"
	version="1"
	Name="SecurityExtensionCodeGroup" 
	Description="Code group for the sample security extension"
	PermissionSetName="FullTrust">
<IMembershipCondition 
	class="UrlMembershipCondition"
	version="1"
	Url="C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer\bin\Microsoft.Samples.ReportingServices.CustomSecurity.dll"/>
</CodeGroup>
```

7、修改报表服务器的 web. config 文件

在文本编辑器中打开 web. config 文件。默认情况下, 该文件位于目录中。 C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer`

* 找到该元素, 并将 “模拟” 属性设置为 false。`<identity>`
```
<identity impersonate="false" />
```

* 找到该元素, 并将 mode 属性更改为窗体。此外, 将以下元素添加为元素的子元素, 并设置 loginurl、名称、超时和路径属性, 如下所示:`<authentication><forms><authentication>`
```
<authentication mode="Forms">
	<forms loginUrl="logon.aspx" name="sqlAuthCookie" timeout="60" path="/"></forms>
</authentication> 
```

* 直接在元素之后添加以下元素。`<authorization><authentication>`
```
<authorization> 
<deny users="?" />
</authorization> 
```

这将拒绝未经身份验证的用户访问报表服务器的权限。该元素以前建立的 loginurl 属性将未经身份验证的请求重定向到 logon. aspx 页。

8、使用CustomSecuritySample\Setup下面 **CreateUserStore.sql** 创建用户表

# 排错

部署完成后，重启Power BI 服务器服务。访问我的报表地址是81端口：http://maxtestweb:81/Reports

会跳转到 http://maxtestweb:81/ReportServer/logon.aspx?ReturnUrl=/ReportServer/localredirect?url=%2freports

但是我在访问的时候报错，出现500错误什么的，检查完成一遍后，还是报错。 检查日志发现：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8108.png)

runtimeBroker没有权限。 打开注册表，找到appid，然后右键权限，将所有者改为管理员。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8109.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8110.png)

然后使用组件服务，找到 runtimeBroker，点击属性 权限添加相应的用户权限。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8111.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8112.png)

重启服务器，然后刷新，看到登录界面。终于看到了希望。点击注册用户，报告无法链接到数据库服务器。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8113.png)

代码里面AuthenticationUtilities.cs可以看到：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8114.png)

sqlconnection使用的参数是：Properties.Settings.Default.Database_ConnectionString 这诡异的地方。这里自己改到仔细的数据库服务器。

改完后登录后的效果。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E7%BA%B5%E6%9C%89%E5%80%9A%E5%A4%A9%E5%89%91%E8%BF%98%E8%A6%81%E5%B1%A0%E9%BE%99%E5%88%80%EF%BC%8C%E5%AE%9E%E7%8E%B0Power%20BI%E6%8A%A5%E8%A1%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AE%A4%E8%AF%8115.png)

# 总结

以上方法实现了自定义认证，因为可以自定义了既可以实现各种验证方法，比如多因子。过程看起来比较繁琐，还是比较容易实现的。AuthenticationUtilities.cs和login.cs可以实现更多的内容。
