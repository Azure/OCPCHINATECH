现在的企业很多会采用NAS的方式来实现文档共享，便于大家协作。但是传统NAS有一个缺陷，就是只能在局域网内使用。如果要跨广域网，就需要在网络上做比较复杂的配置（例如虚拟二层）或者使用分布式架构的文件服务器（例如Windows DFS）等，带来了工作的不便。

Azure的Files Storage在Azure上提供了共享文件服务，虽然支持加密的SMB3.0可以跨广域网共享文件，但是网络连接的不稳定、对Linux版本需求、Internet端口要求等限制了直接在本地使用Azure File Storage作为广域网的NAS。

近期，Azure Files Storage推出了一个新的服务：File Sync，可以实现Azure Files Storage与本地Windows Server的文件同步，在此基础上，可以实现跨区域的NAS服务：

![images]()

基于File Sync，可实现如下功能：

* 云分层：Azure存放所有数据、本地只存放经常使用的热数据，降低存储成本
* 多站点同步：可在各地分支机构部署多台本地NAS，实现就近访问
* 快速容灾：本地NAS出现故障时，只需重新安装一台服务器，数据自动从云端同步回本地，无需备份恢复
* 直接云端访问：用户在办公室外，可以直接访问Azure Files Storage的文件
* 整合云端备份：可在云端统一对NAS文件进行备份，无需分支机构独立备份
* 下边就搭建一个Demo环境验证Fils Sync的功能。

# Demo环境架构

目前File Sync还未在Azure所有Region提供，已提供服务Region列表如下：

* 澳大利亚东部
* 澳大利亚东南部
* 加拿大中部
* 加拿大东部
* 印度中部
* 美国中部
* 东亚
* 美国东部
* 美国东部2
* 北欧
* 印度南部
* 东南亚
* 英国南部
* 英国西部
* 西欧
* 美国西部

本Demo环境使用东亚Region的Files Storage作为云端文件存储，并在美国西部和中国北2两个Region各创建一台Windows2016 Server模拟客户本地文件服务器，通过东亚Region的File Sync进行同步。

# Demo环境搭建

## Files Storage创建

Files Storage的创建很简单，按正常步骤创建资源组——存储账户——Files Storage即可，注意存储账户的类型需要选择“StorageV2 (常规用途 v2)”:

![images]()

![images]()

## 创建Azure文件同步

点击创建资源，搜索并创建Azure 文件同步：

![images]()

![images]()

# 部署文件服务器

在美国西部和中国北2各部署一台Windows2016 Server用做文件服务器：

![images]()

![images]()

按如下步骤分别如下在两台服务器安装同步软件：

打开Power Shell运行如下命令安装AzureRM模块：
```
Install-Module -Name AzureRM -AllowClobber
```

![images]()

修改安全配置，便与服务器通过IE访问外网：

![images]()

在IE打开如下网址：
Azure File Sync Agent

![images]()

点击Download选择合适版本下载安装：

![images]()

安装完成后运行：

![images]()

点击Sign in登录，然后按之前的配置选择相应的参数：

![images]()

点击Register注册服务器，需要再次登录Azure并完成服务器注册：

![images]()

到Azure Portal的同步服务-注册的服务器查看，可以看到两台服务器均已注册成功：

![images]()

## 配置同步

在存储同步服务-同步组中创建同步服务：

![images]()

选择之前创建的存储账户及Files Storage：

![images]()

创建完成进入同步组，可以看到已自动创建云终结点：

![images]()

添加服务器终结点（此处的保留空间意思为该卷最小的剩余空间）：

![images]()

此处要注意：

1. 服务器终结点的目录即为同步文件所放置的目录
2. 如果目录不存在将自动创建
3. 该目录所在文件系统必须为NTFS
4. 不建议放在系统盘，如果放在系统盘，高级功能例如云分层等将不能使用
5. 可以通过云分层方式，只将部分热点数据放在本地服务器，以节约本地存储购买空间

完成后状态如下：

![images]()

# Demo环境验证

## 同步验证

在FileServer01的同步目录（D:\filesync）新建一个文件file01：

![images]()

稍待片刻，可以看到FileServer02和Azure Files Storage都出现了同样文件，同步成功。

从任意一个点删除文件，也可以发现其他空间文件也自动删除。

## 云分层验证

在同步目录考入大文件：

![images]()

可以看到同步目录的容量已大于云分层设定的所在卷容量的20%（保留空间80%，6.99*（1-80%）=1.4GB）

![images]()

等到所有文件同步完成，自动启用云分层，减少本地文件的空间占用：

![images]()

总容量3.48GB的文件实际磁盘占用只有20MB，证明云分层生效。

# 总结

通过简单的测试，验证了File Sync功能实现多台Windows Server之间的文件同步及云分层的功能。

在Windows Server启用网络共享，即可实现本地的NAS服务，并且可以通过云端服务的方式，实现跨广域网的文件共享，有效的提升了办公效率，并节约了成本。
再结合AD用户权限管理，即搭建了一套完整的企业级多地NAS文件方案。

当然在生产环境真正实施时，还需考虑防火墙、防病毒等因素。File Sync解决了最关键的数据同步问题，并且由于云端是完整数据副本，可以集中在云端备份、容灾，大大降低了IT管理运维难度。

此方案还有一个缺点，即目前Azure Files Storage单个共享只有5TB空间，但是明年这个限制将大大提升，File Sync也将在所有Region发布，届时将极大简化跨区域NAS的部署。
