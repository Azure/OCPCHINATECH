客户使用Function过程中，想获取IP格式的JSON输出，在不同Runtime版本，获取到的内容不同，这一块最后发现是需要调整一下代码就可以得到符合要求的JSON格式log输出。

1. Runtime version: 1.0.12154.0 ，同样的代码可以获取到IP，可以输出Log，但不能得到JSON格式的输出。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20Function%20Runtime%E7%89%88%E6%9C%AC%E5%92%8CIP%E8%BE%93%E5%87%BA%E6%A0%BC%E5%BC%8F%E9%97%AE%E9%A2%9801.png)

2. Runtime version: 2.0.12180.0，可以获取到IP，只是不能输出Log，但可以得到JSON格式的输出
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Azure%20Function%20Runtime%E7%89%88%E6%9C%AC%E5%92%8CIP%E8%BE%93%E5%87%BA%E6%A0%BC%E5%BC%8F%E9%97%AE%E9%A2%9802.png)

3. 关于此问题，定位到最后跟客户的代码使用方式有一定关系，一定要使用异步的方法，就可以使用Runtime 2.0版本得到IP log JSON格式输出
```
computeClient.virtualMachines.listAll(function (err, result) {

                    if (err) {

                        context.log(util.format('List all vms under the current subscription. \n%s', util.inspect(err, { depth: null })));

                        var listVmErrorInfo = [];

                        listVmErrorInfo.push({

                            'status_code': '1',

                            'status_info': 'Failed to list VMs.',

                            'error_info': err

                        });

                        var listVmErrorInfoJson = JSON.stringify(listVmErrorInfo);

                        var vmInfo = listVmErrorInfoJson.substring(1, listVmErrorInfoJson.length-1);

                        // Added Section B

                        context.res = {

                            body : JSON.parse(vmInfo)

                        };

                        context.done();

                        //

                    }

                    else {

                        context.log(util.format('List all vms for the current subscription. \n%s', util.inspect(result, { depth: null })));

                        var virtualMachinesJson = JSON.stringify(result);

                        var virtualMachines = JSON.parse(virtualMachinesJson);

                        var vms = [];

                        var count = '';

                        count = virtualMachines.length;

 

                        for (var i=0; i<virtualMachines.length; i++) {

                            virtualMachineName = virtualMachines[i].name;

                            VirtualMachineId = virtualMachines[i].id.split('/');

                            resourceGroupName = VirtualMachineId[4];

 

                            networkClient.publicIPAddresses.list(resourceGroupName, function (err, result){

                                context.log('-------------Get IP Addresses---------------');

                                if (err) {

                                    context.log(util.format('\nGets all public IP addresses in a resource group.:\n%s', util.inspect(err, { depth: null })));

                                } else {

                                    var publicIpAddressJson = JSON.stringify(result);

                                    var publicIpAddressString = JSON.parse(publicIpAddressJson);

                                    for (var i=0; i<publicIpAddressString.length; i++) {

                                        publicIpAddress = publicIpAddressString[i].ipAddress;

                                        context.log('=================Public IP address:'+publicIpAddress);

                                    }

                                    //context.log('=================Public IP address:'+publicIpAddress);

                                }

                                // Added Section A

                                vms.push({

                                    'count': count,

                                    'status_code': '0',

                                    'status_info': 'Get VMs information successfully',

                                    'virtualMachineInfo': virtualMachines,

                                    'ipAddress_Test': publicIpAddress

                                });

                                var vmsJson = JSON.stringify(vms);

                                vmInfo = vmsJson.substring(1, vmsJson.length-1);

                                //

                                // Added Section B

                                context.res = {

                                    body : JSON.parse(vmInfo)

                                };

                                context.done();

                                //

                            })

                        }

                        // Removed Section A

                    }

                    // Removed Section B

                });
```

4. 推荐用v2版本async/await 代替 callback patterns，V2 支持 async/await (with node v8 or v10), V1版本不支持。
 

 

 

**basic sample translation:**
```
module.exports = async function (context, req) {

    if (1) {

        // Declares variables

 

        //login in azure using the service principal

        try {

            const authResponse = await msRestAzure.loginWithServicePrincipalSecret(clientId, secret, domain)

            let credentials = authResponse.credentials;

            let subscriptions = authResponse.subscriptions;

            // success code with other

           

            // This is the same as context.done()... see docs for details: https://docs.microsoft.com/azure/azure-functions/functions-reference-node

            return;

        } catch (err) {

            // the "if err" code

            var loginErrorInfo = [];

            // ...

            // etc.

 

            // this is the same as context.done(err);

            throw err;

        }

    }

}
```

 

5. 最后大家遇到类似问题，可以直接建议客户使用如上方式解决。
