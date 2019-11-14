这篇文档不是原创，只是基于Azure官网上的Doc进行了相关链接的整理，从简单层面的安全设置，到更高层面的安全架构考量，以及Azure安全的白皮书及最佳实践，送给需要的你们，定有一款适合你！

# 做好数据的备份

为了确保数据的安全，尽量减少RPO，合理的规划数据的备份是非常必要的。目前在Azure中，针对虚机资源，包括虚机用到的数据磁盘，有如下几种备份方式：

## Azure 备份

若要备份运行生产工作负荷的 Azure VM，请使用 Azure 备份。 Azure 备份对 Windows 和Linux VM 均支持应用程序一致性备份。 Azure 备份可创建恢复点，这些恢复点存储在异地冗余的恢复保管库中。从恢复点还原时，可以还原整个 VM，也可以仅还原特定的文件。

教程：在 Azure 中备份和还原 Linux 虚拟机的文件 - https://docs.azure.cn/zh-cn/virtual-machines/linux/tutorial-backup-vms

教程：在 Azure 中备份和还原 Windows 虚拟机的文件 - https://docs.azure.cn/zh-cn/virtual-machines/windows/tutorial-backup-vms

 

## Azure Site Recovery

当整个区域因重大自然灾难或大规模服务中断而发生中断时，Azure Site Recovery 可以保护 VM，使其免受重大灾难影响。

教程：将 Azure VM 复制到另一个 Azure 区域 - https://docs.azure.cn/zh-cn/site-recovery/azure-to-azure-quickstart

 

## 托管快照

在开发和测试环境中，快照为使用托管磁盘的 VM 备份提供快速而又简单的选项。 托管快照是托管磁盘的只读完整副本。 快照独立于源磁盘而存在，并可用来新建用于重建 VM 的托管磁盘。 基于磁盘的已使用部分对快照进行计费。

教程：使用 Windows 中的快照创建作为托管磁盘存储的 VHD 的副本 -https://docs.azure.cn/zh-cn/virtual-machines/windows/snapshot-copy-managed-disk

教程：使用 Linux 中的快照创建作为托管磁盘存储的 VHD 的副本 - https://docs.azure.cn/zh-cn/virtual-machines/linux/snapshot-copy-managed-disk

教程：通过递增快照备份 Azure 非托管 VM 磁盘 - https://docs.azure.cn/zh-cn/virtual-machines/windows/incremental-snapshots

 

更多VM备份基础结构及原理请参阅 ：在 Azure 中计划 VM 备份基础结构 - https://docs.azure.cn/zh-cn/backup/backup-azure-vms-introduction

 

# 安全加固虚机资源

虚机目前还是云计算用户最常用的资源，保护好虚机的安全，也就确保了业务的稳定，Azure在针对Windows虚机，Linux虚机都提供了安全方面的最佳实践及建议，以及相应的Extension来保护你的虚机安全。

教程：适用于 Azure 云服务和虚拟机的 Microsoft 反恶意软件 - https://docs.azure.cn/zh-cn/security/azure-security-antimalware

教程：如何查询虚拟机流量异常及相关安全加固建议 - https://docs.azure.cn/zh-cn/articles/azure-operations-guide/virtual-machines/aog-virtual-machines-howto-query-abnormal-traffic-and-security-reinforce-recommendations

教程：针对虚机异常创建警报，以快速通知用户 - https://docs.azure.cn/zh-cn/virtual-machines/windows/tutorial-monitoring#create-alerts-1

教程：Linux虚拟机的安全加固 - https://docs.azure.cn/zh-cn/articles/azure-operations-guide/virtual-machines/linux/aog-virtual-machines-linux-security-reinforce

教程：Linux虚拟机的安全审计 - https://docs.azure.cn/zh-cn/articles/azure-operations-guide/virtual-machines/linux/aog-virtual-machines-linux-security-audit

教程：针对数据库资源的安全访问检查清单 - https://docs.microsoft.com/zh-cn/azure/security/azure-database-security-checklist

 

更多虚机方面的安全请参阅 ： Azure虚拟机安全概述 - https://docs.azure.cn/zh-cn/security/security-virtual-machines-overview

 

# 合理的规划网络安全性

网络是访问公有云资源的方式，合理的规划云端应用的网络结构，严格限制进出站流量的访问能力，尽可能将数据网络与管理网络分离，以提高云上资源的安全性。

教程：禁用对 Azure 虚拟机的 RDP/SSH 访问 - https://docs.azure.cn/zh-cn/security/azure-security-network-security-best-practices#%E7%A6%81%E7%94%A8%E5%AF%B9-azure-%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%9A%84-rdpssh-%E8%AE%BF%E9%97%AE

教程：尽可能少的对外暴露公网的访问，可通过负载均衡提供对外访问能力 - https://docs.azure.cn/zh-cn/security/azure-security-network-security-best-practices#%E5%9F%BA%E4%BA%8E-http-%E7%9A%84%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1

教程：以逻辑方式划分子网，并通过NSG来增加对进出子网及网络流量的权限控制 - https://docs.azure.cn/zh-cn/security/azure-security-network-security-best-practices#%E4%BB%A5%E9%80%BB%E8%BE%91%E6%96%B9%E5%BC%8F%E5%88%86%E6%AE%B5%E5%AD%90%E7%BD%91

教程：根据业务情况合理的使用虚拟网络设备，结合强制路由增加访问流量的安全性 - https://docs.azure.cn/zh-cn/security/azure-security-network-security-best-practices#%E4%BD%BF%E7%94%A8%E8%99%9A%E6%8B%9F%E7%BD%91%E7%BB%9C%E8%AE%BE%E5%A4%87

教程：通过Azure Marketplace中的镜像部署NVA设备 - https://market.azure.cn/zh-cn/marketplace/apps/category/security-identity?page=1

 

更多网络方面的最佳实践请参阅 ： Azure网络安全最佳实践 - https://docs.azure.cn/zh-cn/security/azure-security-network-security-best-practices#%E4%BD%BF%E7%94%A8%E8%99%9A%E6%8B%9F%E7%BD%91%E7%BB%9C%E8%AE%BE%E5%A4%87

 

# 开启诊断日志来收集更多的信息

Azure监控提供了包括Metrics及日志来帮助用户监控云端资源的使用情况，并可结合第三方的工具对日志进行更为具体的分析。目前针对Azure中提供的日志，主要包括活动日志和诊断日志，如果用户对于使用的服务有更多日志的需求，建议开启诊断日志，以收取更多的日志信息，以便日后分析需要。

教程：通过Azure Monitor，开启不同资源的诊断日志 - https://docs.azure.cn/zh-cn/monitoring-and-diagnostics/monitoring-overview-of-diagnostic-logs#enable-collection-of-resource-diagnostic-logs-in-the-portal

教程：根据订阅活动日志，发出警报 - https://docs.azure.cn/zh-cn/monitoring-and-diagnostics/monitor-quick-audit-notify-action-in-subscription

教程：AzureMonitor支持的合作伙伴List，以提高监控及分析能力 - https://docs.azure.cn/zh-cn/monitoring-and-diagnostics/monitoring-partners



# 制定相应的策略和规则

Azure管理员可以借助Azure Policy，通过制定并执行强制的各种规定规则，以尽量减少资源使用过程中误操作带来的风险。

教程：Azure策略概述 - https://docs.azure.cn/zh-cn/azure-policy/azure-policy-introduction

教程：创建和管理策略以强制实施符合性 - https://docs.azure.cn/zh-cn/azure-policy/create-manage-policy



从系统架构触发，提高云上应用的安全性

想要了解更多Azure中的安全指导规则，请参阅 ：Azure 中的安全管理 - https://docs.azure.cn/zh-cn/security/azure-security-management

想要了解数据存储层面的安全方法论，请参阅：Azure存储安全指南 - https://docs.azure.cn/zh-cn/storage/common/storage-security-guide

想要了解由21V运营的Azure公有云的安全准则，请参阅 ：Azure信任中心 - https://docs.azure.cn/zh-cn/security/security-microsoft-trust-center

想要了解更多Azure安全性方面的知识，请参阅：Azure 安全性 白皮书 - https://docs.microsoft.com/zh-cn/azure/security/security-white-papers

想要了解更多Azure安全方面用到的技术，请参阅：Azure 安全技术指南 - https://docs.microsoft.com/zh-cn/azure/security/security-overviews

想要结合不同的层面对现有架构进行修改，请参阅：Azure 安全最佳实践及模式 - https://docs.microsoft.com/zh-cn/azure/security/security-best-practices-and-patterns

想要了解Azure数据中心的安全性设计，请参阅：Azure基础结构安全性 - https://docs.microsoft.com/zh-cn/azure/security/azure-security-infrastructure
