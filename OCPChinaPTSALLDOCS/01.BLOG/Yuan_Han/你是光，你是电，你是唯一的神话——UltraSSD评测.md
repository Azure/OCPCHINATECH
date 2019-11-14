Azure的磁盘存储性能一直被诟病，所幸去年7月在 LasVegas 的 MS Ready 上，我软的颜值担当 Mark Russinovich宣布了新一代 Azure 高性能存储——UltraSSD。
  经过一年的准备，UltraSSD 马上就要正式面世，下边就对这个希望之星进行一个评测。
## UltraSSD 简介
  UltraSSD 摒弃了 Azure 以前的存储架构，将 NVMe 的 SSD整合成 JBOD，然后使用 PCIe 总线连接至计算节点，类似于将 FusionIO 卡做了外置，和 EMC 一款夭折的产品 DSSD有异曲同工之处。这个架构在路径和协议上使得存储和内存尽可能靠近，达到性能最大化。
  与以往的 Azure 存储相比较，UltraSSD 具备如下特性：
- 大容量：最大容量可达64TB
- 高性能：延时低于1ms，最大 IOPS 达到160,000，最大带宽达到2GB/s
- 性能可调节：对于固定容量为的磁盘，IOPS 可在100-300*容量（GiB）之间调整，满足客户性能和成本要求的最佳化
- 支持多读多写：同一块磁盘可挂给多台 vm 同时读写，可实现 cluster 机制
## UltraSSD 性能分析
  当然，对 UltraSSD 最重要的特点就是性能。与友商对比，UltraSSD 可以说是遥遥领先（AWS 最大 IOPS 为64000，最大带宽为1000MB/s）。
  与以往不同容量固定的性能指标不一样，UltraSSD 的性能指标是可配置的，配置规则如下：
- UltraSSD 的容量从4GiB 起配，容量阶梯为4、8、16、32、64、128、256、512、1024GiB，到1TiB 后，以1TiB 为单位增长，最大到64TiB
- 对各种容量的 UltraSSD，IOPS在创建时指定，最小值为100，最大为值300*容量 GiB；例如128GiB 的 UltraSSD，最小 IOPS 为100，最大可到300*128=38,400；但最大 IOPS 不能超过160,000，容量为512GiB 可以达到153,600，接近最大值，容量为1024GiB（1TiB）即可达到 IOPS 的最大值160,000；对于一些对 IOPS 和延时要求高而容量要求低的应用（如 DB 的 redo log），可以用很小容量盘即可满足性能需求
- 带宽的计算比较复杂，UltraSSD 的最小带宽为1MiB，最大值为256kBiops，但不能超过2000MBps；但在实际创建 UltraSSD 时，因为每个数据块大小不能低于4kB，所以带宽的最小值不能低于4kB\iops
  具体性能指标如下：

## UltraSSD实测
### UltraSSD 创建
  目前，UltraSSD 还处于内测阶段，所以需要先申请，申请地址如下：
  [UltraSSD 内测申请](https://login.microsoftonline.com/common/oauth2/authorize?response_mode=form_post&response_type=id_token+code&scope=openid&mkt=zh-CN&msafed=0&nonce=f0df767a-5499-4868-92cf-7cf53fb61181.637046683157505119&state=https%3a%2f%2fforms.office.com%2fPages%2fResponsePage.aspx%3fid%3dv4j5cvGGr0GRqy180BHbRy7CEei_TctErHiOyhrn9QRURFlSUUVMUFJOVzRaWTFIQjJGNU83UDVHWS4u&client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3a%2f%2fforms.office.com%2fauth%2fsignin&sso_nonce=AQABAAAAAAAP0wLlqdLVToOpA4kwzSnxOxcelE2l0dJh-Nf5uIKd4yKw8BQI8Q8oPuSits4QB2zUFt0XJAiRZ4Sb2JbZZXQt2CvPFQER37Ibp-kuf9lsxyAA&client-request-id=1e1e4005-3311-4371-ba31-e3fb51262f74&mscrid=1e1e4005-3311-4371-ba31-e3fb51262f74)
  内测期间有如下限制：
- 只在 East US2 Region 开放
- 必须使用 Availability Zone（AZ）
- 只能在 ESv3、DSv3 机型使用
- 只能用作数据盘，不能用作 OS 盘
- 只能创建空白磁盘，不能从其他磁盘或快照等创建
- 尚不支持磁盘快照、VM 映像、可用性集、虚拟机规模集和 Azure 磁盘加密、ASR 等高级功能
- 目前只能使用 Azure 资源管理器模板、CLI 和 Python SDK 进行部署
  下边使用 CLI 创建 UltraSSD。
  首先检查 AZ 功能是否已经注册(state 为 Registered)：
```
az feature show --namespace Microsoft.Resources --name AvailabilityZones
```

  如果没有注册，请按如下方式注册（需要大约 1、2 小时完成注册）：
```
az feature register --namespace Microsoft.Resources --name AvailabilityZones
az provider register -n Microsoft.Resources
```
  检查是否已激活 UltraSSD 功能：
```
az vm list-skus --resource-type disks -o table |grep 'UltraSSD'
```
  在 East US2 的 Zone1、Zone3 已激活 UltraSSD 功能
  创建 UltraSSD 的方式有两种：
创建 vm 时直接附加一块 UltraSSD 作为数据盘，但是只能指定大小，不能指定性能，性能为默认的 iops500，带宽 8MiB
单独创建空白 UltraSSD，可以指定 iops 及带宽指标
  现在 Zone1 创建一块空白的 128GiB UltraSSD：
```
az disk create -g ultrademo -n disk01 --sku UltraSSD_LRS --size-gb 128 --zone 1
```
  由于没有指定性能指标，可以看到默认的 iops 为 500，带宽为 8MiB
  再创建一块 128GiB UltraSSD，IOPS 为 10000（如上所述，128GiB UltraSSD 的 IOPS 范围为 100——300*128）：
```
az disk create -g ultrademo -n disk02 --sku UltraSSD_LRS --size-gb 1
28 --disk-iops-read-write 10000 --zone 1
```
  却出现报错。
  检查原因，因为 UltraSSD 使用 4K 作为最小块，所以当 IOPS 为 10000 时，对应带宽至少为 4k*1000=40MBps，超过了默认的 8MiB，创建时需要将带宽指定到支持范围内。
  重新创建一遍，指定 IOPS 为 10000，带宽 50MB：
```
az disk create -g ultrademo -n disk02 --sku UltraSSD_LRS --size-gb 128 --disk-iops-read-write 10000 --disk-mbps-read-write 50 --zone 1
```
  这次创建成功。
### 创建 vm 并附加 UltraSSD
  如上所述，目前只有 ESv3 及 DSv3 系列 vm 支持 UltraSSD。除此之外，还需要注意：
vm 与 UlatraSSD 必须在一个 Zone
创建 vm 时必须激活 UltraSSD 支持，创建完成后不能修改
磁盘的性能不止受磁盘限制，同时也受到 vm 自身的限；vm 的限制如下：


### 创建 vm
  目前在 Portal 创建 vm 虽然有激活 UltraSSD 的选项：

  但因为此功能未正式开启，所以显示为灰色，不能直接使用，需要用 cli 去创建：
```
az vm create -g ultrademo -n vm01 --image MicrosoftWindowsServer:WindowsServer:2016-Datacenter-smalldisk:2016.127.20190314 --size Standard_E32-8s_v3 --ultra-ssd-enabled true --admin-username vm --admin-password 'Password=123' --nsg-rule rdp --zone 1
```
### 附加 UltraSSD
  现在将创建好的 disk02 附加到 vm01 上；如同添加普通磁盘，可以直接 Portal 里 vm 的 disk 选项里添加：

## UltraSSD 性能测试
  从 vm 性能的列表中可以看到，上边创建的 E32s 可以达到 51,200 的 iops，而我们创建的 UltraSSD 指定的 IOPS 为 10,000，理论上可以达到指定性能的上限。现在测试一下是否真能达到理论值。
### IOPS 测试
  用远程桌面连接至 vm01，将新加的 disk02 初始化并格式化，自动装载为 F 盘：

  测试工具还是选用老牌的 iometer，数据量 20GB：

  读写模型为 8k 数据块，读写各一半，全随机，模拟数据库：

  20GB 的测试数据准备需要一段时间，正式开始测试后可以看到实时测试结果：

  可以看到，iops 没有达到预期的 10000。检查原因，因为创建 disk02 时，指定了带宽为 50MBps，而测试使用 8KB 的数据块，所以收到带宽限制，iops 最大只能到 501000/8=6250，与测试结果匹配。
  为了达到 10000 的 IOPS，带宽应该不低于 810000/1000=80MB。
  UltraSSD 有一个较好的特性，支持在线调整性能参数，现在将带宽设置为 100MB：
```
az disk update -g ultrademo -n disk02 --disk-mbps-read-write 100
```
  调整后，大约需要 1、2 小时的生效时间，所以结果不会马上变化，需要有个等待时间。
  稍待片刻后，可以看到新的测试结果：

  可以看到 IOPS 已经达到 10000 以上：

  平均延时低于 1ms：

  对应此时带宽也达到了 iops 上限 8*10000=80MBps：

### 带宽测试
  带宽一般是针对大数据块，Azure 磁盘带宽测试标准为 64KB 数据块，可以计算 2000*1000/64=31,250，即 IOPS 不能小于 31,250。
  现在修改 disk02 的性能参数，iops 提升到 32000，带宽提升到 2000：
```
az disk update -g ultrademo -n disk02 --disk-mbps-read-write 2000 --disk-iops-read-write 32000
```
  Iometer 的读写模型设置为 64K 数据块：

  为了高并发，需要将#of Outstanding I/Os 设置为 2，测试结构如下：

  没有达到我们的期望值，只有 785MBps。实际原因是 E32s 的 vm 自身的限制：

  为了充分发挥 UltraSSD 的性能，Azure 专门推出了一款 vm：

## UltraSSD 价格
  相对于其他磁盘，UltraSSD 的收费模式也有变化，总体来说要考虑容量、性能、vm 几个方面做综合的价格。计算模式如下（Preview 阶段参考，GA 后才有正式价格）：

  已刚才创建的 disk02 为例，价格计算如下：
- 容量价格：$0.000082*128=$0.010496/hout
- IOPS 价格：$0.000034*32000=$1.088/hour
- 带宽价格：$0.000685*2000=$1.37/hour
- vcpu 价格：$0.003*8=$0.024/hour（这部分价格为 vm 激活 UltraSSD 功能的收费；计算 vm 的 实际 vcpu 数量，只是在vm 没有附加 UltraSSD 时才收费）
- 总价格：$0.010496+$1.008+$1.37=$2.488496/hour
  改价格为 UltraSSD 的价格，未计算 vm 的计算价格、非 UltraSSD 存储价格、网络价格等。
## 总结
  总体来说 UltraSSD 为 Azure 提供了一个高性能磁盘的选择，并且能满足标称的性能指标。为用户在 MangoDB、MySQL、DW、SAP HANA 等场景的场景提供了很好支持，弥补了 Azure 在存储方面的短板。
  使用 UltraSSD 时需要详细了解客户的 IO 模型，是带宽敏感还是 IOPS 敏感，合理设置性能指标；另外还需注意 vm 的选择，避免成为瓶颈。
  最后，还是希望 UltraSSD 及附加功能尽快在月饼上线，满足国内客户的需求。
