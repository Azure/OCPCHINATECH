当然目前我们还有一些客户使用ASM模式，也需要获得信息，可以参考如下脚本，ARM可以参考link：https://www.cnblogs.com/wangsongshare/p/9835841.html ，

如下介绍通过直接运行PowerShell脚本就可以很快获取到全部信息

1. 脚本如下：

可以通过powershell收集统计VM的公网IP，内网IP，机器型号，位置，操作系统

```
$info=[System.Collections.ArrayList]@()

$svcs=(Get-AzureService).ServiceName

foreach($svcName in $svcs){

    Get-AzureDeployment -ServiceName $svcName >>null -ErrorAction Ignore

    if( $?)

    {

        $vms=Get-AzureVM -ServiceName $svcName

    $svc=Get-AzureService -ServiceName $svcName

    $dep=Get-AzureDeployment -ServiceName $svcName

    foreach( $vm in $vms)

    {

        $d=@{}

        $d.Add("VMname",$vm.Name)

        $d.Add("ServiceName",$svcName)

        $d.Add("VMSize",$vm.InstanceSize)

        $d.Add("OStype",$vm.VM.OSVirtualHardDisk.OS )

        $d.Add("PrivateIP",$vm.IpAddress)

       

        if(Get-AzureStaticVNetIP  -VM $vm){

                    $d.Add("PrivateIPreserved","Yes")

                }

        else{

                    $d.Add("PrivateIPreserved","No")

        }

                $d.Add("PublicIP",$dep.VirtualIPs[0].Address)

        if ($dep.ReservedIPName ){

                    $d.Add("PublicIPreserved","Yes")

        }

        else

        {

            $d.Add("PublicIPreserved","No")

        }

             $d.Add("Location",$svc.Location )

        $info.Add($d)

          }

        }

}

 

$info | select @{Name="Vmname";Expression={$_["Vmname"]}},@{Name="Vmsize";Expression={$_["Vmsize"]}},@{Name="OStype";Expression={$_["OStype"]}},@{Name="ServiceName";Expression={$_["ServiceName"]}},@{Name="PrivateIP";Expression={$_["PrivateIP"]}},@{Name="PrivateIPreserved";Expression={$_["PrivateIPreserved"]}},@{Name="PublicIP";Expression={$_["PublicIP"]}},@{Name="PublicIPreserved";Expression={$_["PublicIPreserved"]}},@{Name="Location";Expression={$_["Location"]}} |Out-GridView
```

2. 跑完脚本之后，可以获取到如下信息：
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20ASM%E6%A8%A1%E5%BC%8F%E4%B8%8B%E8%8E%B7%E5%8F%96VM%E4%BF%A1%E6%81%AF%EF%BC%88%E4%BA%8C%EF%BC%8901.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20ASM%E6%A8%A1%E5%BC%8F%E4%B8%8B%E8%8E%B7%E5%8F%96VM%E4%BF%A1%E6%81%AF%EF%BC%88%E4%BA%8C%EF%BC%8902.png)

3. 如上图可以非常清晰的看到所有VM的信息，这对于IT运维会很方便，尤其是大客户几百台机器需要统计，这可以节省大量时间。当然也可以直接导出到csv文件，添加端口等信息，这个供大家参考。固定IP可以参考：https://www.cnblogs.com/wangsongshare/p/8329051.html
