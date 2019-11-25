
# Azure 监控平台 Whitepaper & Handson

---
## Application Insights SDK Part Hands-on Lab


**第一部分 准备部署应用**
1.	到github下载本次动手实验需要用到的文件
https://github.com/rkuehfus/AzureMonitoringHackathon 
    ![image](./images/monitor/AppInsightsSDK01.png)


2.	解压后，打开其中的DeployMonHackEnv.ps1，可以使用vscode，也可以使用任何文本工具。随后更新最新的powershell

    ```Install-Module -Name AzureRM -Force -Scope CurrentUser -AllowClobber```

3.	首先在脚本文件中更改5个小写字符的名字
    ```Example: $MonitoringHackName = 'mon17'```

4.	在powershell中登录你的azure订阅
    ```Connect-AzureRmAccount```

    ![image](./images/monitor/AppInsightsSDK02.png)

5.	跑脚本文件中的前面两行，建立keyvault

    ![image](./images/monitor/AppInsightsSDK03.png)

6.	随后会跳出输出用户密码，输入你想用的密钥，并且记住

    ![image](./images/monitor/AppInsightsSDK04.png)

7.	接下来跑脚本中的这条命令，并且复制结果中的高亮部分。
    ![image](./images/monitor/AppInsightsSDK05.png)

8.	把高亮复制的内容，黏贴到azuredeploy.parameters.json文件中，并且注意更新对应的prefix

    ![image](./images/monitor/AppInsightsSDK06.png)
    ![image](./images/monitor/AppInsightsSDK07.png)

9.	跑脚本中最后的一条命令，估计要等半小时左右，所有的资源会部署完毕。

    ![image](./images/monitor/AppInsightsSDK08.png)





**第二部分** 在App Insights中观测应用的数据


1.	在Portal中新建一个App Insights的Workspace

    ![image](./images/monitor/AppInsightsSDK09.png)

2.	进入之前部署的跳板机

    ![image](./images/monitor/AppInsightsSDK10.png)

3.	在Visual Studio里打开相对应的project

    ![image](./images/monitor/AppInsightsSDK11.png)

    ![image](./images/monitor/AppInsightsSDK12.png)

    ![image](./images/monitor/AppInsightsSDK13.png)


    接下来就能看到打开的eshop网站了。
    
    ![image](./images/monitor/AppInsightsSDK14.png)


4.	接下来让我们来安装一下application insights的SDK。在右侧“Web”那里点击邮件，然后点击安装sdk。

    ![image](./images/monitor/AppInsightsSDK15.png)

    ![image](./images/monitor/AppInsightsSDK16.png)


5.	注意选择相对应的subscription等信息

    ![image](./images/monitor/AppInsightsSDK17.png)

    ![image](./images/monitor/AppInsightsSDK18.png)


6.	测试一下安装了SDK的程序是否正常运行，同时观测一下app insights的telemetry有没有正常运作。可以尝试做一些商品浏览，登录，添加商品到购物车等操作，然后观测app insights里面的信息。

    ![image](./images/monitor/AppInsightsSDK19.png)

    ![image](./images/monitor/AppInsightsSDK20.png)


7.	好了，现在来更新一下applicaton insights的Nuget Packege。装完之后再运行一遍程序，保证一切都没有问题。

    ![image](./images/monitor/AppInsightsSDK21.png)

    ![image](./images/monitor/AppInsightsSDK22.png)

    ![image](./images/monitor/AppInsightsSDK23.png)


8.	把加入SDK的程序重新发布一下，我们吧这个程序发布到后端的VMSS里面，分别在1号机器，和2号机器做相同的操作。

    ![image](./images/monitor/AppInsightsSDK24.png)

    ![image](./images/monitor/AppInsightsSDK25.png)


    先选择第一台vmss的主机
    
    ![image](./images/monitor/AppInsightsSDK26.png)

    ![image](./images/monitor/AppInsightsSDK27.png)

    ![image](./images/monitor/AppInsightsSDK28.png)

    ![image](./images/monitor/AppInsightsSDK29.png)
    
    ![image](./images/monitor/AppInsightsSDK30.png)

    把vmss里面第二台机器也部署一下

    ![image](./images/monitor/AppInsightsSDK31.png)


9.	现在我们在portal里试一下ping的test，查看事件有没有被捕捉到。
    
    ![image](./images/monitor/AppInsightsSDK32.png)

    ![image](./images/monitor/AppInsightsSDK33.png)

    ![image](./images/monitor/AppInsightsSDK34.png)


10.	通过手工的脚本，在你的笔记本或者jump server上运行一下，把脚本中的url替换成你部署的eshop当中的url。在尝试看一下app insights的数据收集。
    ```
    for ($i = 0 ; $i -lt 100; $i++)
    {
    Invoke-WebRequest -uri http:// mon19webscalesetlb.eastus.cloudapp.azure.com/
    }
    ```

    ![image](./images/monitor/AppInsightsSDK35.png)

    
    Sclaeout 的规则

    ![image](./images/monitor/AppInsightsSDK36.png)


    Scalein的规则

    ![image](./images/monitor/AppInsightsSDK37.png)

    ![image](./images/monitor/AppInsightsSDK38.png)

11.	过5分钟之后，应该可以看到性能数据了，并且可以看到vmss按照规则开始自动扩展。


    ![image](./images/monitor/AppInsightsSDK39.png)

    ![image](./images/monitor/AppInsightsSDK40.png)


12.	尝试触发一个登录错误。打开网站的主页

    ![image](./images/monitor/AppInsightsSDK41.png)

    ![image](./images/monitor/AppInsightsSDK42.png)

    尝试更新一下密码

    ![image](./images/monitor/AppInsightsSDK43.png)

    ![image](./images/monitor/AppInsightsSDK44.png)

    从app insights里找到这个错误

    ![image](./images/monitor/AppInsightsSDK45.png)

    ![image](./images/monitor/AppInsightsSDK46.png)







## Application Insights Container Part Hands-on Lab



**第一部分 准备AKS集群，Application Insights**

1.	在Portal中选择创建AKS集群，注意选择的Node节点要稍微选内存和CPU大一点的型号，因为之后用到的Istio会用到比较多的资源。

    ![image](./images/monitor/AppInsights%20(1).png)

2.	建立集群的选择用Service Principle作为认证机制，这样对连接之后的ACR也会比较方便

    ![image](./images/monitor/AppInsights%20(2).png)

3.	网络的工作模式选在高级的模式，这样可以直接支持CNI。

    ![image](./images/monitor/AppInsights%20(3).png)

4.	当AKS集群建立之后，通过Kubectl命令（需要事先在客户端安装好），获得Secret。此处使用Powershell Console

    ``` az aks get-credentials --resource-group <myResourceGroup> --name <myAKSCluster> ```

5.	创建Application Insights，并且记下instruments，之后在配置中会用到。

    ![image](./images/monitor/AppInsights%20(4).png)



**第二部分 安装Helm，Istio**
1.	在本地客户端安装Helm，根据不同的的本地操作系统可以选择相应的安装方法

    https://helm.sh/docs/using_helm/#installing-helm

    比如windows可以选择用Choclolate安装

    ```choco install kubernetes-helm```

2.	创建Helm使用的Service Account，使用yaml文件进行创建

    [helm-rbac.yaml](./files/monitor/AppInsights/helm-rbac.yaml)

    ```kubectl apply -f helm-rbac.yaml```

3.	初始化AKS服务器端的Helm Tiller进程，此处使用Powershell Console

    ```helm init --service-account tiller```

4.	下载Istio，此处使用Powershell Console
```
# Specify the Istio version that will be leveraged throughout these instructions
$ISTIO_VERSION="1.1.3"

# Windows
# Use TLS 1.2
[Net.ServicePointManager]::SecurityProtocol = "tls12"
$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -URI "https://github.com/istio/istio/releases/download/$ISTIO_VERSION/istio-$ISTIO_VERSION-win.zip" -OutFile "istio-$ISTIO_VERSION.zip"
Expand-Archive -Path "istio-$ISTIO_VERSION.zip" -DestinationPath .
```

5.	安装Istio，此处使用Powershell Console

```
# Copy istioctl.exe to C:\Istio
cd istio-$ISTIO_VERSION
New-Item -ItemType Directory -Force -Path "C:\Istio"
Copy-Item -Path .\bin\istioctl.exe -Destination "C:\Istio\"

# Add C:\Istio to PATH. 
# Make the new PATH permanently available for the current User, and also immediately available in the current shell.
$PATH = [environment]::GetEnvironmentVariable("PATH", "User") + "; C:\Istio\"
[environment]::SetEnvironmentVariable("PATH", $PATH, "User") 
[environment]::SetEnvironmentVariable("PATH", $PATH)
```

6.	Istio通过CRD来管理它的配置信息，下面通过helm来安装CRD，注意的是要在之前下载并解压的Itsio的根目录下运行命令。此处使用Powershell Console

    ```helm install install/kubernetes/helm/istio-init --name istio-init --namespace istio-system```

7.	安装Istio，此处使用Powershell Console
```
helm install install/kubernetes/helm/istio --name istio --namespace istio-system `
  --set global.controlPlaneSecurityEnabled=true `
  --set mixer.adapters.useAdapterCRDs=false `
  --set tracing.enabled=true 
```

8.	通过下面的命令查看Istio相关的Pods是不是都正常启动了。

    ```kubectl get pods --namespace istio-system```



**第三部分 使用Application Insights监控AKS里的服务**

1.	我们先通过Istio的功能把sidecar注入打开，这样新建的pod都会有一个sidecar pod注入进去，用来监控进出的流量，以及把相应的监控数据可以发给Application Insights

    ```kubectl label namespace default istio-injection=enabled```

2.	下载Application Insights adapter，链接地址如下
https://github.com/Microsoft/Application-Insights-Istio-Adapter/releases/

3.	进入这个目录/src/kubernetes/  ， 找到“ISTIO_MIXER_PLUGIN_AI_INSTRUMENTATIONKEY“，并且把这个替换成之前在Application insights里记下的Instrument Key。

4.	在之前的目录下执行命令，让所有的yaml文件部署

    ```kubectl apply -f .```

5.	执行以下命令，查看adapter是否正确运行

    ```kubectl get pods -n istio-system -l "app=application-insights-istio-mixer-adapter"```

6.	打开application insights的实时展现数据的页面，观察到已经有一个server链接上了，这个就是我们刚刚部署的adapter

    ![image](./images/monitor/AppInsights%20(5).png)

7.	现在我们来部署两个应用，一个叫sleep，一个叫httpbin。先进入之前下载并解压的Istio根目录，执行下面的部署命令。
```
    kubectl apply -f samples/sleep/sleep.yaml
    kubectl apply -f samples/httpbin/httpbin.yaml
```

8.	随后我们要从sleep发送请求到httpbin，为了发送请求我们要储存一个变量，这个命令在Bash里运行。（你可以使用WSL）

    ```export SOURCE_POD=$(kubectl get pod -l app=sleep -o jsonpath={.items..metadata.name})```

9.	从 sleep 向 httpbin 发送一个请求，这个命令在Bash里运行。（你可以使用WSL）

    ```kubectl exec -it $(kubectl get pod -l app=sleep -o jsonpath={.items..metadata.name}) -c sleep -- curl -v httpbin:8000/status/418```

10.	我们回到application insights的界面，可以观测到之前发送的这个请求已经被adapter发送到了app insights，并且实施展现在了仪表盘上。

    ![image](./images/monitor/AppInsights%20(6).png)

---








s