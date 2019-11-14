前不久，Kubernetes社区刚刚官宣了其1.12版本正式GA，其中强调的两点功能更新之一 “Support for Azure Virtual Machine Scale Sets (VMSS) and Cluster-Autoscaler is Now Stable” ，意味着通过Azure中的VMSS，大家可以更为快速、灵活的去动态调整 Kubernetes 集群大小，今天在这里，以ACS-Engine为例，跟大家聊聊如何快速部署出支持VMSS的Kubernetes集群。



# 部署支持 VMSS 的ACS-Engine集群



部署支持 VMSS 的ACS-Engine集群很简单，所使用的ACS-Engine模板请参照：

```
{
  "apiVersion": "vlabs",
  "location": "chinaeast2",
  "properties": {
    "orchestratorProfile": {
      "orchestratorType": "Kubernetes",
      "orchestratorRelease": "1.12",
      "kubernetesConfig": {
        "addons": [
          {
            "name": "cluster-autoscaler",
            "enabled": true,
            "config": {
              "minNodes": "1",
              "maxNodes": "5"
            }
          }
        ]
      }
    },
    "masterProfile": {
      "count": 1,
      "dnsPrefix": "zjacsenginedemo01",
      "vmSize": "Standard_D2_v2"
    },
    "agentPoolProfiles": [
      {
        "name": "agentpool01",
        "count": 1,
        "vmSize": "Standard_D2_v2",
        "availabilityProfile": "VirtualMachineScaleSets"
      }
    ],
    "linuxProfile": {
      "adminUsername": "azureuser",
      "ssh": {
        "publicKeys": [
          {
            "keyData": "$your_private_key"
          }
        ]
      }
    },
    "servicePrincipalProfile": {
      "clientId": "$your_sp_id",
      "secret": "$your_sp_password"
    }
  }
}
```

接下来，按照官方步骤部署集群，请参照：

https://github.com/Azure/acs-engine/blob/master/docs/kubernetes/deploy.md#acs-engine-the-long-way



部署完成后，可以看到资源组中的构成如下：

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A401.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A402.webp)

VMSS已经创建出来，且包含一个实例，正是目前正在运行的Kubernetes Working Node ：

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A403.webp)

下面我们通过手动触发，完成VMSS的扩展 ：

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A404.webp)

可以看到，在数分钟之内，就可以将集群的Working Nodes进行横向扩展：

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A405.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A406.webp)

我们也可以通过VMSS的自动缩放机制，动态的根据VM资源的监控指标完成动态缩放：

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A407.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A408.webp)

![image](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E9%80%9A%E8%BF%87VMSS%E5%BF%AB%E9%80%9F%E7%BC%A9%E6%94%BEACS%20Engine%E9%9B%86%E7%BE%A409.webp)

# 实现原理



通过 VMSS 实现 Kubernetes 集群的自动缩放，其背后是开源项目 kubernetes/autoscaler 的功劳。



kubernetes/autoscaler 是Kubernetes中用于自动扩展&收缩集群Nodes的Add-On。其原理是 Cluster Autoscaler会定时的通过api-server去查询当前集群中的负载状态，当有Pods因为当前节点资源不足，导致创建失败，Cluster Autoscaler就会自动增加节点到集群中，以确保环境的稳定性；当其发现有Nodes在一段时间之内，工作负载很低，且其上没有重要的Pods，Cluster Autoscaler就会自动的去已出此节点，以减少资源的消耗。



Cluster Autoscaler 提供了丰富的配置，以防止重要的Pods（包括系统级的Pods，没有被Replica Controller管理，无其他可用Nodes，以及声明了"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"的Pods等）因为自动缩容，被删除却没有办法重建，影响应用的可用性。



Cluster Autoscaler 提供了丰富的配置，以标记节点是不能够被缩减的，可以通过"cluster-autoscaler.kubernetes.io/scale-down-disabled": "true"声明来防止节点在自动缩容过程中被删除。



Cluster Autoscaler 结合 Azure VMSS，我们既可以从Kubernetes集群出发，根据实际的资源调度负载来动态的去调整Working Nodes，也可以根据虚机的资源消耗，从Azure IaaS端完成集群节点的动态调整。同时，结合丰富的配置信息，可以合理的规划集群环境中，哪些节点是可以做扩缩容，哪些节点是需要固定使用，确保我们环境的灵活性。



目前，对于ACS-Engine，有两种主要的使用Cluster Autoscaler的方式，一种是Kubernetes的contral plane，仍然放在AvaliabilitySet中，提供相对固定的节点数量，针对working nodes，使用VMSS；另外一种是对Kubernetes的contral plane，和working nodes皆使用VMSS。



# 参考资料：

ACS Engine : https://github.com/Azure/acs-engine

Cluster Autoscaler (VMSS) Add-on in ACS Engine : https://github.com/Azure/acs-engine/blob/160dfa5620edcb5f3e02657467f9748e5f62d03d/examples/addons/cluster-autoscaler/README.md

kubernetes/autoscaler ：https://github.com/kubernetes/autoscaler

Support for Azure VMSS, Cluster-Autoscaler and User Assigned Identity ： https://kubernetes.io/blog/2018/10/08/support-for-azure-vmss--cluster-autoscaler-and-user-assigned-identity/

Frequently Asked Questions for Cluster Autoscaler :  https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md
