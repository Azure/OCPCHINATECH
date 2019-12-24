---
title: Week3 Azure-Level-200
date: 2019-10-22 23:00:40
type: Azure
---

第三周希望大家能够达到的学习效果：

- 本周主要针对Azure虚拟网络部分
- 进一步学习虚拟网络部分的产品及服务
- 对Azure虚拟网络主要服务进行部署和操作



### Section1 : 虚拟网络的简单操作

计划用时： 5小时

本部分主要内容：

1.  理解虚拟网络之间的默认路由规则
2.   理解虚拟网络几个主要概念和功能：网络安全组、用户自定义路由、服务终结点
3.  理解加速网络的原理和作用
4.  掌握虚拟网络之间、虚拟网络与本地之间的连接方案

资料连接：

- 网络安全组：https://docs.azure.cn/zh-cn/virtual-network/security-overview
- 虚拟网络路由规则：https://docs.azure.cn/zh-cn/virtual-network/virtual-networks-udr-overview
- 服务终结点：https://docs.azure.cn/zh-cn/virtual-network/virtual-network-service-endpoints-overview
- 加速网络：https://docs.azure.cn/zh-cn/virtual-network/create-vm-accelerated-networking-cli
- 创建虚拟网络对等互连：https://docs.azure.cn/zh-cn/virtual-network/tutorial-connect-virtual-networks-portal
- 配置VNet到VNet VPN网关连接: https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-howto-vnet-vnet-resource-manager-portal

### Section2：虚拟网络VPN网关

计划用时：1.5天

本部分主要内容：

1.  理解VPN网关的作用和原理
2.   部署VPN网关的连接：点到站点的连接，站点到站点的连接
3.  了解VPN网关的SKU（型号）
4.  了解VPN网关的监视和警报

资料连接：

- VPN网关概述：https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-about-vpngateways
- VPN网关SKU：https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-about-vpn-gateway-settings
- 什么是边界网关协议（BGP）：https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-bgp-overview
- 创建基于路由的VPN网关：https://docs.azure.cn/zh-cn/vpn-gateway/create-routebased-vpn-gateway-portal
- 配置站点到站点VPN连接：https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-portal
- VPN网关连接到本地VPN设备：https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-connect-multiple-policybased-rm-ps
- 配置点到站点的VPN连接：https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-howto-point-to-site-resource-manager-portal
- VPN网关基于指标设置警报：https://docs.azure.cn/zh-cn/vpn-gateway/vpn-gateway-howto-setup-alerts-virtual-network-gateway-metric

### Section3 虚拟网络ExpressRoute

计划用时：5小时

本部分主要内容：

1. 理解ExpressRoute功能及优势
2. 掌握ExpressRoute连接模型、部署方式
3. 了解ExpressRoute在多种场景下的使用方式

资料链接：

- ExpressRoute概述：https://docs.azure.cn/zh-cn/expressroute/expressroute-introduction
- ExpressRoute连接模型：https://docs.azure.cn/zh-cn/expressroute/expressroute-connectivity-models
- ExpressRoute线路和对等互连：https://docs.azure.cn/zh-cn/expressroute/expressroute-circuit-peerings
- 创建ExpressRoute：https://docs.azure.cn/zh-cn/articles/azure-operations-guide/expressroute/aog-expressroute-howto-create-through-azure-portal
- 将虚拟网络连接到ExpressRoute：https://docs.azure.cn/zh-cn/expressroute/expressroute-howto-linkvnet-portal-resource-manager
- ExpressRoute与VPN网关共存场景：https://docs.azure.cn/zh-cn/expressroute/expressroute-howto-coexist-resource-manager

### Section4 负载均衡器

计划用时：1天

本部分主要内容：

1.   理解负载均衡器的原理、作用和使用场景
2.   熟悉不同SKU负载均衡器之间的区别和限制
3.   掌握负载均衡器的部署方式

资料链接：

- 负载均衡器的概述：https://docs.azure.cn/zh-cn/load-balancer/load-balancer-overview
- 负载均衡器SKU（基本和标准）对比：https://docs.azure.cn/zh-cn/load-balancer/load-balancer-standard-overview
- 标准负载均衡器的创建：https://docs.azure.cn/zh-cn/load-balancer/quickstart-load-balancer-standard-public-portal
- 在负载均衡器中配置端口转发：https://docs.azure.cn/zh-cn/load-balancer/tutorial-load-balancer-port-forwarding-portal
- 负载均衡器运行状况探测原理：https://docs.azure.cn/zh-cn/load-balancer/load-balancer-custom-probe-overview
- 负载均衡器的分配模式：https://docs.azure.cn/zh-cn/load-balancer/load-balancer-distribution-mode
- Azure中的负载均衡服务：https://docs.azure.cn/zh-cn/traffic-manager/traffic-manager-load-balancing-azure?toc=%2fload-balancer%2ftoc.json

### Section5 应用程序网关

计划用时：5小时

本部分主要内容：

1. 理解应用程序网关的工作原理和使用场景
2. 掌握应用程序网关的SSL配置、WAF配置
3. 了解应用程序网关的运行状况探测

资料链接

- 应用程序网关概述：https://docs.azure.cn/zh-cn/application-gateway/overview
- 应用程序网关工作原理：https://docs.azure.cn/zh-cn/application-gateway/how-application-gateway-works
- 应用程序网关组件：https://docs.azure.cn/zh-cn/application-gateway/application-gateway-components
- 创建应用程序网关：https://docs.azure.cn/zh-cn/application-gateway/quick-create-portal
- SSL配置：https://docs.azure.cn/zh-cn/application-gateway/ssl-overview
- WAF配置：https://docs.azure.cn/zh-cn/application-gateway/waf-overview
- 运行状况探测：https://docs.azure.cn/zh-cn/application-gateway/application-gateway-probe-overview

### Section6  流量管理器

计划用时：2小时

主要内容：

1.  理解流量管理器的作用和工作原理
2.  掌握流量管理器的创建和使用场景

资料链接：

- 流量管理器概述：https://docs.azure.cn/zh-cn/traffic-manager/traffic-manager-overview
- 流量管理器工作原理：https://docs.azure.cn/zh-cn/traffic-manager/traffic-manager-how-it-works
- 流量管理器的创建：https://docs.azure.cn/zh-cn/traffic-manager/quickstart-create-traffic-manager-profile

### section7 CDN网络

计划用时：1小时

主要内容:

1. 理解CDN的功能及优势
2. 了解CND网络的创建
3. 了解CDN网络的管理方式

资料链接：

- CDN网络概述：https://docs.azure.cn/zh-cn/cdn/cdn-overview
- 节点分布：https://docs.azure.cn/zh-cn/cdn/cdn-pops
- CDN网络的创建：https://docs.azure.cn/zh-cn/cdn/cdn-how-to-use
- CDN网络控制台：https://docs.azure.cn/zh-cn/cdn/cdn-management-v2-portal-how-to-use

