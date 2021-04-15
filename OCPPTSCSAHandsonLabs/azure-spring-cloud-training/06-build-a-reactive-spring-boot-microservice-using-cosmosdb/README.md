# 06 - 使用Cosmos DB构建Reactive Spring Boot微服务

**本教程是[Azure Spring Cloud 培训](../README.md)系列之一**


在本节中，我们将构建一个使用[Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/?WT.mc_id=azurespringcloud-github-judubois)的应用程序，以便访问性能最佳的全球分布式数据库。

我们将使用Reactive编程范式来构建本节中的微服务，利用[Spring Reactive stack](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html). 作为对比，我们将在下一节构建更传统的数据驱动微服务。

---

## 准备Cosmos DB

从第 00 节开始， 你应该已经有一个Cosmos DB帐户命名`sclabc-<unique string>`.

-   单击"数据资源管理器"菜单项

    -   展开目录`azure-spring-cloud-cosmosdb`.
    -   在该目录中，展开目录`City`.
    -   单击"项目(Items)"并使用"新项目(New Item)"按钮创建一些示例项目：

        ```json
        {
            "name": "Paris, France"
        }
        ```

        ```json
        {
            "name": "London, UK"
        }
        ```
    - 点击Save
![Data explorer](media/02-data-explorer.png)

## 创建Spring Webflux微服务

我们在本教程中创建的微服务[可以参考在这里](city-service/).

为了创建我们的微服务，我们将从命令行调用Spring Initalizer服务：

```bash
curl https://start.spring.io/starter.tgz -d dependencies=webflux,cloud-eureka,cloud-config-client -d baseDir=city-service -d bootVersion=2.3.8 -d javaVersion=1.8 | tar -xzvf -
```

> 我们使用`Spring Webflux`,`Eureka Discovery Client`和`Config Client`Spring Boot starters。

## 添加Cosmos DB API

在应用程序的`pom.xml`文件中，在`spring-cloud-starter-netflix-eureka-client`后添加Cosmos DB依赖：

```xml
        <dependency>
            <groupId>com.azure</groupId>
            <artifactId>azure-cosmos</artifactId>
            <version>4.5.0</version>
        </dependency>
```

## 添加Spring Reactive代码从数据库获取数据

在`DemoApplication`类的目录下，创建一个`City` domain Object：

```java
package com.example.demo;

class City {

    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

然后，在同一位置创建一个新的`CityController.java`文件，
添加用于查询数据库的代码。

> City控制器类将从 Azure Spring Cloud服务绑定中获取其Cosmos DB 配置，我们将在稍后进行配置。

```java
package com.example.demo;

import com.azure.cosmos.CosmosAsyncContainer;
import com.azure.cosmos.CosmosClientBuilder;
import com.azure.cosmos.models.CosmosQueryRequestOptions;
import com.azure.cosmos.models.FeedResponse;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

import javax.annotation.PostConstruct;
import java.util.List;

@RestController
public class CityController {

    @Value("${azure.cosmosdb.uri}")
    private String cosmosDbUrl;

    @Value("${azure.cosmosdb.key}")
    private String cosmosDbKey;

    @Value("${azure.cosmosdb.database}")
    private String cosmosDbDatabase;

    private CosmosAsyncContainer container;

    @PostConstruct
    public void init() {
        container = new CosmosClientBuilder()
                .endpoint(cosmosDbUrl)
                .key(cosmosDbKey)
                .buildAsyncClient()
                .getDatabase(cosmosDbDatabase)
                .getContainer("City");
    }

    @GetMapping("/cities")
    public Flux<List<City>> getCities() {
        CosmosQueryRequestOptions options = new CosmosQueryRequestOptions();
        return container.queryItems("SELECT TOP 20 * FROM City c", options, City.class)
                .byPage()
                .map(FeedResponse::getResults);
    }
}
```

## 在Azure Spring Cloud上创建应用程序

如在[02 - 构建一个简单的Spring Boot微服务](../02-build-a-simple-spring-boot-microservice/README.md)，创建一个特定的`city-service`应用在您的Azure Spring Cloud实例中：

```bash
az spring-cloud app create -n city-service
```

## 将Cosmos DB绑定到应用程序中

Azure Spring Cloud可以自动将我们创建的Cosmos DB绑定到我们的微服务中。

-   转到 Azure Spring Cloud实例中的"应用"。
-   选择`city-service`应用
-   转到(G)`Service bindings`
-   单击"创建服务绑定"
    -   例如，给绑定一个名称`cosmosdb-city`
    -   选择我们创建的Cosmos DB帐户和数据库，并保留默认值`sql`API 类型
    -   在下拉列表中，选择主要密钥
    -   单击`Create`创建数据库绑定

![Bind Cosmos DB database](media/03-bind-service-cosmosdb.png)

## 部署应用程序

现在，您可以构建您的"city-service"项目，并将其部署到 Azure Spring Cloud：

```bash
cd city-service
./mvnw clean package -DskipTests
az spring-cloud app deploy -n city-service --jar-path target/demo-0.0.1-SNAPSHOT.jar
cd ..
```

## 在云中测试项目

-   转到 Azure Spring Cloud实例中的"应用"。
    -   验证`city-service`有一个`Registration status`其中说`1/1`.这表明它在Spring Cloud Service Registry注册成功。
    -   选择`city-service`了解有关微服务的更多信息。
-   复制/粘贴提供的"测试终点"。

您现在可以使用cURL来测试`/cities`终点，它应该返回你创建的城市列表。例如，如果您只创建`Paris, France`和`London, UK`就像本教程中显示的那样，您应该获得：

```json
[[{"name":"Paris, France"},{"name":"London, UK"}]]
```

如果您需要检查您的代码，最终项目可在["city-service"文件夹](city-service/).

---

⬅️上一个教程：[05 - 使用Spring Cloud功能构建Spring Boot微服务](../05-build-a-spring-boot-microservice-using-spring-cloud-features/README.md)

➡️下一个教程：[07 - 使用 MySQL 构建Spring Boot微服务](../07-build-a-spring-boot-microservice-using-mysql/README.md)
