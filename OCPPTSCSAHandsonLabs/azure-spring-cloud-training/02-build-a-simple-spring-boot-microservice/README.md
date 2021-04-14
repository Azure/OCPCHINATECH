# 02 - 构建一个简单的Spring Boot微服务

**本教程是[Azure Spring Cloud 培训](../README.md)系列之一**

在此部分中，我们将构建一个简单的Spring Boot微服务，并将其部署到 Azure Spring Cloud。这是我们在以后的章节中学习Spring Cloud技术的一个基础前提。

---

## 创建简单的Spring Boot微服务

我们在本教程中创建的微服务是[基于这个样例](simple-microservice/), 样例仅供参考，下面我们会一步步把它创建出来.

创建Spring Boot应用程序的典型方法是使用Spring Initializer：<https://start.spring.io/> . 如果想了解更多，可以看看官方文档或其他教程。**为了这次培训的目的，我们只会使用`curl`命令**.

> 💡**注意：**本Workshop的所有后续命令应从同一目录运行，除非另有指示`cd`命令。

在一个**空**目录执行下面的 curl 命令行：

```bash
curl https://start.spring.io/starter.tgz -d dependencies=web -d baseDir=simple-microservice -d bootVersion=2.3.8 -d javaVersion=1.8 | tar -xzvf -
```

> 我们强制Spring Boot版本为2.3.8。

## 添加新的Spring MVC Controller

可以在VS Code下操作
```bash
cd simple-microservice
code .
```

在`simple-microservice/src/main/java/com/example/demo`目录，创建一个
新文件`HelloController.java`, 与`DemoApplication.java`文件一起。输入
以下内容：

```java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello from Azure Spring Cloud\n";
    }
}
```

最终项目可在["simple-microservice"文件夹](simple-microservice/).

## 在本地测试项目

运行项目：

```bash
cd simple-microservice
./mvnw spring-boot:run &
cd ..
```

请求`/hello` 服务应返回"Hello from Azure Spring Cloud"的消息。

```bash
curl http://127.0.0.1:8080/hello
```

最后，kill运行的应用程序：

```bash
kill %1
```

## 在Azure Spring Cloud上创建和部署应用程序

此部分显示如何创建应用实例，然后将代码部署到其中。

为了以图形方式创建应用实例，您可以使用[Azure Portal](https://portal.azure.com/):

-   在资源组中查找您的 Azure Spring Cloud实例
-   单击导航侧边栏"设置"下的"应用"链接。
-   单击应用页面顶部的"创建应用"链接。
-   创建名为"simple-microservice"的新应用

![Create application](media/01-create-application.png)

-   单击"创建"。

或者，您可以使用命令行创建应用实例，这更容易：

```bash
az spring-cloud app create -n simple-microservice
```

您现在可以构建您的"simple-microservice"项目，并将其部署到 Azure Spring Cloud：

```bash
cd simple-microservice
./mvnw clean package
az spring-cloud app deploy -n simple-microservice --jar-path target/demo-0.0.1-SNAPSHOT.jar
cd ..
```

这将在本地磁盘上创建一个jar文件，并将其上传到您在上一步中创建的应用实例。 这`az`命令将在JSON中输出结果。 您现在不需要注意此输出，但将来，您会发现它可用于诊断和测试的。

## 在云中测试项目

转到(G)[Azure Portal](https://portal.azure.com/):

-   在资源组中查找您的 Azure Spring Cloud实例
-   单击导航窗格"设置"部分中的"应用"，然后选择"simple-microservice"
-   单击"查看更多"以查看"测试终点"
    ![See More](media/02-seemore.png)
-   网址上的鼠标标记为"测试端点"，然后单击显示的剪贴板图标。  
    这将显示类似的链接：
     `https://primary:BBQM6nsYnmmdQREXQINityNx63kWUbjsP7SIvqKhOcWDfP6HJTqg27klMLaSfpTB@rwo1106f.test.azuremicroservices.io/simple-microservice/default/`
    > 💡注意之间的文本`https://`和`@`. 这些是基本的身份验证凭据，没有凭据，您将无权访问该服务。
-   点终结点右边的复制，并附加`hello/`到网址末尾。 否则，将导致"找不到404"。

您现在可以再次使用cURL来测试`/hello`终点，这次由Azure Spring Cloud服务。 例如。

```bash
curl https://primary:...simple-microservice/default/hello/
```

如果成功，您应该看到消息：`Hello from Azure Spring Cloud`.

## 结论

恭喜你，你已经部署了你的第一个Spring Boot微服务到Azure Spring Cloud！

如果您需要检查您的代码，最终项目可在["simple-microservice"文件夹](simple-microservice/).

下面是构建和部署本教程中所做的一切的最终脚本：
```bash
    curl https://start.spring.io/starter.tgz -d dependencies=web -d baseDir=simple-microservice -d bootVersion=2.3.8 -d javaVersion=1.8 | tar -xzvf -
    cd simple-microservice
    cat > HelloController.java << EOF
    package com.example.demo;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    public class HelloController {

        @GetMapping("/hello")
        public String hello() {
            return "Hello from Azure Spring Cloud";
        }
    }
    EOF
    mv HelloController.java src/main/java/com/example/demo/HelloController.java
    az spring-cloud app create -n simple-microservice
    ./mvnw clean package
    az spring-cloud app deploy -n simple-microservice --jar-path target/demo-0.0.1-SNAPSHOT.jar
```
---

⬅️上一个教程：[01 - 创建Azure Spring Cloud实例](../01-create-an-azure-spring-cloud-instance/README.md)

➡️下一个教程：[03 - 配置监控](../03-configure-monitoring/README.md)
