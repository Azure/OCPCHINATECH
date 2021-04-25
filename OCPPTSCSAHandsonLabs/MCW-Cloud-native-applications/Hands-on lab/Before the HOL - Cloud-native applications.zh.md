![](media/logo.jpg)

<div class="MCWHeader1">
Cloud-native applications
</div>

<div class="MCWHeader2">
Before the hands-on lab setup guide
</div>

<div class="MCWHeader3">
November 2020
</div>

本文档中的信息（包括 URL 和其他互联网网站参考）可能会在未通知的情况下更改。除非另有说明，否则此处描述的示例公司、组织、产品、域名、电子邮件地址、徽标、人员、地点和事件均为虚构的，并且不与任何真实公司、组织、产品、域名、电子邮件地址、徽标、人、地点或事件关联，或应推断。遵守所有适用的版权法是用户的责任。在不限制版权保护的情况下，未经微软公司明确书面许可，不得复制、存储或引入检索系统，也不得以任何形式或以任何方式（电子、机械、影印、录音或其他方式）传输本文件的任何部分。

Microsoft 可能拥有本文件中涉及主题事项的专利、专利申请、商标、版权或其他知识产权。除非 Microsoft 的任何书面许可协议中明确规定，否则本文档的提供不会为您提供这些专利、商标、版权或其他知识产权的任何许可。

制造商、产品或 URL 的名称仅供参考，Microsoft 不会就这些制造商或使用 Microsoft 任何技术的产品进行任何陈述和保修，无论是表达、暗示还是法定。包括制造商或产品并不意味着微软对制造商或产品的认可。链接可提供给第三方网站。此类站点不在 Microsoft 的控制之下，Microsoft 不负责链接站点中包含的任何链接站点的内容或链接的内容，也不对链接站点的任何更改或更新负责。Microsoft 不负责从任何链接站点接收的网络广播或任何其他形式的传输。微软只为方便而向您提供这些链接，包含任何链接并不意味着微软对该网站或其中包含的产品的认可。

©2020年微软公司。保留所有权利。

**内容**

<!-- TOC -->

-   <a href="#cloud-native-applications-before-the-hands-on-lab-setup-guide">动手实验室设置指南之前的云原生应用</a>
    -   <a href="#requirements">要求</a>
    -   <a href="#before-the-hands-on-lab">在动手实验室之前</a>
        -   <a href="#task1">任务1：设置蔚蓝云壳</a>
        -   <a href="#task-2-download-starter-files">任务2：下载入门文件</a>
        -   <a href="#task-3-resource-group">任务3：资源组</a>
        -   <a href="#task-4-create-an-ssh-key">任务 4：创建 SSH 密钥</a>
        -   <a href="#task-5-deploy-arm-template">任务 5：部署 ARM 模板</a>
        -   <a href="#task-6-create-a-github-repository">任务 6： 创建 GitHub 存储库</a>
        -   <a href="#task-7-connect-securely-to-the-build-agent">任务 7：安全地连接到构建代理</a>
        -   <a href="#task-8-complete-the-build-agent-setup">任务 8：完成构建代理设置</a>
        -   <a href="#task-9-clone-repositories-to-the-build-agent">任务 9：生成代理的克隆存储库</a>

<!-- /TOC -->

# <a id="cloud-native-applications-before-the-hands-on-lab-setup-guide">动手实验室设置指南之前的云原生应用</a>

## <a id="requirements">要求</a>

1.  微软 Azure 订阅必须是即用即付或 MSDN。

    -   试用订阅将_不_工作。

    -   要完成此实验室设置，请确保您的帐户包括以下内容：

        -   有[所有者](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#owner)用于您使用的订阅的内置角色。

        -   是一个[成员](https://docs.microsoft.com/azure/active-directory/fundamentals/users-default-permissions#member-and-guest-users)用户在您使用的Azure广告租户。（访客用户将没有必要的权限。

    -   您的订阅中必须有足够的内核来创建构建代理和Azure库伯涅茨服务集群[任务 5：部署 ARM 模板](#Task-5-Deploy-ARM-Template).如果按照实验室中的确切说明操作，则需要八个内核;如果您选择其他代理或更大的 VM 尺寸，则需要更多内核。执行实验室前所需的步骤，查看是否需要在子中请求更多内核。

2.  微软的一个帐户[吉特胡布](https://github.com).

3.  本地计算机或配置为以下配置的虚拟机器：

    -   浏览器，最好是Chrome浏览器，以实现与实验室实施测试的一致性。

4.  在整个练习过程中，您将被要求安装其他工具。

## <a id="before-the-hands-on-lab">在动手实验室之前</a>

**期间**：60分钟

您应该遵循本节中提供的所有步骤_以前_提前参加动手实验室，因为其中一些步骤需要时间。

### <a id="task1">任务1：设置蔚蓝云壳</a>

1.  通过选择菜单栏中的云壳图标打开云壳。

    ![The cloud shell icon is highlighted on the menu bar.](media/b4-image35.png "Cloud Shell")

2.  云壳在浏览器窗口中打开。选择**巴什**如果提示或使用外壳菜单栏上的左侧下拉来选择**巴什**从下降（如图所示）。如果提示，请选择**确认**.

    ![This is a screenshot of the cloud shell opened in a browser window. Bash was selected.](media/b4-image36.png "Cloud Shell Bash Window")

3.  您应该确保正确设置默认订阅。查看当前订阅类型：

    ```bash
    az account show
    ```

    ![In this screenshot of a Bash window, az account show has been typed and run at the command prompt. Some subscription information is visible in the window, and some information is obscured.](media/b4-image37.png "Bash Shell AZ Account Show")

4.  要将默认订阅设置为当前选择以外的其他操作，请键入以下类型，用所需的订阅 ID 值替换 {id}：

    ```bash
    az account set --subscription {id}
    ```

> **注意**：要列出您的所有订阅，请键入：

```bash
az account list
```

   ![In this screenshot of a Bash window, az account list has been typed and run at the command prompt. Some subscription information is visible in the window, and some information is obscured.](media/b4-image38.png "Bash AZ Account List")

### <a id="task-2-download-starter-files">任务2：下载入门文件</a>

在此任务中，您使用`git`将实验室内容复制到云壳中，以便实验室启动文件可用。

> **注意**：如果您没有可用的云壳，请参阅<a href="#task1">任务1：设置蔚蓝云壳</a>.

1.  键入以下命令并按下`<ENTER>`:

    ```bash
    git clone https://github.com/microsoft/MCW-Cloud-native-applications.git
    ```

    > **注意**：如果您没有足够的自由空间，您可能需要从云壳环境中删除额外的文件。 尝试运行`azcopy jobs clean`删除任何`azcopy`您不需要的工作和数据。

2.  实验室文件下载。

    ![In this screenshot of a Bash window, git clone has been typed and run at the command prompt. The output from git clone is shown.](media/b4-2019-09-30_21-25-06.png "Bash Git Clone")

3.  我们不需要`.git`文件夹，以后的步骤将不那么复杂，如果我们删除它。运行此命令：

    ```bash
    rm -rf MCW-Cloud-native-applications/.git
    ```

### <a id="task-3-resource-group">任务3：资源组</a>

创建一个 Azure 资源组，以保存您在这个动手实验室中创建的大部分资源。这种方法使得以后更容易清理。

1.  在云壳窗口中，您键入类似于以下命令的命令，请务必更换令牌：

    > **注意**：如果您没有可用的云壳，请参阅<a href="#task1">任务1：设置蔚蓝云壳</a>.

    ```bash
    az group create -l '[LOCATION]' -n 'fabmedical-[SUFFIX]'
    ```

    -   **后缀：**在整个实验室中，后缀应用于使资源独一无二，如电子邮件前缀或您的第一个初始和姓氏。

    -   **位置：**选择所有 Azure 集装箱注册处 SKU 必须可用的区域，即当前：加拿大中部、加拿大东部、美国中北部、美国中部、美国中南部、美国东部、美国东部 2、美国西部、美国西部 2、美国中西部、法国中部、英国南部、英国西部、北欧、西欧、澳大利亚东部、澳大利亚东南部、巴西南部、印度中部、印度南部，日本东部，日本西部，韩国中部，东南亚，东亚，并记住这一点，为未来的步骤，使你在Azure创造的资源都保存在同一区域。

    例：

    ```bash
    az group create -l 'west us' -n 'fabmedical-sol'
    ```

2.  完成此功能后，Azure 门户将显示您的资源组。

    ![In this screenshot of the Azure Portal, the fabmedical-sol Resource group is listed.](media/b4-image8.png "Fabmedical Resource Groups")

### <a id="task-4-create-an-ssh-key">任务 4：创建 SSH 密钥</a>

在即将到来的练习中，您创建虚拟机。在此部分中，您创建一个 SSH 密钥，以便安全地访问 VM。

1.  从云壳命令行输入以下命令，以确保存在 SSH 密钥的目录。您可以忽略在输出中看到的任何错误。

    > **注意**：如果您没有可用的云壳，请参阅<a href="#task1">任务1：设置蔚蓝云壳</a>.

    ```bash
    mkdir .ssh
    ```

2.  从云壳命令行，输入以下命令生成 SSH 键对。您可以替换`admin`与您的首选名称或句柄。

    ```bash
    ssh-keygen -t RSA -b 2048 -C admin@fabmedical
    ```

3.  当被要求将生成的密钥保存到文件时，请输入`.ssh/fabmedical`为名称。

4.  提示时输入密码短语，以及**别忘了**!

5.  因为你输入`.ssh/fabmedical`什基根生成的文件在`.ssh`用户文件夹中的文件夹，默认情况下云外壳打开的位置。

    ![In this screenshot of the cloud shell window, ssh-keygen -t RSA -b 2048 -C admin@fabmedical has been typed and run at the command prompt. Information about the generated key appears in the window.](media/b4-image57.png "SSH Keygen")

6.  从云壳命令行，输入以下命令以输出公共关键内容。复制此信息以稍后使用。

    ```bash
    cat .ssh/fabmedical.pub
    ```

7.  保持此云壳打开并保留在默认目录中。您将在以后的任务中使用此外壳。

    ![In this screenshot of the cloud shell window, cat .ssh/fabmedical has been typed and run at the command prompt. Information about the public key content appears in the window.](media/b4-image571.png "Cloud Shell - cat .ssh")

### <a id="task-5-deploy-arm-template">任务 5：部署 ARM 模板</a>

在本节中，您配置并执行 ARM 模板，该模板可创建整个练习所需的所有资源。

1.  在 Azure 云壳中，切换到 ARM 模板目录：

    > **注意**：如果您没有可用的云壳，请参阅<a href="#task1">任务1：设置蔚蓝云壳</a>.

    ```bash
    cd MCW-Cloud-native-applications/Hands-on\ lab/arm/
    ```

2.  打开azure部署.参数.json文件，使用蔚蓝云壳编辑器进行编辑。

    ```bash
    code azuredeploy.parameters.json
    ```

    ![This screenshot shows the online editor for azure could shell. Display the azuredeploy.parameters.json](media/b4-image581.png "Edit azuredeploy.parameters.json")

3.  更新各种密钥的值，以便它们与您的环境相匹配：

    -   **后缀**：输入最多3个字符的SUFFIX的缩短版本。
    -   **虚拟机器管理员乌塞纳梅利努克斯**：Linux生成代理VM管理员用户名（示例：`"adminfabmedical"`).
    -   **虚拟机器管理员公开基利努克斯**：Linux生成代理VM管理员sh公钥。您可以在`.ssh/fabmedical.pub`以前创建的文件（示例：`"ssh-rsa AAAAB3N(...)vPiybQV admin@fabmedical"`).
    -   **宇宙定位**：蔚蓝宇宙DB的主要位置。使用与之前创建的资源组相同的位置（示例：`"eastus"`).
    -   **宇宙定位名**：蔚蓝宇宙DB的主要位置的名称。使用与之前创建的资源组相同的位置名称（示例：`"East US"`).
    -   **宇宙定位**：蔚蓝宇宙DB的次要位置。下面的链接可用于帮助查找您主要位置的 Azure 区域对。（示例：`"westus"`).
    -   **宇宙定位名**：蔚蓝宇宙DB的次要位置的名称。使用与上一密钥中定义的辅助位置匹配的位置名称（示例：`"West US"`).

    > **注意**：可在此处找到 Azure 区域对的列表：<https://docs.microsoft.com/en-us/azure/best-practices-availability-paired-regions#azure-regional-pairs>.

4.  选择**...**按钮并选择**救**.

    ![In this screenshot of an Azure Cloud Shell editor window, the ... button has been selected, and the Save option is highlighted.](media/b4-image62.png "Azure Cloud Shell Save")

5.  选择**...**再次按钮并选择**关闭编辑器**.

    ![In this screenshot of the Azure Cloud Shell editor window, the ... button has been selected, and the Close Editor option is highlighted.](media/b4-image63.png "Azure Cloud Shell Close")

6.  通过键入以下指令（案例敏感），用以前创建的资源组的名称替换 \[资源组]来创建所需的资源：

    ```bash
    az deployment group create --resource-group {resourceGroup} --template-file azuredeploy.json --parameters azuredeploy.parameters.json
    ```

    此命令部署所有实验室资源需要 30 到 60 分钟。您可以在部署运行时继续执行设置 GitHub 的下一个任务。

    > **注意**如果你得到一个关于宇宙DB名称的错误，确保你键入`ComsosLocation`和`CosmosPairedLocation`没有任何空间。更正名称后重新运行上述命令。

### <a id="task-6-create-a-github-repository">任务 6： 创建 GitHub 存储库</a>

Fab医疗为您提供了入门文件。他们为客户 Contoso Neuro 获取了网站副本，并将其从单个节点.js网站重新构接到一个包含内容 API 的网站，该网站为扬声器和会话提供服务。此重构代码是验证其网站的容器化的起点。使用此功能帮助他们完成 POC，验证将网站和 API 作为 Docker 容器运行的开发工作流程，并在 Azure Kubernetes 服务环境中管理它们。

1.  打开网络浏览器并导航到<https://www.github.com>.使用您的 GitHub 帐户凭据登录。

2.  在右上角，展开用户下拉菜单并进行选择**您的存储库**.

    ![The user menu is expanded with the Your repositories item selected.](media/2020-08-23-18-03-40.png "User menu, your repositories")

3.  在搜索标准旁边，定位并选择**新增功能**按钮。

    ![The GitHub Find a repository search criteria is shown with the New button selected.](media/2020-08-23-18-08-02.png "New repository button")

4.  在**创建新存储库**屏幕，命名存储库**法医学**并选择**创建存储库**按钮。

    ![Create a new repository page with Repository name field and Create repository button highlighted.](media/2020-08-23-18-11-38.png "Create a new repository")

5.  在**快速设置**屏幕，复制**赫特普斯**GitHub URL用于您的新存储库，将此存储库粘贴在记事本中供将来使用。

    ![Quick setup screen is displayed with the copy button next to the GitHub URL textbox selected.](media/2020-08-23-18-15-45.png "Quick setup screen")

6.  打开一个**新增功能**蔚蓝云壳控制台。 您可以通过选择**打开新会话**按钮从第一个控制台，或导航到<https://shell.azure.com>并使用相同的实验室凭据登录。

7.  导航到 Fab 医疗源代码文件夹并列出内容。

    ```bash
    cd ~/MCW-Cloud-native-applications/Hands-on\ lab/lab-files/developer/
    ls
    ```

    > **重要说明**：如果您将采用实验室的基础设施版本，而不是使用上述说明，则键入以下说明：
    >
    > ```bash
    > cd ~/MCW-Cloud-native-applications/Hands-on\ lab/lab-files/infrastructure/
    > ls
    > ```
    >
    > 这将带您到该版本的实验室将使用的启动文件的版本。

8.  您将看到列表包括三个文件夹，一个用于网站，另一个用于内容 API，另一个用于初始化 API 数据：

    ```bash
    content-api/
    content-init/
    content-web/
    ```

9.  设置您的用户名和电子邮件，git 用于提交。

    ```bash
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    ```

10. 使用云壳，初始化新的 git 存储库：

    ```bash
    git init
    git add .
    git commit -m "Initial Commit"
    ```

11. 通过发布以下命令将远程源设置为 GitHub URL：

    ```bash
    git remote add origin <your GitHub URL>
    ```

12. 配置 git CLI 以缓存您的凭据，这样您就不必继续重新键入凭据。

    ```bash
    git config --global --unset credential.helper
    git config --global credential.helper store
    ```

13. 通过发布以下命令向主分支推进：

    ```bash
    git push -u origin master
    ```

    > **注意**：如果您具有多重身份验证，则在使用云壳时需要创建个人访问令牌。请参阅以下链接以获取有关设置 GitHub 个人访问令牌以进行身份验证的帮助`git`与您的GitHub帐户：<https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token>.

    > **注意**：一旦您获得个人访问令牌，请重试上述命令，使用令牌作为密码。

14. 刷新 GitHub 存储库，您现在应该可以看到已发布的代码。

### <a id="task-7-connect-securely-to-the-build-agent">任务 7：安全地连接到构建代理</a>

在本节中，您验证可以连接到新的生成代理
虚拟市场。

1.  打开一个**新增功能**Azure 云壳牌控制台并运行以下命令，以查找运行 ARM 部署时提供的构建代理 VM 的 IP 地址：

    > **注意**：如果您没有可用的云壳，请参阅<a href="#task1">任务1：设置蔚蓝云壳</a>.

    ```bash
    az vm show -d -g fabmedical-[SUFFIX] -n fabmedical-[SHORT_SUFFIX] --query publicIps -o tsv
    ```

    例：

    ```bash
    az vm show -d -g fabmedical-sol -n fabmedical-SOL --query publicIps -o tsv
    ```

2.  在云壳输出中，请注意 VM 的公共 IP 地址。

    ![The cloud shell window is displayed with the Public IP address shown.](media/b4-2019-10-01_11-58-05.png "Azure Cloud Shell Public IP")

3.  连接到您通过键入以下命令创建的新 VM：

    ```bash
     ssh -i [PRIVATEKEYNAME] [BUILDAGENTUSERNAME]@[BUILDAGENTIP]
    ```

    替换命令中的括号值如下：

    -   `[PRIVATEKEYNAME]`：使用私钥名称`.ssh/fabmedical`，创建于上图。

    -   `[BUILDAGENTUSERNAME]`：在默认设置中使用VM的用户名`adminfabmedical`.

    -   `[BUILDAGENTIP]`：上一步检索的生成代理VM的IP地址。

    ```bash
    ssh -i .ssh/fabmedical adminfabmedical@52.174.141.11
    ```

4.  当被要求确认是否要连接时，由于无法验证连接的真实性，请键入`yes`.

5.  当要求您之前创建的私人密钥的密码短语时，请输入此值。

6.  SSH 连接到 VM 并显示以下命令提示。为下一步保持此云壳窗口打开：

    `adminfabmedical@fabmedical-SUFFIX:~$`

    ![In this screenshot of a Cloud Shell window, ssh -i .ssh/fabmedical adminfabmedical@52.174.141.11 has been typed and run at the command prompt. The information detailed above appears in the window.](media/b4-image27.png "Azure Cloud Shell Connect to Host")

> **注意**：如果连接有问题，您可能在ARM模板中错误地粘贴了SSH公钥。不幸的是，如果是这样的话，你将不得不重新创建VM并重试。

### <a id="task-8-complete-the-build-agent-setup">任务 8：完成构建代理设置</a>

在此任务中，您更新包并安装 Docker 引擎。

1.  转到向构建代理VM打开SSH连接的云壳窗口。

2.  更新 Ubuntu 封装，通过在单行命令中键入以下内容，在 HTTPS 上单步安装卷发和支持存储库。通过键入来响应`Y`并按下输入，如果问你是否愿意继续。

    ```bash
    sudo apt-get update && sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

    > **注意**：这是一条线。

3.  通过在单行命令中键入以下键入，添加 Docker 的官方 GPG 密钥：

    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

4.  通过在单行命令中键入以下项，将 Docker 的稳定存储库添加到 Ubuntu 包列表中：

    ```bash
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    ```

5.  添加节点Js PPA以使用节点JS LTS版本并更新Ubuntu封装，并通过键入以下命令（每个命令均在自己的线路上）安装Docker引擎、节点.js和节点包管理器。如果被问到是否要继续，请通过键入来回答`Y`并按下输入。

    ```bash
    sudo apt-get install curl python-software-properties -y

    curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

    sudo apt-get update && sudo apt-get install -y docker-ce nodejs mongodb-clients
    ```

6.  现在，通过在单行命令中键入以下软件包，将 Ubuntu 包升级到最新版本。

    ```bash
    sudo apt-get upgrade -y
    ```

7.  命令完成后，通过执行此命令检查安装的 Docker 版本。输出可能类似以下屏幕截图中显示的。请注意，服务器版本尚未显示，因为您没有使用提升的权限运行命令（即将解决）。

    ```bash
    docker version
    ```

    ![In this screenshot of a Cloud Shell window, docker version has been typed and run at the command prompt. Docker version information appears in the window.](media/docker-version.png "Display Docker version")

8.  您也可以使用以下命令检查节点的版本.js和 npm，只是为了信息目的：

    ```bash
    nodejs --version

    npm -version
    ```

9.  安装角CLI。

    ```bash
    sudo npm install -g @angular/cli
    ```

10. 要删除使用 sudo 的要求，请将您的用户添加到 Docker 组。您可以忽略在输出中看到的任何错误。

    ```bash
    sudo usermod -aG docker $USER
    ```

    ![In this screenshot of a Cloud Shell window, sudo usermod -aG docker $USER has been typed and run at the command prompt. Errors appear in the window.](media/b4-image29.png "Remove SUDO requirement")

11. 要使用户权限更改生效，请退出 SSH
    通过键入会话`exit`，然后按下\[&lt;进入>.使用SSH重新连接到生成代理VM，就像您在上一个任务中所做的那样。

    ```bash
    ssh -i .ssh/fabmedical adminfabmedical@52.174.141.11
    ```

12. 重复`docker version`命令，并注意输出现在显示服务器版本以及。

    ![In this screenshot of a Cloud Shell window, docker version has been typed and run at the command prompt. Docker version information appears in the window, in addition to server version information.](media/docker-version-server.png "Display Docker version")

13. 运行一些码头命令：

    -   一个看看是否有任何容器目前运行。

        ```bash
        docker container ls
        ```

    -   一个看看是否有任何容器存在，是否运行。

        ```bash
        docker container ls -a
        ```

14. 在这两种情况下，您都有一个空列表，但在运行命令时没有错误。您的构建代理已准备好，Docker 引擎运行正常。

    ![In this screenshot of a Cloud Shell window, docker container ls has been typed and run at the command prompt, as has the docker container ls -a command.](media/b4-image31.png "Display Docker container list")

### <a id="task-9-clone-repositories-to-the-build-agent">任务 9：生成代理的克隆存储库</a>

在此任务中，您从 GitHub 克隆存储库，以便您可以在构建代理上与他们合作。

1.  正如您以前在云壳中所做的那样，设置用于 git 提交的用户名和电子邮件。

    ```bash
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    ```

    > **注意**：在某些情况下，`root`用户拥有用户的`.config`文件夹。如果发生这种情况，运行以下命令以返回所有权`adminfabmedical`然后尝试`git`再次命令：
    >
    > ```bash
    > sudo chown -R $USER:$(id -gn $USER) /home/adminfabmedical/.config
    > ```

2.  配置 git CLI 以缓存您的凭据，这样您就不必保留凭据
    重新键入它们。

    ```bash
    git config --global credential.helper cache
    ```

    > **注意**：在某些情况下，`root`用户拥有用户的`.config`文件夹。如果发生这种情况，运行以下命令以返回所有权`adminfabmedical`然后尝试`git`再次命令：
    >
    > ```bash
    > sudo chown -R $USER:$(id -gn $USER) /home/adminfabmedical/.config
    > ```

3.  使用 GitHub URL 将存储库代码克隆到构建代理机器。

    ```bash
    git clone <GITHUB_REPOSITORY_URL>
    ```

    > **注意**：在某些情况下，`root`用户拥有用户的`.config`文件夹。如果发生这种情况，运行以下命令以返回所有权`adminfabmedical`然后尝试`git`再次命令：
    >
    > ```bash
    > sudo chown -R $USER:$(id -gn $USER) /home/adminfabmedical/.config
    > ```

您应该遵循提供的所有步骤_以前_执行动手实验室。

[logo]: https://github.com/Microsoft/MCW-Template-Cloud-Workshop/raw/master/Media/ms-cloud-workshop.png
