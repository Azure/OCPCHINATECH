最近爆出的在代码仓库中泄露密钥的新闻屡见不鲜，今儿我们就来聊聊如何在 Azure 中有效管理代码中的密钥。Azure 中的服务通常可以分为控制平面和数据平面，控制平面通常指资源的CRUD操作（比如创建xx Azure 资源服务），数据平面通常指与服务的数据连接（比如在 Azure Blob Storage 中做 Blob 的 CRUD 操作）。很多小伙伴常常把 RBAC (Role Based Access Control) 挂在嘴边，不过我相信很多小伙伴嘴中的 RBAC 更多指的是 Azure Resource 在控制平面的 RBAC。小伙伴试想一下如果我想通过一段代码自动化实现 Azure Resource 的 CRUD 管理，是不是这段代码内要放置身份信息和密码信息？同理，如果我们的应用程序希望与 Azure 的资源服务建立数据平面的数据连接，是不是这段代码内要放置连接字符串这类的密钥信息？为了上这些敏感的密钥信息安全存放和使用，有没有办法可以不在代码存放这些密钥，并可以使我们的程序正常使用这些密码？Azure Managed Identities 就是我们要找的答案，它可以实现托管式的身份密钥管理服务，Azure Managed Identities 服务通过服务节点(Endpoint)为授权的 Azure 服务返回访问密钥令牌，并通过对托管的身份密钥进行 RBAC 控制，从而实现在代码中无密访问 Azure 资源或数据连接 Azure 资源。除此之外 Azure 也提供非托管的身份服务，此时身份密钥的生命周期管理不由 Azure 提供托管，用户可以自行控制，其实现的功能与 Azure Managed Identities 是一致的。

下面的图示，帮助我们更好的理解 Azure Managed Identities。通常我们在具有代码计算能力的 Azure 服务中（如 VM，Webapp，Function 等）开启 Azure Managed Identities 服务，并且在待被前述服务消费的 Azure 服务中（如 Blob Storage, Key Vault, Resource Manager 等）为该 Identities 分配相应的 RBAC 角色，从而具有代码计算能力的 Azure 服务即可通过相应的 Identities 所具有的角色权限来消费目标 Azure 服务。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20%E6%89%98%E7%AE%A1%E8%BA%AB%E4%BB%BD%E6%9C%8D%E5%8A%A1%20--%20%E6%97%A0%E5%AF%86%E4%BB%A3%E7%A0%81%E8%AE%BF%E9%97%AE01.png)

有些小伙伴可能会好奇的问，无密代码？那密钥或令牌从哪里来啊？当我们把在相应服务中开启 Azure Managed Identities 后，该服务即可通过请求来获取令牌，然后通过该令牌来访问相应的服务。对应访问服务时所获得权限全部被通过令牌进行传递。下面图中以 Azure VM 服务为例，1-2. 首先在 Azure VM 中开启 Azure Managed Identities, 3. 创建的 Identities 被同步到 Azure Managed Identities 服务结点， 4. 在支持 Azure Managed Identities 访问的服务中为上一步中创建的 Identites 分配相应的权限，5-6. VM 内通过 Azure Managed Identities 服务结点获取令牌，7. VM 内代码通过步骤 5-6 获取的令牌对目标 Azure 服务发起访问。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20%E6%89%98%E7%AE%A1%E8%BA%AB%E4%BB%BD%E6%9C%8D%E5%8A%A1%20--%20%E6%97%A0%E5%AF%86%E4%BB%A3%E7%A0%81%E8%AE%BF%E9%97%AE02.png)

原理念叨完了，让我们用几个小栗子来找找感觉吧。

栗子1 ：通过无密代码访问 Azure KeyVault 服务获取 Secret

1. 准备一台虚拟机，在 Azure Portal 中为该虚拟机开启 Azure Managed Identities 服务

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20%E6%89%98%E7%AE%A1%E8%BA%AB%E4%BB%BD%E6%9C%8D%E5%8A%A1%20--%20%E6%97%A0%E5%AF%86%E4%BB%A3%E7%A0%81%E8%AE%BF%E9%97%AE03.png)

2. 在 Azure KeyVault 服务中，为步骤 1 创建的 Identities 分配角色权限（可参阅：https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/tutorial-linux-vm-access-nonaad）

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20%E6%89%98%E7%AE%A1%E8%BA%AB%E4%BB%BD%E6%9C%8D%E5%8A%A1%20--%20%E6%97%A0%E5%AF%86%E4%BB%A3%E7%A0%81%E8%AE%BF%E9%97%AE04.png)

3. Python 代码示例  

```
 1 from msrestazure.azure_active_directory import MSIAuthentication
 2 from msrestazure.azure_cloud import AZURE_CHINA_CLOUD
 3 from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
 4 from azure.keyvault import KeyVaultId
 5 
 6 #Get Access Token Using MSI Service, if Global Azure Ignore the cloud_environment parameters
 7 credentials = MSIAuthentication(cloud_environment = AZURE_CHINA_CLOUD, resource = "https://vault.azure.cn")
 8 
 9 #Create KeyVault Client Object Using MSI Token 
10 client = KeyVaultClient(credentials)
11 
12 #Get Secret which name is mdidemo
13 secret_bundle = client.get_secret("https://mdikv.vault.azure.cn/", "mdidemo", secret_version=KeyVaultId.version_none)
14 
15 #Print the Secret Result
16 print(secret_bundle.value)
```
 

栗子 2 ：通过无密代码访问 Azure Blob Storage 服务， 枚举 Blob Container 内 Blob

1. 准备一台虚拟机，在 Azure Portal 中为该虚拟机开启 Azure Managed Identities 服务，参考栗子 1

2. 在 Azure Storage Account 内为 Identities 分配角色权限（可参考：https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/tutorial-linux-vm-access-storage）

3. Python 代码示例  

```
 1 from msrestazure.azure_active_directory import MSIAuthentication
 2 from azure.storage.common import TokenCredential
 3 from azure.storage.blob import BlockBlobService
 4 
 5 #Get Azure Storage Token Using MSI
 6 credentials = MSIAuthentication(resource = "https://storage.azure.com/")
 7 
 8 #Create Azure Storage Access Token
 9 tokenCredential = TokenCredential(credentials.token['access_token'])
10 
11 #Create Azure Blob Serve Object
12 block_blob_service = BlockBlobService(account_name='adx', token_credential=tokenCredential)
13 
14 #List Container with Name 
15 generator = block_blob_service.list_blobs('mdidemo')
16 for blob in generator:
17     print("\t Blob name: " + blob.name)
```
 

吃了两个栗子，大家应该已经对无密代码访问基本掌握了，最后给大家说下 Azure Managed Identities 已经在中国 Azure 支持，正如上述栗子 1 中所示，但是并不是所有的支持服务已经在中国落地，具体哪些服务支持 Azure Managed Identities，可以查阅如下文档：https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/services-support-managed-identities。

 

参考资料：

1. Azure Managed Identities 概述：https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview

2. Azure Managed Identities 虚拟机获取令牌详解：https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-use-vm-token
