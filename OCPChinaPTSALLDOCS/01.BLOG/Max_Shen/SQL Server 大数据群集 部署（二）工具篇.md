在进行部署大数据群集之前，先要安装一系列的工具，下表列出了常用的大数据群集工具以及如何安装它们：

| 工具 | Required |	Description |	安装 |
| ---- | ---- |	---- |	---- |
| mssqlctl | 	用户帐户控制 |	用于安装和管理大数据群集的命令行工具。 |	[安装](https://docs.microsoft.com/zh-cn/sql/big-data-cluster/deploy-install-mssqlctl?view=sqlallproducts-allversions) |
| kubectl1	| 用户帐户控制 |	监视基础 Kuberentes 群集的命令行工具 ([详细信息](https://kubernetes.io/docs/tasks/tools/install-kubectl/))。 |	[Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-powershell-from-psgallery) / [Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-using-native-package-management) |
| Azure Data Studio |	用户帐户控制 |	用于查询 SQL Server 的跨平台图形化工具 ([详细信息](https://docs.microsoft.com/zh-cn/sql/azure-data-studio/what-is?view=sql-server-ver15))。 |	[安装](https://docs.microsoft.com/zh-cn/sql/azure-data-studio/download?view=sqlallproducts-allversions) |
| SQL Server 2019 扩展	| 用户帐户控制 |	适用于支持连接到大数据群集的 Azure Data Studio 的扩展。 此外提供了数据虚拟化向导。 |	[安装](https://docs.microsoft.com/zh-cn/sql/azure-data-studio/sql-server-2019-extension?view=sqlallproducts-allversions) |
| Azure CLI2	| 适用于 AKS |	用于管理 Azure 服务的新式命令行界面。 与 AKS 的大数据群集部署一起使用 ([详细信息](https://docs.microsoft.com/zh-cn/cli/azure/?view=azure-cli-latest))。 |	[安装](https://docs.microsoft.com/zh-cn/cli/azure/install-azure-cli?view=azure-cli-latest) |
| mssql-cli	| 可选 |	新式命令行接口，用于查询 SQL Server ([详细信息](https://github.com/dbcli/mssql-cli/blob/master/README.rst))。 |	[Windows](https://github.com/dbcli/mssql-cli/blob/master/doc/installation/windows.md) / [Linux](https://github.com/dbcli/mssql-cli/blob/master/doc/installation/linux.md) |
| sqlcmd	| 对于某些脚本 |	用于查询 SQL Server 的传统命令行工具 ([详细信息](https://docs.microsoft.com/zh-cn/sql/tools/sqlcmd-utility?view=sql-server-ver15))。 |	[Windows](https://www.microsoft.com/en-us/download/details.aspx?id=36433) / [Linux](https://docs.microsoft.com/zh-cn/sql/linux/sql-server-linux-setup-tools?view=sqlallproducts-allversions) |
| curl 3	| 对于某些脚本 |	将使用的 Url 的数据传输的命令行工具。 |	[Windows](https://curl.haxx.se/windows/) / Linux： 安装 curl 包 |
 

# 需要哪些工具？

上表提供了所有与大数据群集配合使用的常见工具。 所需的工具取决于你的方案。 但一般情况下，以下工具是最重要的管理、 连接和查询群集：

* mssqlctl

* kubectl

* Azure Data Studio

* SQL Server 2019 扩展

# 安装过程

1、首先要安装mssqlctl，这个工具先要安装python，在python 官方网站 https://www.python.org/downloads/release/python-372/ 下载最新版的python，

2、安装时需要加上path路径，完成后最好重启电脑，否则路径不一定生效。

3、运行

pip3 install --extra-index-url https://private-repo.microsoft.com/python/ctp-2.2 mssqlctl       
正常结果如下图：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/SQL%20Server%20%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%BE%A4%E9%9B%86%20%E9%83%A8%E7%BD%B2%EF%BC%88%E4%BA%8C%EF%BC%89%E5%B7%A5%E5%85%B7%E7%AF%8701.png)

4、mssqlctl安装完成后安装**kubectl** ，安装kubectl还比较麻烦，不知道什么原因，我用powershell进行安装，却报告无法进行数字签名。

```
Install-Script -Name install-kubectl -Scope CurrentUser -Force
install-kubectl.ps1 -downloadlocation D:\Program Files\k8s

————————————————————————
install-kubectl.ps1 : 无法加载文件 C:\Users\maxshen\Documents\WindowsPowerShell\Scripts\install-kubectl.ps1。未对文件 C
:\Users\maxshen\Documents\WindowsPowerShell\Scripts\install-kubectl.ps1 进行数字签名。无法在当前系统上运行该脚本。有关
运行脚本和设置执行策略的详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 1
+ install-kubectl.ps1 -downloadlocation D:\Program Files\k8s
+ ~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

5、执行

```
Set-ExecutionPolicy Bypass -Scope Process
再执行
install-kubectl.ps1 -downloadlocation D:\Program Files\k8s 
安装成功后
cmd执行
kubectl.exe version
```

6、安装 azure data studio， 这个比较简单，下载相应的安装包安装即可。 https://docs.microsoft.com/zh-cn/sql/azure-data-studio/download?view=sqlallproducts-allversions

7、安装SQL SERVER 2019在azure data studio的扩展。这个也比较简单：https://docs.microsoft.com/zh-cn/sql/azure-data-studio/sql-server-2019-extension?view=sqlallproducts-allversions

8、另外还可以安装mssql-cli，SQLCMD,CURL工具，

```
安装mssql-cli
pip install mssql-cli

SQLCMD下载安装 
https://www.microsoft.com/zh-cn/download/confirmation.aspx?id=36433
现在安装curl
https://curl.haxx.se/windows/
```

 

在某些情况下仅需要其余的工具。 **Azure CLI**可用于管理与 AKS 部署关联的 Azure 服务。 **mssql cli**是一种可选的但有用的工具，可用于连接到群集中的 SQL Server 主实例和从命令行运行查询。 并**sqlcmd**并**curl**是必需的，特别是要使用 GitHub 脚本安装示例数据。

**这篇还没进入正题， 从工具来看，就会发现这件事情其实蛮复杂。对搞SQL Server的朋友提出了更加高的技术要求，下一篇开始安装学习AKS**
