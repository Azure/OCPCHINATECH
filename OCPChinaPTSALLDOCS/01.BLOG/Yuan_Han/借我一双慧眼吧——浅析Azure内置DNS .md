 Azure已经发布了DNS服务，Azure上的客户可以直接使用该服务创建DNS解析而无需自己安装配置管理DNS服务器，大大方便了使用。即使客户不使用DNS服务，Azure其实也内置了一套为VM服务的DNS。下边就看看内置DNS的使用规则。
## DNS解析规则
  再同一个资源组、同一个vnet里创建两台VM，虚机名（代指在Azure创建VM给虚机的命名，下同）分别为vm01和vm02。登录后可以看到，默认将虚机名作为了主机名（代指在Guest OS的机器名，下同）：
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%201.png)

 从vm01直接用ping到vm02：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%202.png)

  可以正确的解析vm02。
  现在需要确认解析是基于虚机名还是主机名？通过hostname命令将vm02的主机名改为host02：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%203.png)

  再次从vm01分别ping虚机名和主机名：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%204.png)

  虚机名（vm02）已经找不到，解析已经变成了主机名（host02）。
  通过nslookup查找也是同样结果：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%205.png)

  这个简单测试可以确认，在Azure默认的VM DNS解析中，是对主机名进行解析。
## 主机名修改对DNS的影响
  众所周知，hostname虽然可以修改主机名，但是并不会发起DNS注册。DNS服务器如何知道VM修改了主机名？在Azure VM里，有一个插件waagent对VM进行配置管理，检查waagent的配置文件（/etc/waagent.conf），可以看到如下参数：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%206.png)

  从参数名就能看出，这个参数是对hostname进行监控，如果发现hostname变化就会通告。
  再做一个小测试，将该参数修改为n，然后重启waagent服务，再将虚机vm02的主机名从host02修改为vm02，看看DNS解析是否自动修改：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%207.png)

  如我们所料，将该参数修改为n后，DSN解析仍为host02，修改主机名不会再影响到DNS解析。
  所以如果客户的环境希望能保持DNS解析不受修改主机名的影响，可以通过修改waagent的参数来实现。
## 虚机状态对DNS的影响
  VM的各种状态（OS层面关机、解除分配、删除）会对DNS解析有何影响？下边逐一测试。
  vm02在正常开机情况下，从vm01可以解析到vm02的主机名：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%208.png)

  从OS层将vm02关机，vm02状态是已停止，从vm01检查vm02的解析，正常：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%209.png)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2010.png)


  在Azure层面关机，vm02状态是已取消分配，从vm01检查vm02的解析，无法解析，vm02的解析自动从DNS注销：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2011.png)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2012.png)

  现在将vm02正常开机后直接删除，vm02的解析也被注销了：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2013.png)

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2014.png)

  综上所述，Azure VM的DNS生命周期是在分配资源的状态，与VM自身的开关机无关。当VM的资源被释放（deallocate、删除等）时，VM的DNS解析被注销。
## 主机名冲突
  如果同一个环境里，两台VM被修改为同一个主机名，解析会怎样？
  还是新建两台VM，然后主机名分别修改为host01和host02，可以正常解析到对应主机的ip：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2015.png)

  现在将vm02的主机名从host02修改为host01，再检查解析：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2016.png)

  host02的解析找不到，而host01的解析从之前的vm01的ip（172.19.18.4）变为了host02的ip（172.19.18.6）。
  从以上实验可以看出，多台VM的主机名出现冲突时，按照后来者优先的原则，DNS解析到最后一台同名的VM。
  这个设计思路是非常合理的，考虑一个场景，当一台业务主机出现故障时，启动一台备机来顶替；这时候需要将所有业务指向备机，这时候只需要将备机的主机名设置为故障机的主机名，DNS就会解析到备机的ip，备机直接“抢到”所有的流量，而无需再做其他配置。
  现在去将vm02解除分配，解析是否会“飘回”vm01？测试一下。
  从Azure界面管掉vm02（取消分配）：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2017.png)

  再去vm01上检查host01：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2018.png)

  所以当正常解析的VM由于各种原因从DNS注销后，DNS并不会自动解析到同主机名的VM。
  这种设计是为了避免出现不可知故障。例如，当环境里有多台同主机名的VM，正常解析并使用的VM下线后，自动解析到剩下的哪台主机？要是解析到了错误的主机，就会影响业务，所以这时候需要人工介入处理。
  处理方法很简单，既然修改主机名就可以导致DNS重新注册，那么我们将需要解析的主机随便修改一下主机名（主要不要导致冲突），再改回正确的主机名即可：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2019.png)

## 进一步的研究
### waagent的影响
  前边说了，VM的waagent配置里有对hostname的监控，VM取消分配并重新分配（以下简重置VM）后将重新注册DNS。进一步看看，如果在waagent配置里禁用对hostname改变的监控，然后修改主机名后重置VM，DNS解析是否会更改。
  修改waagent配置文件，重启waagent服务，重命名主机名：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2020.png)

  主机名从host01修改为host001.
  重置VM后检查解析：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2021.png)

  虽然重置了VM，但是解析仍然是host01，而非修改后的主机名host001.
  为什么会出现这个情况？检查一下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2022.png)

  重置VM后，修改主机名失效，变回了修改前的主机名host01。
  在Linux里，hostname命令只是临时修改主机名，OS重启后就会失效，真正的主机名时保存在/etc/hostname文件里的。做个测试如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2023.png)

  如图所示，用hostname修改主机名后，/etc/hostname文件的内容并没有变化，所以重启就失效了。
  之前的修改为什么可以持久化？原因还是在waagent配置里，当监控hostname的参数设置为y时，用hostname修改主机名，将会把新主机名写入/etc/hostname文件，测试如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2024.png)

  修改成功。
### 网络的影响
  如果我们检查VM完整主机名，得到信息如下：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2025.png)

  主机名后加上了一串后缀。
  但是我们不用加后缀也可以ping通另一台VM：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2026.png)

  检查另一VM的完整主机名：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2027.png)

  可以发现两VM的后缀一样。这是因为在同一个vnet里，DNS解析默认的后缀一致。
  根据Azure的设计，vnet之间是不通的，如果要跨vnet通讯，需要做vnet peer互通。
  现在创建一个新的VM，命名为vm03，在HyDNSDemoRG-vnet02的vnet：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2028.png)

  而原有的vm01（主机名为host01）在HyDNSDemoRG-vnet的vnet：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2029.png)

  显然vm01找不到vm03：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2030.png)

  现在通过peer将两个vnet打通，通过vm01去ping vm03的ip，可以通讯：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2031.png)

  但是用主机名仍然找不到：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2032.png)

  检查vm03的完整主机名：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2033.png)

  其主机名的后缀与vm01不一样，所以vm01通过不带域名的主机名找不到vm03。
  现在通过完整的主机名来查找vm03：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2034.png)

  依然找不到。
  由此可以看出，Azure默认的DNS只对vnet内部生效，不能跨vnet。如果需要跨vnet使用DNS解析VM，就要通过配置Azure 私有DNS服务，并附加到多个vnet来实现：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/借我一双慧眼吧——浅析Azure内置DNS%2035.png)

## 总结
  虽然Azure Private DNS在Azure China还未提供，但是Azure已经内置了一套对VM的DNS解析规则。充分了解其工作方式，可以大大简化对VM的网络管理。
  在实际运维中也需注意，规则的灵活性可能会导致事故，所以一定要有完善的文档管理、变更机制以保证生产的正常。
