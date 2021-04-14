# 00 - 设置您的环境

**本教程是[Azure Spring Cloud 培训](../README.md)系列之一**

为了让您能快速顺利的完成培训，在本节中，我们将设置好所需的一切。

---

## 创建Azure资源

为了节省时间，我们提供了一个 ARM 模板，用于创建此实验室所需的所有 Azure 资源，而不是 Azure Spring Cloud实例本身。使用下面的"部署到Azure"按钮。

> 💡 使用以下设置部署 Azure 模板：
>
> -   创建新的资源组。
> -   在位置字段中，从[Azure Spring Cloud可用区域列表](https://azure.microsoft.com/global-infrastructure/services/?products=spring-cloud&regions=all)选择，建议选东南亚(SouthEast Asia).
> -   保存您在此步骤中指定的 MySQL 密码。您将需要它在第6节。如果你不设置一个，默认是`super$ecr3t`.

[![部署到Azure](media/deploybutton.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fmicrosoft%2Fazure-spring-cloud-training%2Fmaster%2F00-setup-your-environment%2Fazuredeploy.json?WT.mc_id=azurespringcloud-github-judubois)

> ⏱资源配置需要一些时间。**不用等待**继续进行Workshop。

## 先决条件

此培训实验要求在您的计算机上安装以下设备：

-   [JDK 1.8](https://www.azul.com/downloads/azure-only/zulu/?&version=java-8-lts&architecture=x86-64-bit&package=jdk)

-   文本编辑器或IDE。如果您还没有用于Java开发的IDE，我们建议使用[Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=azurespringcloud-github-judubois)与[Java Extension Pack](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack&WT.mc_id=azurespringcloud-github-judubois).

-    Bash Shell. 虽然 Azure CLI 应在所有OS环境中作用相同，但 Shell 语法各不相同。因此，只有 bash 才能用于此培训中的命令。要在 Windows 上完成此培训，请使用[Git Bash，Windows 版本的Git安装包里自带](https://git-scm.com/download/win).**仅使用 Git Bash 在 Windows 上完成此培训。不要使用 WSL、Cloud Shell 或任何其他以外的 Shell 。**

-   [Azure](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest&WT.mc_id=azurespringcloud-github-judubois)版本2.0.80或更新。您可以通过运行来检查当前 Azure CLI 安装的版本：

    ```bash
    az --version
    #升级到最新版本
    az --upgrade --yes
    ```

> 💡如果你尝试上面的命令，你会看到错误`bash: az: command not found`，运行以下命令：`alias az='az.cmd'`再试一次

-   🚧`spring-cloud`Azure CLI 的扩展。您可以在安装Azure CLI后通过运行安装此扩展`az extension add -n spring-cloud -y`.如果已安装扩展，请通过运行`az extension update -n spring-cloud` 将其更新到最新版本.

> 💡 在第 9 节和第 10 节中，您将在 Web 浏览器中访问微服务应用程序的 UI。使用[新Edge](https://microsoft.com/edge/?WT.mc_id=azurespringcloud-github-judubois)，谷歌浏览器，或火狐浏览器为这些部分。

环境变量`JAVA_HOME`应设置为JDK安装的路径。此路径指定的目录应具有`bin`,`jre`和`lib`在其子目录中。此外，确保您的`PATH`变量包含目录`${JAVA_HOME}/bin`.要测试、键入`which javac`进入bash外 Shell ，确保由此产生的路径指向里面的文件`${JAVA_HOME}/bin`.

然后，您可以使用可视化工作室代码或您选择的 IDE。

---

➡️下一个教程：[01 - 创建Azure Spring Cloud实例](../01-create-an-azure-spring-cloud-instance/README.md)
