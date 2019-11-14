  随着企业业务的发展，会产生越来越多的数据。一般来说，企业数据遵的完整生命遵循『产生——使用——保存——销毁』的过程。而其中，数据的使用和保存阶段尤为重要。

  企业产生的数据在不同阶段会有不同的访问需求：
- 数据产生初期：频繁访问使用
- 数据保存期：非频繁使用，但需要随时可访问
- 数据归档期：偶尔访问，以读为主，容许一定的数据调用时间
  
  当企业数据量越来越大时，数据的保存方式、保存成本逐步成为企业的难题。所以，基于公有云的存储为企业提供了海量数据的廉价保存途径。而在云端，针对不同的访问需求，云端提供了不同的数据保存层，来满足企业对成本的要求。
  
  以Azure为例，Blob存储提供了热、冷、归档三层，对应不同的数据保存成本及访问成本。简单来说，数据保存成本从热到冷再到归档，越来越便宜；而对数据访问，冷层比热层高，归档层数据不能直接访问，需要先恢复到冷层或者热层。
  
  以医院的PACS系统为例，病人刚做完检查的前几天，PACS的图像资料需要经常查看，应放入热层；几天后（例如一周），有时需要做对比检查，但不会频繁访问，图像资料可以转为冷层；一个月后，病人就诊完成，按照法律规定，PACS资料需要存放7年，但只是在极少数情况（如医疗纠纷、法规性抽查等）需要访问，没有实时要求，这时候就应该下降到归档层。这样数据通过在不同存储层间的扭转，既满足了保存要求，又实现了较高的性价比。
  
  如何能让数据按需在不同存储层间转移？通常的做法是，写一段小程序，放到vm或者docker上，每天对保存的数据进行扫描，满足条件（保存到一定时间）的数据自动转移到下一层。当然，也可以通过Function等无服务器计算等方式来实现。但是这些方式要依赖于外部的计算环境，如果vm或docker出现问题，体系较为复杂，可靠性和客观理性都不够完善。
  
  而Azure现在提供了基于Azure Blob本身的数据生命周期管理功能，不用基于外部计算环境即可实现按策略的数据自动分层转移。现在就来看看数据生命周期如何配置管理。
  创建一个存储账户（数据生命周期管理支持Blob和V2两种存储账户），创建完成后在Blob服务里可以看到生命周期管理的选项：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理1.png)

  点击该选项进入，期初状态是空的，可以通过添加规则的方式来制定策略。规则的添加有两种方式：列表视图和代码视图：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理2.png)
  先按照列表视图添加规则：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理3.png)
  可以看到在一个规则里，可以执行的操作有：
- 将blob移入冷存储
- 将blob移入归档存储
- 删除blob
- 删除快照
  以医院PACS存储需求为例，可以制定如下规则：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理4.png)

  此外，还可以看到一页筛选器集：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理5.png)

  在这个页面，可以指定策略该策略对哪些数据生效，规则为Container/文件前缀（blob的虚拟文件夹可以看到做文件名前缀），例如如下规则指定了该策略对容器container01下test01开头的文件或文件夹下所有的文件生效：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理6.png)

  添加完规则回到列表视图，可以看到该规则：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理7.png)

  新添加的规则默认启用。
  切换到代码视图，可以看到规则其实是一段json文件：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理8.png)

  可以通过修改其中的值直接修改规则。例如把“Enabled”从“true”修改为“false”，保存后回到列表视图：
  
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images2/尘归尘土归土%EF%BC%8C一切为有法——Azure的数据生命周期管理9.png)
  该规则已经变为禁用状态，修改生效了。
  可以看到，基于Blob自身的生命周期管理，可以很方便的实现数据随时间自动迁移到对应层级甚至删除的目的。结合之前谈到的数据WORM保护，可以对数据整体生命周期做完善管理，简化我们的数据存储管理流程，降低数据保存成本。
  对于数据生命周期管理，使用的时候需要注意如下几点：
1. 只能实现数据向下迁移，向上迁移（如冷到热）需要手工操作
2. 在没有筛选器集时，规则对整个存储账户生效
3. 当出现规则冲突时（例如在同一时间，对数据同时有热到冷、热到归档），优先执行低成本的策略，即按照删除——转移到归档——转移到冷存储的优先级执行
4. 数据生命周期管理不产生额外的费用，但是会有列出Blob（用作枚举所有Blob的产生时间）和设置Blob层（Blob在不同存储层间转移）的费用
