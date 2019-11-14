官网有很多文档介绍如何创建自定义镜像，之前support一个客户，已经使用Azure两年多，很多机器都是非托管磁盘，所以帮客户去测试使用通过非托管自定义镜像创建VM，整个脚本很简单，只需要改掉一个参数就可以实现，但是因为没有直接文档说明，当时花了时间去测试，所以直接把成功脚本分享给大家使用，批量创建自定义非托管磁盘VM也只是需要修改imageurl即可，托管磁盘创建晚点分享给大家。

脚本如下：

```
$rgName = "myResourceGroup"

$subnetName = "mySubNet"

$singleSubnet = New-AzureRmVirtualNetworkSubnetConfig -Name $subnetName -AddressPrefix 10.0.0.0/24

$location = "China North"

$vnetName = "myVnetName"

$vnet = New-AzureRmVirtualNetwork -Name $vnetName -ResourceGroupName $rgName -Location $location `

    -AddressPrefix 10.0.0.0/16 -Subnet $singleSubnet

    $ipName = "myIP"

$pip = New-AzureRmPublicIpAddress -Name $ipName -ResourceGroupName $rgName -Location $location `

    -AllocationMethod Dynamic

    $nicName = "myNicName"

$nic = New-AzureRmNetworkInterface -Name $nicName -ResourceGroupName $rgName `

-Location $location -SubnetId $vnet.Subnets[0].Id -PublicIpAddressId $pip.Id

$nsgName = "myNsg"

 

$rdpRule = New-AzureRmNetworkSecurityRuleConfig -Name myRdpRule -Description "Allow RDP" `

    -Access Allow -Protocol Tcp -Direction Inbound -Priority 110 `

    -SourceAddressPrefix Internet -SourcePortRange * `

    -DestinationAddressPrefix * -DestinationPortRange 3389

$nsg = New-AzureRmNetworkSecurityGroup -ResourceGroupName $rgName -Location $location `

    -Name $nsgName -SecurityRules $rdpRule

    $vmName = "myVM"

$vmConfig = New-AzureRmVMConfig -VMName $vmName -VMSize "Standard_A2"

$vm = Add-AzureRmVMNetworkInterface -VM $vmConfig -Id $nic.Id

$osDiskUri = "https://xxxxxxxxxxxx.vhd" ，改成自己的vhd url

$osDiskName = $vmName + "osDisk"

$vm = Set-AzureRmVMOSDisk -VM $vm -Name $osDiskName -VhdUri $osDiskUri -CreateOption attach -Linux
```

 

通过Powershell，就可以创建出来，最后三行是重点，尤其是attach -Linux，如果是windows，就是attach -Windows。
