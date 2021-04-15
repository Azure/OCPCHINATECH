# 04 - 配置Spring Cloud Config Server

**本教程是[Azure Spring Cloud 培训](../README.md)系列之一**

云原生应用程序的一个关键功能是*外部化配置*-能够将配置与应用程序代码分开，进行独立的存储、管理和版本化。在此部分中，我们将配置[Spring Cloud Config Server](https://cloud.spring.io/spring-cloud-config)启用此功能。在下一节中，您将看到Spring Cloud Config 如何从 Git 存储库向您的应用程序注入配置。

---

> 💡 如果您的组织使用 Azure 存储库(Repos)作为源代码存储库，请参阅[使用Azure Repos进行Azure Spring Cloud配置](AzureReposForConfig.md)

> ⏱如果您想跳过创建私有存储库的步骤，您可以改用此公共存储库：<https://github.com/Azure-Samples/spring-cloud-sample-public-config.git>. **在真实世界部署中不建议将配置存储在公共存储库中.** 我们仅提供此公共存储库作为本次Workshop的实验便利，例如，如果您没有 GitHub 帐户。
>
> 要使用此快捷方式：
>
> -   转到(G)[Azure门户网站](https://portal.azure.com/).
> -   转到 Azure Spring Cloud服务器的概述页面，并在菜单中选择" Config Server"
> -   设置存储库网址：`https://github.com/Azure-Samples/spring-cloud-sample-public-config.git`
> -   单击"验证"并等待操作成功
> -   单击"应用"并等待操作成功
>
>     我们已启用 Azure Spring Cloud创建 Config Server，其中包含来自此存储库的配置文件。现在，您可以继续阅读下一个教程：
>     ➡[05 - 使用Spring Cloud功能构建Spring Boot微服务](../05-build-a-spring-boot-microservice-using-spring-cloud-features/README.md)

## 创建用于存储应用程序配置的 Git 存储库

在你的[Github帐户](https://github.com)，创建一个新的**私人**存储库用来作为Spring Boot配置的存储库。

在新的私人 GitHub 存储库中，添加新的`application.yml`文件将存储配置数据为我们所有的微服务。

通常，每个Spring Boot应用程序在打包文件中都包含有类似文件，用来作为应用程序配置。Spring Cloud Config Server允许将此类设置集中存储在单个位置，来实现配置集中化管理。

现在，我们的`application.yml`将只存储一条消息，以检查配置是否成功：

```yaml
application:
    message: Configured by Azure Spring Cloud
```

commit并push修改的文件。

## 创建 GitHub 私有 Token

Azure Spring Cloud可以访问公共、由 SSH 保护或使用 HTTP 基本身份验证进行保护的 Git 存储库。我们将使用最后一个选项，因为这样在Github上更容易创建和管理GitHub。

参考[GitHub 教程，以创建私有访问token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)，并保存您的令牌。当被要求选择范围(Scope)时，请选择整个"Repo(库)"部分（如下所示），这样就完成了。

![GitHub personal access token](media/01-github-personal-access-token.png)

生成令牌后，将该选项卡保持打开状态，直到本节结束。

## 配置 Azure Spring Cloud以访问 Git 存储库

-   转到(G)[Azure门户网站](https://portal.azure.com/?WT.mc_id=azurespringcloud-github-judubois).
-   转到 Azure Spring Cloud服务器的概述页面，并在菜单中选择" Config Server"
-   配置我们以前创建的存储库：

    -   例如，添加存储库 URL`https://github.com/Azure-Samples/spring-cloud-sample-public-config.git`

        > 💡确保您包括`.git`以网址结尾。

    -   单击`Authentication`并选择`HTTP Basic`

    -   这**用户名**是您的GitHub登录名

    -   这**密码**是我们在前一节创建的个人令牌
-   单击"验证"并等待操作成功
-   单击"应用"并等待操作成功

![Spring Cloud config server](media/02-config-server.png)

## 回顾

我们现在创建了一个私人配置存储库。我们已启用 Azure Spring Cloud创建 Config Server，其中包含来自此存储库的配置文件。

在下一节中，我们将创建一个应用程序来使用此配置，特别是我们在定义的自定义消息`application.yml`.

---

⬅️上一个教程：[03 - 配置应用程序日志](../03-configure-monitoring/README.md)

➡️下一个教程：[05 - 使用Spring Cloud功能构建Spring Boot微服务](../05-build-a-spring-boot-microservice-using-spring-cloud-features/README.md)
