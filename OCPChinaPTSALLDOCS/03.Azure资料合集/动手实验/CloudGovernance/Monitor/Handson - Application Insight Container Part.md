## Application Insights Container Part Hands-on Lab


**第一部分 准备AKS集群，Application Insights**

1.	在Portal中选择创建AKS集群，注意选择的Node节点要稍微选内存和CPU大一点的型号，因为之后用到的Istio会用到比较多的资源。

    ![image](./images/app_insight_container_images/AppInsights%20(1).png)

2.	建立集群的选择用Service Principle作为认证机制，这样对连接之后的ACR也会比较方便

    ![image](./images/app_insight_container_images/AppInsights%20(2).png)

3.	网络的工作模式选在高级的模式，这样可以直接支持CNI。

    ![image](./images/app_insight_container_images/AppInsights%20(3).png)

4.	当AKS集群建立之后，通过Kubectl命令（需要事先在客户端安装好），获得Secret。此处使用Powershell Console

    ``` az aks get-credentials --resource-group <myResourceGroup> --name <myAKSCluster> ```

5.	创建Application Insights，并且记下instruments，之后在配置中会用到。

    ![image](./images/app_insight_container_images/AppInsights%20(4).png)



**第二部分 安装Helm，Istio**
1.	在本地客户端安装Helm，根据不同的的本地操作系统可以选择相应的安装方法

    https://helm.sh/docs/using_helm/#installing-helm

    比如windows可以选择用Choclolate安装

    ```choco install kubernetes-helm --version=2.16.0```

2.	创建Helm使用的Service Account，使用yaml文件进行创建

    [helm-rbac.yaml](./files/appInsights/helm-rbac.yaml)

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

或直接下载：[istio-1.1.3-win.zip](https://github.com/istio/istio/releases/download/1.1.3/istio-1.1.3-win.zip)

5.	安装Istio，此处使用Powershell Console

```
# Copy istioctl.exe to C:\Istio - C盘新建Istio文件夹，把刚才解压出来的istioctl.exe复制过去

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


    ![image](./images/app_insight_container_images/AppInsights%20(4.1).png)




**第三部分 使用Application Insights监控AKS里的服务**

1.	我们先通过Istio的功能把sidecar注入打开，这样新建的pod都会有一个sidecar pod注入进去，用来监控进出的流量，以及把相应的监控数据可以发给Application Insights

    ```kubectl label namespace default istio-injection=enabled```

2.	下载Application Insights adapter，链接地址如下
https://github.com/Microsoft/Application-Insights-Istio-Adapter/releases/

3.	进入这个目录/src/kubernetes/，编辑文件 `application-insights-istio-mixer-adapter-deployment.yaml`， 找到“ISTIO_MIXER_PLUGIN_AI_INSTRUMENTATIONKEY“，并且把这个替换成之前在Application insights里记下的Instrument Key。

4.	在之前的目录下执行命令，让所有的yaml文件部署

    ```kubectl apply -f .```

5.	执行以下命令，查看adapter是否正确运行

    ```kubectl get pods -n istio-system -l "app=application-insights-istio-mixer-adapter"```

    ![image](./images/app_insight_container_images/AppInsights%20(4.2).png)


6.	打开application insights的实时展现数据的页面 `Live Metrics Stream`，观察到已经有一个server链接上了，这个就是我们刚刚部署的adapter

    ![image](./images/app_insight_container_images/AppInsights%20(5).png)

7.	现在我们来部署两个应用，一个叫sleep，一个叫httpbin。先进入之前下载并解压的Istio根目录，执行下面的部署命令。
```
    kubectl apply -f samples/sleep/sleep.yaml
    kubectl apply -f samples/httpbin/httpbin.yaml
```

8.	随后我们要从sleep发送请求到httpbin，为了发送请求我们要储存一个变量，这个命令在Bash里运行。（你可以使用WSL）

    ```export SOURCE_POD=$(kubectl get pod -l app=sleep -o jsonpath={.items..metadata.name})```

9.	从 sleep 向 httpbin 发送一个请求，这个命令在Bash里运行。（你可以使用WSL）

    ```kubectl exec -it $(kubectl get pod -l app=sleep -o jsonpath={.items..metadata.name}) -c sleep -- curl -v httpbin:8000/status/418```

    ![image](./images/app_insight_container_images/AppInsights%20(5.1).png)


10.	我们回到application insights的界面，可以观测到之前发送的这个请求已经被adapter发送到了app insights，并且实施展现在了仪表盘上。

    ![image](./images/app_insight_container_images/AppInsights%20(6).png)

---