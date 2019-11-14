如我们所知，Kubernetes通过 Volume 为集群中的容器提供存储，通过Persistent Volume 和 Persistent Volume Claim实现Volume 的静态供给和动态供给。Azure File和Azure Disk 也在Kubernetes 支持的动态供给 PV 的 Provisioner之列（如下图：https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner），本篇文章就带领大家操作一遍，如何动态创建Azure File 文件共享，以供集群中的多个Pod使用。
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储1.png)
 
### （1）准备工作：
按照上一篇文章中的步骤创建好一个AKS集群，并且升级Azure CLI到最新版本（[AKS初体验：创建集群并登录到node节点](https://www.cnblogs.com/changruijun/p/10930723.html)）；
登录到你创建好的集群中，确认下各Node节点状态是否正常：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储2.png)

### （2）添加StorageClass：
 创建一个azure-file-sc.yaml文件并编辑如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储3.png)

如上我们创建的这个Storage Class封装的名称（name）为azurefile, provisioner指定为kubernetes.io/azure-file，参数parameter部分，指定冗余形式，目前支持Standard的三张，其他暂不支持：
- Standard_LRS - standard locally redundant storage (LRS)
- Standard_GRS - standard geo-redundant storage (GRS)
- Standard_RAGRS - standard read-access geo-redundant storage (RA-GRS)
 创建好之后执行 kubectl apply -f azure-file-sc.yaml。
（3）创建集群角色并绑定
作为Azure平台上的服务，AKS仍然使用的RBAC去控制集群的权限和安全。为了使Azure平台能够创建所需要的存储资源，这一步我们需要添加一个集群角色：
```
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: system:azure-cloud-provider
rules:
- apiGroups: ['']
  resources: ['secrets']
  verbs:     ['get','create']
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: system:azure-cloud-provider
roleRef:
  kind: ClusterRole
  apiGroup: rbac.authorization.k8s.io
  name: system:azure-cloud-provider
subjects:
- kind: ServiceAccount
  name: persistent-volume-binder
  namespace: kube-system
```
执行kubectl apply -f azure-pvc-roles.yaml 如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储4.png)

（4）创建PVC：
这一步就是动态申请存储资源的文件了，命名这个PVC yaml文件为azure-file-pvc.yml，编辑如下，指定metadata为第（2）步中的StorageClassName,配置好访问模式和容量，编辑好保存并运行，可以看到这个PVC已经被成功创建。
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: azurefile
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: azurefile
  resources:
    requests:
      storage: 5Gi
```
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储5.png)

（5）使用并检验
首先我们创建一个pod,命令为mypod1.yml,这个pod运行的是一个busybox镜像，通过PVC将Azure File mount 到容器的/datatest目录中。
```
apiVersion: v1
kind: Pod
metadata:
  name: mypod1
spec:
  containers:
  - image: busybox
    name: mycontainer1
    volumeMounts:
    - mountPath: /datatest
      name: datatest
    args:
    - /bin/sh
    - -c
    - sleep 30000
  volumes:
  - name: datatest
    persistentVolumeClaim:
      claimName: my-azurefile-pvc
```
然后依次执行：
```
kubectl apply -f mypod1.yaml

#查看pod状态
kubectl get pod -o wide

#在pod里的datatest目录下创建一个名字为hello的文件
kubectl exec mypod1 touch /datatest/hello
```

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储6.png)

如上是截图，在pod中创建完名字为hello的文件后，我们检验下这个文件有没有更新到Azure File中，这里说明一下，AKS动态配置完后的AzureFile会默认创建在MC_的集群中，portal上找到这个存储账户进去，找到Azure File下面的文件，如截图，发现hello.txt已经存在了。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储7.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20File实现动态持久化存储8.png)
 

以上就是整个实验过程，演示了AKS如何使用Azure File实现动态持久化存储。希望对大家有用。
