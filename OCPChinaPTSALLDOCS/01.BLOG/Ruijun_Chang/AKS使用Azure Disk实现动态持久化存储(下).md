上一篇文章我们初步体验了AKS pod挂载Azure Disk的流程，这篇文章我们来正式部署一个mysql的服务来看下。
首先准备一个PVC，命名为mysql-pvc.yaml,内容如下：
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pvc
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: managed-premium
  resources:
    requests:
      storage: 32Gi
```
 编辑后执行:
```
kubectl apply -f mysql-pvc.yaml
```
完了部署mysql, 创建mysql.yml如下：
```
kind: Service
apiVersion: v1
metadata:
  name: mysql
spec:
  selector:
    app: mysql
  ports:
  - port: 3306
   
---
kind: Deployment
apiVersion: apps/v1beta1
metadata:
  name: mysql
spec:
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:5.6
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: password
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - mountPath: /var/lib/mysql
          name: volumeformysql
      volumes:
      - name: volumeformysql
        persistentVolumeClaim:
          claimName: mysql  
```
执行kubectl apply -f mysql.yml 后看到这个pod在node aks-agentpool-37075081-0上启动了，此时可以去portal上MC_开头的资源组里找到相应的azure 磁盘，概述中发现它是属于aks-agentpool-37075081-0这台VM。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)1.png)

 然后我们创建一个mysql-client的pod，进入该pod中简单创建一个数据库，命名为test，插入一条数据：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)2.png)


![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)3.png)

 接下来我们进入portal看下这个磁盘的监控情况：
 
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)4.png)

 然后我们在MC_开头的资源组找到aks-agentpool-37075081-0这台VM，手动关机，观察pod的状态，立即查看发现之前aks-agentpool-37075081-0上的两个pod的unknow了：
 
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)5.png)

与此同时另一个pod mysql-87585fdf4-r4zkj正在创建，这就是K8S集群的特点，能监控节点的运行状况，保证服务可用。（这里之所以mysql-client没有重新创建是因为创建的时候给它的属性就是挂掉了直接删除该pod）,过几分钟后我们重新查看，看到这个新的pod已经迁移到aks-agentpool-37075081-2上了：


![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)6.png)

执行kubectl describe pod mysql-87585fdf4-r4zkj：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)7.png)
 
再回到portal上查看磁盘，看到磁盘的所属VM已经更新为aks-agentpool-37075081-2：


![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)8.png)
 
然后去数据库里检查之前的数据是否完整：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/AKS使用Azure%20Disk实现动态持久化存储(下)9.png)

至此一个AKS上搭建Mysql，利用Azure Disk做持久化存储的实践就完成了。
