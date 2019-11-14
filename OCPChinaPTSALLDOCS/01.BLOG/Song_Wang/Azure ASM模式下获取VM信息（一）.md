马上就要双十一了，对于一些大客户而言，使用的VM机器超过几百台，无论是促销活动还是每个季度的机器梳理，都需要对这些VM进行梳理总结，是否有公网IP，IP动态静态，对于动态IP而言，因为机器重启有可能造成IP改变，有可能对业务造成很大影响。所以快速获取订阅下所有VM信息就很重要。

如下介绍通过直接运行PowerShell脚本就可以很快获取到全部信息

1. 脚本如下：

可以通过powershell收集统计VM的公网IP，内网IP，机器型号，位置，操作系统

```
#

Login-AzureRmAccount -EnvironmentName Azurechinacloud

Select-AzureRmSubscription  -SubscriptionName xxxxxxx（需要添加自己的订阅ID）

$AllNic=[System.Collections.ArrayList]@()

$AllRG=(Get-AzureRmResourceGroup).ResourceGroupName

foreach($RG in $AllRG ){

    $Nics=Get-AzureRmNetworkInterface -ResourceGroupName $RG

    foreach($nic in $Nics){

     $d=@{}

          if( $nic.VirtualMachine )

     {

        $d.Add("Vmname",$nic.VirtualMachine[0].Id.Split("/")[8])

        $vm=Get-AzureRmVM -ResourceGroupName $nic.VirtualMachine[0].Id.Split("/")[4] -Name $nic.VirtualMachine[0].Id.Split("/")[8]

        $d.Add("Vmsize",$vm.HardwareProfile.VmSize)

        if( $vm.OSProfile.WindowsConfiguration ){

            $d.Add("OStype","Windows")

                }

     else

        {

            $d.Add("OStype","Linux")

        }

     

     $d.Add("NicName",$nic.Name)

     $d.Add("PrivateIP",$nic.IpConfigurations[0].PrivateIpAddress)

     $d.Add("PrivateIPAllocationMethod",$nic.IpConfigurations[0].PrivateIpAllocationMethod)

 

     #获取公网IP配置

     if( $nic.IpConfigurations[0].PublicIpAddress )

     {

                $pubip=Get-AzureRmPublicIpAddress -Name $nic.IpConfigurations[0].PublicIpAddress.id.Split("/")[8] -ResourceGroupName $nic.IpConfigurations[0].PublicIpAddress.id.Split("/")[4]

 

        $d.Add("PublicIP",$pubip.IpAddress)

        $d.Add("PublicIpAllocationMethod",$pubip.PublicIpAllocationMethod)

    }

    else

    {

            $d.Add("PublicIP","Null")

        $d.Add("PublicIpAllocationMethod","Null")

   

    }

 

     $d.Add("Location",$nic.Location )

     $AllNic.Add($d)

     }

      

  }

}

$AllNic | select @{Name="Vmname";Expression={$_["Vmname"]}},@{Name="Vmsize";Expression={$_["Vmsize"]}},@{Name="OStype";Expression={$_["OStype"]}},@{Name="NicName";Expression={$_["NicName"]}},@{Name="PrivateIP";Expression={$_["PrivateIP"]}},@{Name="PrivateIpAllocationMethod";Expression={$_["PrivateIpAllocationMethod"]}},@{Name="PublicIP";Expression={$_["PublicIP"]}},@{Name="PublicIpAllocationMethod";Expression={$_["PublicIpAllocationMethod"]}},@{Name="Location";Expression={$_["Location"]}} | Out-GridView
```

2. 跑完脚本之后，可以获取到如下信息：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20ASM%E6%A8%A1%E5%BC%8F%E4%B8%8B%E8%8E%B7%E5%8F%96VM%E4%BF%A1%E6%81%AF%EF%BC%88%E4%B8%80%EF%BC%8901.png)

3. 如上图可以非常清晰的看到所有VM的信息，这对于IT运维会很方便，尤其是大客户几百台机器需要统计，这可以节省大量时间。当然也可以直接导出到csv文件，添加端口等信息，这个供大家参考。如何固定IP可以参考：https://www.cnblogs.com/wangsongshare/p/8329051.html
