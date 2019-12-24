---
title: Week2 Azure-Level-200
date: 2019-10-22 22:01:40
type: Azure
---

第二周希望大家能够达到的学习效果：

- 以动手实验为主，学习Azure命令行工具的使用
- 能够部署Azure虚拟机的主要服务
- 能够进一步掌握Azure存储服务，并进行简单的操作
- 掌握Azure备份服务的概念和相关操作
- 掌握Sie Recovery站点恢复服务的概念和相关操作

### Section1 : Azure CLI的安装和使用

计划用时： 2小时

本部分主要内容：

1. 学习Azure CLI & Powershell的安装和使用
2. 利用Azure CLI & Powershell部署虚拟机

资料连接：

- Azure CLI安装：https://docs.microsoft.com/zh-cn/cli/azure/install-azure-cli?view=azure-cli-latest
- Azure Powershell的安装：https://docs.microsoft.com/zh-cn/powershell/azure/install-az-ps?view=azps-2.8.0
- 利用Azure CLI创建Linux虚拟机： https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/quick-create-cli
- 利用Powershell创建Linux虚拟机：https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/quick-create-powershell

### Section2：虚拟机简单操作

计划用时：4小时

本部分主要内容：

1. 为虚拟机创建并附加磁盘
2.  创建虚拟机映像
3.  为虚拟机配置可用性集
4.  创建虚拟机规模集

资料连接：

- 虚拟机磁盘管理：https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/tutorial-manage-disks
- 创建VM映像：https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/tutorial-custom-images
- 将虚拟机部署在可用性集中: https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/tutorial-availability-sets
- 创建规模集：https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/tutorial-create-vmss

### Section3 Azure存储简单操作

计划用时：2天

本部分主要内容：week1中我们已经了解到Azure存储的类型和它们之间的区别，本周要对每种存储类型进行深入了解，并学习如何对这些Azure存储进行简单操作。

1. 掌握Azure Blob存储的数据冗余、访问层&性能层
2. 学习Azure Blob存储的简单操作，学习使用AzCopy工具，并将本地数据迁移到云存储
3. 存储的数据迁移和导入导出方案
4.  学习Azure文件存储的简单操作

资料链接：

- Azure存储的数据冗余：https://docs.microsoft.com/zh-cn/azure/storage/common/storage-redundancy?toc=%2fazure%2fstorage%2fblobs%2ftoc.json

- Blob存储的访问层&性能层：

  访问层：https://docs.microsoft.com/zh-cn/azure/storage/blobs/storage-blob-storage-tiers

  性能层：https://docs.microsoft.com/zh-cn/azure/storage/blobs/storage-blob-performance-tiers

- 使用Blob存储在云中上传图片：https://docs.microsoft.com/zh-cn/azure/storage/blobs/storage-upload-process-images?tabs=dotnet

- 将本地数据迁移到云存储（AzCopy工具的使用）：

  https://docs.microsoft.com/zh-cn/azure/storage/common/storage-use-azcopy-migrate-on-premises-data?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=windows

- 数据传输解决方案：https://docs.microsoft.com/zh-cn/azure/storage/common/storage-choose-data-transfer-solution?toc=%2fazure%2fstorage%2fblobs%2ftoc.json

- 导入导出数据：https://docs.microsoft.com/zh-cn/azure/storage/common/storage-import-export-service?toc=%2fazure%2fstorage%2fblobs%2ftoc.json

- 使用Azure文件同步扩展Windows文件服务器：https://docs.microsoft.com/zh-cn/azure/storage/files/storage-sync-files-extend-servers

- Azure队列存储的使用：https://docs.microsoft.com/zh-cn/azure/storage/queues/storage-tutorial-queues?toc=%2fazure%2fstorage%2fqueues%2ftoc.json

- Azure表存储的使用：https://docs.microsoft.com/zh-cn/azure/storage/tables/table-storage-quickstart-portal

### Section4 Azure备份服务

计划用时：6小时

本部分主要内容：

1.  掌握Azure备份服务的功能和特别点
2.   学习Azure备份服务的简单使用
3.   了解Azaure备份服务器

资料链接：

- Azure备份服务介绍：https://docs.microsoft.com/zh-cn/azure/backup/backup-overview
-  Azure备份本地服务的方案大致有以下两种， 参考链接 [https://docs.azure.cn/zh-cn/backup/backup-overview#what-backup-scenarios-are-supported](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.azure.cn%2Fzh-cn%2Fbackup%2Fbackup-overview%23what-backup-scenarios-are-supported&data=02|01|Yi.Liang%40microsoft.com|c93ce11578f04643513708d756c99375|72f988bf86f141af91ab2d7cd011db47|1|0|637073296109259273&sdata=Q5vEeBDyQ0aHLbJ6ZKzCLYC5n12fU%2BdQWJ6DXWXV3OQ%3D&reserved=0)   
-  选择哪种备份方案，主要基于您需要备份什么内容？ 可参考《我应该使用哪个备份代理？》 [https://docs.azure.cn/zh-cn/backup/backup-overview#which-backup-agent-should-i-use](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.azure.cn%2Fzh-cn%2Fbackup%2Fbackup-overview%23which-backup-agent-should-i-use&data=02|01|Yi.Liang%40microsoft.com|c93ce11578f04643513708d756c99375|72f988bf86f141af91ab2d7cd011db47|1|0|637073296109269265&sdata=XtvSH478qH3YTj9gOYhbitQSR8N%2BZKVwbcT2bT4GgXE%3D&reserved=0)  
- 关于Azure备份服务器（MABS）信息，您可参考 ： [https://docs.azure.cn/zh-cn/backup/backup-azure-microsoft-azure-backup](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.azure.cn%2Fzh-cn%2Fbackup%2Fbackup-azure-microsoft-azure-backup&data=02|01|Yi.Liang%40microsoft.com|c93ce11578f04643513708d756c99375|72f988bf86f141af91ab2d7cd011db47|1|0|637073296109279269&sdata=mglt%2FaTPxrUkXtJwxOxLLX3dP3%2B0xBuXi5%2BU4I140JE%3D&reserved=0) 
- 在Azure VM上备份SQL Server：https://docs.microsoft.com/zh-cn/azure/backup/tutorial-sql-backup
- 备份Azure文件共享：https://docs.microsoft.com/zh-cn/azure/backup/tutorial-backup-azure-files

### Section5 Azure 站点恢复

计划用时：5小时

本部分主要内容：

1. 掌握Azure Site Recovery服务的功能和作用
2. 学习Azure上的灾难恢复和故障转移的部署和操作
3. 学习这对本地虚拟机的灾难恢复和故障转移的部署的操作
4. 使用Powershell配置灾难恢复的自动化操作

学习资料：

- Azure Site Recovery服务概述：https://docs.azure.cn/zh-cn/site-recovery/site-recovery-overview
- Azure上站点恢复的配置：https://docs.azure.cn/zh-cn/site-recovery/azure-to-azure-quickstart
- Azure区域之间的故障转移：https://docs.azure.cn/zh-cn/site-recovery/azure-to-azure-tutorial-failover-failback
- VMware/Hyper-V的灾难恢复演练: https://docs.azure.cn/zh-cn/site-recovery/tutorial-dr-drill-azure
- 将本地计算机迁移到Azure：https://docs.azure.cn/zh-cn/site-recovery/migrate-tutorial-on-premises-azure
- 灾难恢复的自动化操作：https://docs.azure.cn/zh-cn/site-recovery/azure-to-azure-powershell





