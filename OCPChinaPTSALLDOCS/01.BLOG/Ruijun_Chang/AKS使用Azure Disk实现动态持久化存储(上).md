上一篇文章中我们讲了[Azure如何使用Azure File实现动态持久化存储](https://www.cnblogs.com/changruijun/p/10941339.html)，这篇文章我们一起来实践下AKS如何使用Azure Disk实现动态持久化存储。
（1）准备集群环境
同上一篇一样，开始之前先创建好集群并升级CLI至最新版本。
（2）开始实践
每一个AKS集群中默认都有预创建好的两类storage classe，运行 kubectl get sc 查看如下：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(上)1.png)
除了第一个azurefile是上一篇文章中创建的一个类，default默认后端绑定的是Azure HDD 类型的磁盘，managed-premium 默认后端绑定的是SSD类型的磁盘。我们用managed-premium来创建一个PVC：
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: azure-managed-disk
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: managed-premium
  resources:
    requests:
      storage: 5Gi
```
创建一个pod，命名为mypod2，并将磁盘挂载到/data文件夹
```
kind: Pod
apiVersion: v1
metadata:
  name: mypod2
spec:
  containers:
  - name: mypod2
    image: nginx:1.15.5
    resources:
      requests:
        cpu: 100m
        memory: 128Mi
      limits:
        cpu: 250m
        memory: 256Mi
    volumeMounts:
    - mountPath: "/data"
      name: volume
  volumes:
    - name: volume
      persistentVolumeClaim:
        claimName: azure-managed-disk
```
执行kubectl apply -f azure-pvc-disk.yaml：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(上)2.png)

然后去pod中/data文件夹下创建一个名为hello的文件夹用于验证：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(上)3.png)


这时候我们回到portal页面上MC_开头的资源组里面刷新下，发现多了一个kubernetes-dynamic-pvc-开头的磁盘，名称就是上图中红框圈出来的卷名称，这是创建的时候自动命名的，点进去查看相关信息，磁盘所有者VM显示就是mypod2所在的node节点上：

 ![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(上)4.png)
 
 ![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(上)5.png)

最后我们用磁盘创建快照再生成一个新的磁盘，最后再挂载到新的pod上的方式来检验下磁盘同步是否成功：
```
#查找diskID，pvc-换成自己的
$ az disk list --query '[].id | [?contains(@,`pvc-faf0f176-8b8d-11e8-923b-deb28c58d242`)]' -o tsv
 
#创建快照
$ az snapshot create \
    --resource-group MC_myResourceGroup_myAKSCluster_eastus \
    --name pvcSnapshot \
    --source xxx #xxx部分换成上一个命令输出的diskID,类似
/subscriptions/<guid>/resourceGroups/MC_MYRESOURCEGROUP_MYAKSCLUSTER_EASTUS/providers/MicrosoftCompute/disks/kubernetes-dynamic-pvc-faf0f176-8b8d-11e8-923b-deb28c58d24
 
 
#创建新的磁盘
az disk create --resource-group MC_myResourceGroup_myAKSCluster_eastus --name pvcRestored --source pvcSnapshot
 
 
#拿到新的磁盘ID
az disk show --resource-group MC_myResourceGroup_myAKSCluster_eastus --name pvcRestored --query id -o tsv

```
用生成的新的磁盘ID挂载到新的pod上，yml文件如下：
```
kind: Pod
apiVersion: v1
metadata:
  name: mypod3
spec:
  containers:
  - name: mypod3
    image: nginx:1.15.5
    resources:
      requests:
        cpu: 100m
        memory: 128Mi
      limits:
        cpu: 250m
        memory: 256Mi
    volumeMounts:
    - mountPath: "/test"
      name: volume
  volumes:
    - name: volume
      azureDisk:
        kind: Managed
        diskName: pvcRestored
        diskURI: /subscriptions/<guid>/resourceGroups/MC_myResourceGroupAKS_myAKSCluster_eastus/providers/Microsoft.Compute/disks/pvcRestored
```
最后我们来检验下新的pod是否存在/test/hello文件夹：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(上)6.png)

验证没问题，至此我们实现了本节内容的目标，具体更详细的可以参考：https://docs.microsoft.com/en-us/azure/aks/azure-disks-dynamic-pv
下一篇文章我们将实践一个AKS上mysql使用Azure Disk做动态存储的过程。
