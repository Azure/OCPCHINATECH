  美国安然事件后，电子数据的合规性保存越来越受到重视；各国政府制定了一系列的法律，如美国《赛班斯法案》等，对于不同类型的电子数据保留期限做了严格规定；国内也没落后，以医疗行业为例，《电子病历基本规范》等一系列法规，规定了不同类型医疗数据的保留周期，其他行业也如此。

  电子数据的保留，不只是将数据存起来，还需要做到在规定的期限内防篡改（增删改等操作），才满足合规性要求。从存储角度来看，这就是经常提到的WORM（Write Once， Read Many ）。
  随着越来越多用户将数据长期保留在公有云，Azure也引入了不可变Blob的服务，来实现对数据的WORM保护。
## 合规性
  数据WORM保护并不是简单的说自己满足就可以，而是要经过相关法规认证，才能通过审计。
  Azure的不可变Blob满足SEC 17a-4(f)、CFTC 1.31(d)、FINRA 和其他法规要求。在国内，虽然还没有明确的相应法规，但AzureChina也已经引入WORM保护的服务。
## 保护范围
保护对象：WORM保护针对的对象是Block Blob。Append Blob及Page Blob由于其特性，不满足WORM保护需求
保护颗粒度：以容器为单位，WORM保护对容器内所有对象同时生效
适用存储账户：Blob存储账户及通用存储账户v2可以实施WORM保护，通用存储账户v1目前还没有WORM功能，但可以升级为通用存储账户v2来实现此功能
## 配置过程
  Azure的WORM保护分为两种类型：基于时间的保留和依法保留。对一个容器，既可以配置其中一种策略，也可以两种都配置。
  WORM保护的配置很简单，进入创建好的容器里，在访问策略里添加策略即可：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%201.png)

### 依法保留
  首先添加一个依法保留的策略，在添加策略的下拉框选择依法保留：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%202.png)

  依法保留的意义是按照某种规定防止数据被篡改，例如临时需要将一个数据锁定，但没有固定期限，直到取消；为了记录保留数据的原因，需要添加至少一个标记：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%203.png)

  添加完成，可以在不可变存储的策略中看到：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护4.png)

  现在给容器中上传一个数据，以一个文本文件为例：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%205.png)

  可以看到文件可正确上传。
  现删除文件：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%206.png)

  发现由于启用了WORM保护，无法删除：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%207.png)

  更新文件元数据也不成功：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%208.png)

  编辑文件，仍然失败：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%209.png)

  现在上传一个同名文件来覆盖原文件：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2023.png)

  还是失败：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2010.png)

  从如上测试可以看出，在启用了WORM保护的容器里，文件只能上传，不能被修改删除或覆盖，有效保证了原始数据安全。
  那么依法保留的生命周期是多久？如下可以看到，依法保留的策略可以编辑：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2011.png)

  在编辑页面，可以对该策略的标记进行增加或删除：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2012.png)

  当一个策略所有的标记被删除时，该策略被自动删除。
  问题来了，如果一个有操作权限的人员删除策略后修改了原始文件，然后在加上策略，是否就意味着WORM保护失效？现在将容器里的文件删除并重新加上相同的依法保留策略。虽然操作没问题，但是在存储账户的日志里，记录下了所有操作：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2013.png)

  并且在每条日志的详细信息里均可看到操作人员：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2014.png)

  所以合规性审计时，并不只是简单的查看是否启用了策略，还要检查日志，确认是否有非法操作。
### 基于时间的保留
  另一种WORM保护的策略是基于时间的保留：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2015.png)

  基于时间的保留需要设置需要设置一个保留期，以天为单位，范围是1——146000，即保留期为1天到400年。
  设置好基于时间的保留后，会立即生效，但是状态为已解锁：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2016.png)

  此时可随意编辑策略（修改保留期）甚至删除策略：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2017.png)

  这相当于给了一个反悔期（当然所有操作仍然会被记录）。但是如果选择锁定策略并确认后：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2018.png)
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2019.png)

  策略的状态变为已锁定：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2020.png)

  策略不可删除，只能编辑：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2021.png)

  但是编辑的次数不能超过5次，并且保留期只能增加不能减少：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/你可以保持沉默%EF%BC%8C但你所说的一切都将成为呈堂证供——浅谈Azure%20WORM保护%2022.png)

  还有一点需注意，保留期满后，数据仍然不可修改，只能删除。
### 多策略
  当为一个容器同时设置两种类型的策略时，将同时生效，例如：
- 任意一个策略有效：数据不能做任何修改
- 两种策略都失效：收基于时间保留的影响，数据只能删除不能修改
### 数据分层的影响
  受WORM保护的数据，仍可以在热、冷、归档三层中任意转换，不影响保留策略；也如同没有WORM保护的数据，放入归档层后不能直接访问，需要恢复到热层或冷层。
### 总结
  经过测试可以看出，Azure的WORM功能可有效提供数据保护，作为审计的依据；结合数据分层功能，可作为用户长期低成本合规保存数据的地方。
