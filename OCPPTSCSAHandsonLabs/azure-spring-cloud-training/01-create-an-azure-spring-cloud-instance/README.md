# 01 - 创建Azure Spring Cloud实例

**本教程是[Azure Spring Cloud培训](../README.md)系列之一**

在本节中，我们将使用 Azure CLI 创建 Azure Spring Cloud实例。虽然还有其他方法可以创建 Azure 资源，但 Azure CLI 是最快、最简单的方法。

---

## 验证Azure 订阅

确保您在 Azure CLI 中登录到您的 Azure 订阅。

> 💡如果使用 Windows，请确保输入这些命令和 Git Bash 中遵循的所有其他命令。**不要使用 WSL、Cloud Shell或任何其他Shell。**

```bash
az login # Sign into an azure account
az account show # See the currently signed-in account.
```

确保默认订阅是您打算用于此实验室的订阅，如果不是 - 通过下面命令来指定：
`az account set --subscription <SUBSCRIPTION_ID>`

## 创建Azure Spring Cloud实例

在本节中，我们将使用 Azure CLI 创建我们的Azure Spring Cloud实例。

首先，您需要为您的 Azure Spring Cloud实例指定一个名称。

-   **这个名字必须在所有Azure的Spring Cloud实例中是独一无二的**.可以考虑使用您的用户名作为名称的一部分。
-   名称只能包含小写字母、数字和连字符。第一个字符必须是字母。最后一个字符必须是字母或数字。长度必须在 4 到 32 个字符之间。

为了减少重复输入，设置变量`AZ_RESOURCE_GROUP`到上一节中创建的资源组的名称。设置变量`AZ_SPRING_CLOUD_NAME`要创建的Azure Spring Cloud实例的名称：

> 🛑如上所述， 一定要用你自己的值来替换`AZ_RESOURCE_GROUP`和`AZ_SPRING_CLOUD_NAME`。**`AZ_SPRING_CLOUD_NAME`必须是全球独一无二的，使用小写字母，不应该有特殊的字符。**

```bash
AZ_RESOURCE_GROUP=spring-cloud-lab
AZ_SPRING_CLOUD_NAME=azure-spring-cloud-lab
```

使用这些变量集，我们现在可以创建 Azure Spring Cloud实例。为了启用 Java 进程监控代理，我们添加`enable-java-agent`参数。

```bash
az spring-cloud create \
    -g "$AZ_RESOURCE_GROUP" \
    -n "$AZ_SPRING_CLOUD_NAME" \
    --enable-java-agent \
    --sku standard
```

在本次Workshop的剩余时间里，我们将在Azure CLI里 一直使用同一资源组和 Azure Spring Cloud 实例。因此，我们可以把它们设置为默认值，这样就不必再次指定这些参数：

```bash
az configure --defaults group=$AZ_RESOURCE_GROUP
az configure --defaults spring-cloud=$AZ_SPRING_CLOUD_NAME
```

等Azure Spring Cloud实例创建完，可以在Azure Portal里确认，并熟悉一下菜单配置。

---

⬅️上一个教程：[00 - 设置您的环境](../00-setup-your-environment/README.md)

➡️下一个教程：[02 - 构建一个简单的Spring Boot微服务](../02-build-a-simple-spring-boot-microservice/README.md)
