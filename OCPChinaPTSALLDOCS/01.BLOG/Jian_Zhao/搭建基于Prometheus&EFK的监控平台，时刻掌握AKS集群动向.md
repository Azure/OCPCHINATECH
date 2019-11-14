(估计是今年最后一篇文章了)  愣是拖成了新年的第一篇文章，这篇文章主要是动手，Step by Step的构建AKS的开源监控系统，所有跟工具相关的详细介绍请移步参考资料。
目前，中国Azure中提供的AKS服务正在预览阶段，今天将介绍如何通过Prometheus+Grafana来构建监控系统，通过Elastic Search + Fluent + Kibana来构建日志分析系统，来实时监控你的AKS集群。以下所有服务均跑在容器中，即运行于AKS集群内。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9101.webp)

# Step 1 通过 Azure CLI 创建 AKS 集群
```
# 配置 Azure CLI，以使用中国Azure
az cloud set -n AzureChinaCloud
az login

# 创建 Resource Group，名为 zjaks04
az group create -n zjaks04 -l chinaeast2

# 创建 AKS 集群
az aks get-versions -l chinaeast2 -o table
az aks create -g zjaks04 -n aks04 --node-count 2 --node-vm-size Standard_A3 --disable-rbac --generate-ssh-keys --kubernetes-version 1.11.5 --no-wait

# 连接 AKS 集群
az aks install-cli
az aks get-credentials -n aks04 -g zjaks04
kubectl get nodes
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9102.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9103.webp)

在实际应用AKS过程中，使用相应的容器镜像，可能会遇到gcr.io地址无法访问的情况，不要担心，中国Azure已经做好了相应的Mirror地址，详情可参见参考资料。

# Step 2 安装并配置 Helm
Helm是针对Kubernetes上运行的应用，进行包管理的工具，可以将应用部署过程中需要的多种资源，包括Deployment，Service，Role等，通过Chart进行打包并管理，可以通过Helm对程序进行方便的安装。

```
# 安装 Helm
VER=v2.11.0
wget https://mirror.azure.cn/kubernetes/helm/helm-$VER-linux-amd64.tar.gz
tar -zxvf helm-v2.11.0-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin
sudo helm init --tiller-image gcr.azk8s.cn/kubernetes-helm/tiller:$VER --stable-repo-url https://mirror.azure.cn/kubernetes/charts/
```
由于Helm repo也存在连接访问不可达的情况，所以我们也可以借用Azure 已经创建好的Mirror，进行连接。

安装完成后，可以查看可用的repo ：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9104.webp)

试验一下 Helm 是否可用 ：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9105.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9106.webp)

# Step 3 安装并配置监控系统
以 Prometheus 为中心的监控告警系统的架构图如图所示：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9107.webp)

Prometheus相比于常用的agent based监控工具，如Zabbix，在数据收集方法上有如下比较：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9108.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9109.webp)

后续如果需要通过Prometheus打造整个系统的监控，包括云上的虚机，PaaS服务等，可通过Azure Monitor对应的exporter，将数据接口暴露给Prometheus，实现Metrics数据的汇总。Azure Monitor对应的exporter，可参见 https://github.com/RobustPerception/azure_metrics_exporter

Prometheus 可以单独装在虚拟机中，也可以容器化的方式装在目前的AKS集群中，本次实验将以容器化的方式进行安装。

创建 Namespace，为本次实验做准备。
```
kubectl create namespace monitoring
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9110.webp)

创建 ConfigMap，此ConfigMap将作为Prometheus Server的配置文件，用来记录需要监控的资源 metric endpoint 信息及配置。
ConfigMap 文件内容请参见 https://zjblog.blob.core.chinacloudapi.cn/1226blogfiles/prometheus.yml
```
kubectl create configmap prometheus-config --from-file ./demo/prometheus.yml -n monitoring
```
创建 Prometheus Deployment，具体文件内容请参见 https://zjblog.blob.core.chinacloudapi.cn/1226blogfiles/prometheus-deploy.yml
```
kubectl create -f ./demo/prometheus-deploy.yml
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9111.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9112.webp)

接下来，我们将为Prometheus配置两个 metric endpoints, 即 kube-state-metrics，node-exporter, 来收AKS集群中资源使用情况的信息，实际应用中，我们可以通过更多的metric endpoints 收集不同层面的Metrics信息。

```
# 通过 Helm，安装 Node exporter
helm install --name node-exporter stable/prometheus-node-exporter --namespace monitoring
```
当我们创建 AKS 时，如果指定参数 --disable-rbac，执行上述命令可能会收到如下错误：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9113.webp)

这是由于目前系统里暂无RBAC的Role及RoleBinding，但Helm在创建资源需要，一种解决办法是手工创建需要的Role及RoleBinding，具体文件内容请参见：https://zjblog.blob.core.chinacloudapi.cn/1226blogfiles/rbac.yml
```
kubectl create -f ./demo/rbac.yml
```
继续 Helm 安装 Node exporter 操作

```
# 清除刚创建的node-exporter
helm del --purge node-exporter

# 通过新创建的 Service Account tiller，重新初始化Helm
helm init --tiller-image gcr.azk8s.cn/kubernetes-helm/tiller:v2.11.0 --stable-repo-url https://mirror.azure.cn/kubernetes/charts/ --service-account tiller --upgrade

# 重新创建 node-exporter
helm install --name node-exporter stable/prometheus-node-exporter --namespace monitoring
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9114.webp)

```
# 安装 kube-state-metrics
git clone https://github.com/kubernetes/kube-state-metrics.git

# 由于 k8s.gcr.io & quay.io 没有办法直接访问，需要替换成 mirror的镜像地址 `gcr.azk8s.cn/google_containers/` & `quay.azk8s.cn`，需要通过修改文件 ./kube-state-metrics/kubernetes/kube-state-metrics-deployment.yaml

kubectl apply -f kube-state-metrics/kubernetes/
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9115.webp)

接下来，我们将更新Prometheus的配置 prometheus.yml，将添加的metric endpoints 添加到配置中，更改后的文件内容请参照 https://zjblog.blob.core.chinacloudapi.cn/1226blogfiles/prometheus_final.yml

```
# 更新 ConfigMap
kubectl create configmap prometheus-config --from-file=./demo/prometheus.yml -o yaml --dry-run -n monitoring | kubectl apply -f -

# 将更新的ConfigMap patch到 Prometheus deployment
kubectl patch deployment prometheus-deployment -p '{"spec":{"template":{"metadata":{"labels":{"date":"1226-03"}}}}}' -n monitoring
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9116.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9117.webp)

现在，我们已经通过Prometheus获取了集群中的监控信息，接下来需要通过Grafana进行图形化的展现。

```
# 通过 Helm 安装 Grafana
helm install --name grafana stable/grafana --set service.type=LoadBalancer --set sidecar.datasources.enabled=true --set sidecar.dashboards.enabled=true --set sidecar.datasources.label=grafana_datasource --set sidecar.dashboards.label=grafana_dashboard --namespace monitoring

# 获取 Grafana 登陆字符串，用户名为 admin
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

# 登陆 Grafana后，需要配置Prometheus DataSource，配置后方可读到相应的监控信息
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9118.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9119.webp)

Grafana 除了可以自定义大家需要的Dashboard之外，Grafana 社区有很多大家分享的比较漂亮的模板，大家可以挑选自己喜欢的模板，并进行二次更改。下面的页面，就是借用了 K8s Cluster Summary 和 ``

导入很简单，在 Import Dashboard中，输入 Dashboard 模板的编号即可。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9120.webp)

最终得到的页面如下所示：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9121.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9122.webp)

至此，我们已经完成了监控AKS集群性能指标的部分，下一部分将主要介绍如何搭建日志系统。

# Step 4 安装并配置日志系统
通过日志系统，我们可以将容器应用的Log，与Node的系统Log都收集到一起，进行统一的存储跟管理，当出现问题，可以通过日志系统快速定位问题。本次实验，基于 Elasticsearch & Fluent & Kibana 进行日志系统的构建。

```
# 添加 Helm repo，安装 ElasticSearch Operator
helm repo add akomljen-charts https://raw.githubusercontent.com/komljen/helm-charts/master/charts/
helm install --name es-operator --namespace logging akomljen-charts/elasticsearch-operator

# 创建 ElasticSearch
helm install --name efk --namespace logging akomljen-charts/efk
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9123.webp)

由于使用的 Helm Chart 没有定义 Kibana Service 的变量，将其从ClusterIP 改为 LoadBalancer，需要手动做这件事情。

```
# 查找并更改 Kibana Service Type
kubectl get svc -n logging
kubectl edit svc efk-kibana -n logging
```

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9124.webp)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E6%90%AD%E5%BB%BA%E5%9F%BA%E4%BA%8EPrometheus%26EFK%E7%9A%84%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%EF%BC%8C%E6%97%B6%E5%88%BB%E6%8E%8C%E6%8F%A1AKS%E9%9B%86%E7%BE%A4%E5%8A%A8%E5%90%9125.webp)

通过此实验，我们最终完整了如图所示的环境构建，能够看出，我们能够实时的看到目前集群的状态及节点状态等详细信息。

# 参考资料
AKS on Azure China Best Practices : https://github.com/Azure/container-service-for-azure-china/tree/master/aks

Helm 快速入门 : https://docs.helm.sh/using_helm/#quickstart-guide

Prometheus 介绍 ：https://prometheus.io/docs/introduction/overview/

Kubernetes Monitoring with Prometheus -The ultimate guide
: https://sysdig.com/blog/kubernetes-monitoring-prometheus/

Node exporter简介 : https://github.com/prometheus/node_exporter

kube-state-metrics介绍:https://github.com/kubernetes/kube-state-metrics

Grafana快速上手:http://docs.grafana.org/guides/getting_started/

Get Kubernetes Logs with EFK Stack in 5 Minutes : https://akomljen.com/get-kubernetes-logs-with-efk-stack-in-5-minutes/
