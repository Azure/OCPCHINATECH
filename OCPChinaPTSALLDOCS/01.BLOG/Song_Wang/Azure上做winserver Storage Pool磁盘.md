很多企业客户在Azure VM上使用winserver，会使用到存储池的feature，存储池也是建立在一定数量的物理磁盘的基础之上的，将一定数量未使用的物理磁盘（physical disk）添加到存储池（storage pool）中，形成一定数量的虚拟磁盘（virtual disk），然后针对虚拟磁盘进行新建卷（简单卷、镜像卷等)的操作。可以用来搭建极其灵活、复杂的具有高容错能力、高性能存储系统，存储池如下：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9801.png)

当存储池所在VM挂掉或者当前VM不足以支撑业务使用的时候，存储池磁盘是否可以直接迁移，如下针对于上述问题做了测试。

1. Attach三块磁盘到VM上，200GB，500GB，1TB，按照向导新建存储池，这里最关键的就是复原类型（resiliency type），不同的复原类型有不同的冗余度、读写性能。有三种复原类型：分别是简单（simple）、镜像（mirror）、奇偶校验（parity）。其中镜像分成双向镜像（two-way mirror）、三向镜像（three-way mirror），三向镜像至少需要5块硬盘，具体细节见Technet：https://social.technet.microsoft.com/wiki/contents/articles/15200.storage-spaces-designing-for-performance.aspx

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9802.png)

2. 创建虚拟磁盘，并格式化分区，进入电脑可以看到新建卷
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9803.png)
 
3. 如下是在winserver针对于存储池的显示。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9804.png)

4. 关闭改VM进行磁盘分离：
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9805.png)

5. 在一台新Windows VM上，直接attach三块磁盘

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9806.png)

6. 进入电脑里可以看到没有任何操作，新建卷跟之前VM里显示一致，存储池所有信息也一致。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9807.png)
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%E4%B8%8A%E5%81%9Awinserver%20Storage%20Pool%E7%A3%81%E7%9B%9808.png)
 



 

总结：

1. Windows存储池对磁盘进行设置，信息就在磁盘和OS盘上，当attach到新的VM上，会扫描磁盘的配置文件，记录到OS盘里，从而保持设置数据磁盘等信息一致

2. 比on promise迁移数据更加方便，不受限于 机器的大小，当VM本身无法支撑业务时候，可以直接迁移

3. 如果磁盘分离迁移请遵从程序，关机，分离，attach到新机器，开机，磁盘的信息设置成功None，如果是读写，虽然读写速度加快，但因为数据在缓存里，有可能会有一定数据丢失。

4. Linux Raid对磁盘操作类似，分离attach也可以
