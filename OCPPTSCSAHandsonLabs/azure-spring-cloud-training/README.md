---
page_type：sample
Language：
-   Java
---

# Azure Spring Cloud培训

> 您将在此处找到关于 Azure Spring Cloud的完整Workshop，包括教程和演示。

> 这个实验是基于一个公共Workshop创建的[朱利安·杜布瓦](https://twitter.com/juliendubois)并免费提供给每个人，遵守[MIT License](LICENSE.txt).

## 友情提示

> 这不是官方产品组提供的培训，而是第三方提供的。

> 这是一次动手培训，它将大量使用命令行CLI。这样是为了快速编码和熟悉平台，将从一个简单的演示开始到更复杂的例子。

> 完成所有教程后，您应该对Azure  Spring Cloud提供的功能有比较好的了解。

## 符号说明

> 🛑 -**需要手工修改**.当此符号出现在一个或多个命令前面时，您将需要在运行命令之前按照指示修改命令。

> 🚧 -**预览特定**.此符号表示仅在 Azure Spring Cloud 预览时需要的步骤。

> 💡 -**坑避免提示**.这些将帮助您避免潜在的陷阱。

## [00 - 先决条件和设置](00-setup-your-environment/README.md)

先决条件和环境设置。

## [01 - 创建Azure Spring Cloud Cluster ](01-create-an-azure-spring-cloud-instance/README.md)

创建集群， 并配置 CLI 来提高工作效率。

## [02 - 构建一个简单的Spring Boot 微服务](02-build-a-simple-spring-boot-microservice/README.md)

使用Spring Initializer构建最简单的Spring Boot 微服务。

## [03 - 配置应用程序日志](03-configure-monitoring/README.md)

访问Spring Boot 应用程序日志以了解常见问题。

## [04 - 配置Spring Cloud Config Server](04-configure-a-spring-cloud-config-server/README.md)

配置一个[Spring Cloud Config Server](https://cloud.spring.io/spring-cloud-config)，这将完全由 Azure Spring Cloud管理和支持，由Spring Boot微服务使用。

## [05 - 使用Spring Cloud 特性来构建Spring Boot 微服务](05-build-a-spring-boot-microservice-using-spring-cloud-features/README.md)

构建云原生的Spring Boot微服务：结合使用Spring Cloud Service Registry和[Spring Cloud Config Server](https://cloud.spring.io/spring-cloud-config) 两个服务都由Azure Spring Cloud管理和支持。

## [06 - 构建一个使用Cosmos DB 的响应式 Spring Boot 微服务](06-build-a-reactive-spring-boot-microservice-using-cosmosdb/README.md)

构建一个响应式的Spring Boot 微服务，使用[Spring reactive stack ](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html)并绑定一个[Cosmos DB 数据库](https://docs.microsoft.com/en-us/azure/cosmos-db/?WT.mc_id=azurespringcloud-github-judubois)以便访问性能最佳的全球分布式数据库。

## [07 - 构建一个使用 MySQL 的 Spring Boot 微服务](07-build-a-spring-boot-microservice-using-mysql/README.md)

构建一个经典的Spring Boot 应用程序，使用 JPA 访问[由Azure管理的 MySQL 数据库](https://docs.microsoft.com/en-us/azure/mysql/?WT.mc_id=azurespringcloud-github-judubois).

## [08 - 构建Spring Cloud 网关](08-build-a-spring-cloud-gateway/README.md)

构建一个[ Spring Cloud网关](https://spring.io/projects/spring-cloud-gateway)将HTTP请求路由到指定的Spring Boot 微服务。

## [09 - 综合一起，一个完整的微服务堆栈](09-putting-it-all-together-a-complete-microservice-stack/README.md)

使用前端以图形方式访问我们完整的微服务堆栈。通过 Azure Spring Cloud的分布式跟踪机制监控我们的服务，并根据我们的需求扩展我们的服务。

## [10 - 蓝/绿部署](10-blue-green-deployment/README.md)

在Staging环境中部署新版本的应用程序，并与 Azure Spring Cloud在Staging和Production之间切换。

## [11 - 配置 CI/CD](11-configure-ci-cd/README.md)

使用 GitHub Action配置连续集成/连续部署平台，因此我们的Spring Boot 微服务将实现自动部署。

## [12 - 微服务间的相互调用](12-making-microservices-talk-to-each-other/README.md)

创建与其他微服务相互调用的微服务。

## [总结](99-conclusion/README.md)

---

## Legal Notices

微软和任何贡献者授予您微软文档和其他内容的许可证
在此存储库下[创意共享归属 4.0 国际公共许可证](https://creativecommons.org/licenses/by/4.0/legalcode),
看到[许可证](LICENSE)文件，并授予您许可证下存储库中的任何代码[MIT License](https://opensource.org/licenses/MIT)，请参阅
[许可证代码](LICENSE-CODE)文件。

文档中引用的微软、Windows、微软 Azure 和/或其他微软产品和服务
可能是微软在美国和/或其他国家的商标或注册商标。
此项目的许可证不授予您使用任何 Microsoft 名称、徽标或商标的权利。
微软的一般商标教程可以在<http://go.microsoft.com/fwlink/?LinkID=254653>.

隐私信息可在<https://privacy.microsoft.com/en-us/>

微软和任何贡献者保留所有其他权利，无论是根据各自的版权，专利，
或商标，无论是通过暗示，阻止或其他。
