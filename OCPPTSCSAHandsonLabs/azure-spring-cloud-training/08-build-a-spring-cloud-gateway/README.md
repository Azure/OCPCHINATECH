# 08 - 构建Spring Cloud网关

**本教程是[Azure Spring Cloud 培训](../README.md)系列之一**


Spring Cloud网关允许您有选择地通过统一的服务入口暴露您的微服务，并将流量路由到各服务。在此部分中，我们将创建一个"Spring Cloud Gateway"，该网关将使用我们在前两个部分创建的微服务。

---

## 创建Spring Cloud网关

我们在本教程中创建的应用程序[可参考这里](gateway/). 建议按下面一步一步来创建。

为了创建我们的网关，我们将从命令行调用Spring Initalizer服务：

```bash
curl https://start.spring.io/starter.tgz -d dependencies=cloud-gateway,cloud-eureka,cloud-config-client -d baseDir=gateway -d bootVersion=2.3.8 -d javaVersion=1.8 | tar -xzvf -
```

> 我们使用`Cloud Gateway`,`Eureka Discovery Client`和`Config Client`组件。

## 配置应用程序

重命名`src/main/resources/application.properties`自`src/main/resources/application.yml`并添加以下配置：

```yaml
spring:
  main:
    allow-bean-definition-overriding: true
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
      globalcors:
        corsConfigurations:
          '[/**]':
            allowedOrigins: "*"
            allowedMethods:
              - GET

```

-   `spring.main.allow-bean-definition-overriding=true`这部分是配置Spring Cloud网关，以使用 Azure Spring Cloud Client Library中配置的Spring Cloud Discovery Server bean。
-   `spring.cloud.gateway.discovery.locator.enabled=true`这部分是配置Spring Cloud网关，使用Spring Cloud Service Registry发现可用的微服务。
-   `spring.cloud.gateway.globalcors.corsConfiguration`这部分是允许CORS(跨站)请求到我们的网关。这将在下一个教程中使用到，届时我们将添加未在 Azure Spring Cloud 上托管的前端应用。

## 在Azure Spring Cloud上创建应用程序

如在[02 - 构建一个简单的Spring Boot微服务](../02-build-a-simple-spring-boot-microservice/README.md)，创建一个特定的`gateway`应用在您的Azure Spring Cloud实例中。由于此应用程序是网关，我们需要添加`--is-public true`标志，以便互联网可以访问到。

注：这个标志以后会改成 `--assign-endpoint`

```bash
az spring-cloud app create -n gateway --is-public true
```

## 部署应用程序

您现在可以构建您的"Gateway"项目并将其部署到 Azure Spring Cloud 中：

```bash
cd gateway
./mvnw clean package -DskipTests
az spring-cloud app deploy -n gateway --jar-path target/demo-0.0.1-SNAPSHOT.jar
cd ..

```

## 在云中测试项目

-   转到 Azure Spring Cloud实例中的"应用"。
    -   验证`gateway`有一个`Registration status`其中说`1/1`.这表明它在Spring Cloud Service Registry注册成功。
    -   选择`gateway`了解有关微服务的更多信息。
-   复制/粘贴提供的公共网址（有一个"测试端点"，如微服务，但网关直接暴露在互联网上，所以我们可以使用公共网址）。为后续部分方便测试，记下这个URL。

由于网关连接到Spring Cloud Service Registry，因此它应该自动打开通往可用微服务的路由，URL 路径的格式如下`/MICROSERVICE-ID/**`:
[MICROSERVICE-ID必须是大写字母]

-   测试`city-service`微服务终点通过做：`curl https://XXXXXXXX-gateway.azuremicroservices.io/CITY-SERVICE/cities`（用您的Azure Spring Cloud实例名称替换X）
-   测试`weather-service`微服务终点通过做：`curl 'https://XXXXXXXX-gateway.azuremicroservices.io/WEATHER-SERVICE/weather/city?name=Paris%2C%20France'`（用网关名称替换X）

如果您需要参考您的代码，最终项目在["gateway"文件夹](gateway/).

---

⬅️上一个教程：[07 - 使用 MySQL 构建Spring Boot微服务](../07-build-a-spring-boot-microservice-using-mysql/README.md)

➡️下一个教程：[09 - 综上所述，一个完整的微服务Stack](../09-putting-it-all-together-a-complete-microservice-stack/README.md)
