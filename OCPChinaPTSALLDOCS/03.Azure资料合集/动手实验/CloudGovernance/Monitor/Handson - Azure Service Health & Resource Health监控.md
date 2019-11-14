
## Handson Lab for Azure Service Health & Resource Health

`Service Health`是集中了解云平台中资源是否可用，或当平台出现问题时，及时了解问题进站及下载事故分析的地方; `Service Health`会提供包括`Service issue` & `Planned maintenance` & `Health advisories`在内的三种指标，建议在实际的生产环境中，针对这三种指标设置三个警报，分别对应特定`Action Group`, 确保不同问题能够找到合适处理的人。

![image](./images/service_resource_health_images/mon47.png)

`Resource Health`是能够及时反映正在使用的某一个Azure资源是否因为平台出现的问题，达到`Limitation`, 或性能出现显著降低的一种监控指标; 

资源是指Azure提供的服务，例如：`Virtual Machines` & `Application Gateway`等, 资源的状态会在 `Available` & `Unavailable` & `Unknown` & `Degraded` 之间转换，只要资源不处于 `Available` 状态，除非是一些已知的原因，比如：`手动停机`，都应该发送相应的警报引起负责人员的重视，资源处于非`Available`状态证明当前环境中正存在一种或多种资源不能正常使用。

![image](./images/service_resource_health_images/mon51.png)

针对 `Service Health & Resource Health`, 及时设置告警信息, 当环境中出现问题时, 能够快速定位, 并有效的处理问题.

### 针对 Service Health Service Issue & Planned Maintenance 设置告警

#### 设置 Action Group








### 参考资料

- [服务运行状况概述](https://docs.microsoft.com/zh-cn/azure/service-health/service-health-overview)

- [资源运行状况概述](https://docs.microsoft.com/zh-cn/azure/service-health/resource-health-overview)

- [Azure 资源运行状况中的资源类型和运行状况检查](https://docs.microsoft.com/zh-cn/azure/service-health/resource-health-checks-resource-types)

- [使用资源管理器模板创建资源运行状况警报](https://docs.microsoft.com/zh-cn/azure/service-health/resource-health-alert-arm-template-guide)




### 结合 Service Health & Resource Health，及时了解环境动态并设置告警

本次实验，将结合两个服务`Service Health` & `Resource Health`，设置相应的警报，确保当云平台或资源出现问题时，第一时间知晓。







本次实验将针对`Service issue`进行设置，另外两个的设置请自行练习。

![image](./images/monitor/mon48.png)

Step 1 选择需要涉及的订阅，区域，服务以及事件类别

![image](./images/monitor/mon49.png)

Step 2 选择Alert关联的`Action Group` 并进行创建

![image](./images/monitor/mon50.png)

这样当下一次平台中选中的服务出现问题或出现维护公告时，你会第一时间收到消息，确保可以及早处理突发事件。





本次实验将针对资源组下的所有资源类型`Resource Health`设置警报，有关涉及到的 ARM Template 请参阅 [arm-templates](./files/monitor/arm-templates/) 下的相应文件。

```
# 本次实验将使用 Azure CLI 结合 ARM 模板完成
# 针对 Resource Health 进行告警设置，当资源组下的某一资源状态从Available改变成Unavailable,Unknown,Degraded时，发送警报通知运维人员
# 获取ResourceID
az group show -n Prj01 --query id -o tsv

# 获取 Action Group ResourceID
az monitor action-group show -n Prj01 -g Prj01 --query 'id' -o tsv

# 设置Resource Health的警报
az group deployment create --name ResourceHealth01 -g Prj01 --template-file monitor-resources-health.json --parameters activityLogAlertName="ResourceHealthAlert_Prj01" --parameters '{ "scopes": {"value": ["$rgID"]}}' --parameters actionGroupResourceId='$actionGroupID'
```

设置完成后，当出现平台性问题导致资源状态变化，或如实验中，手动触发停止VM，就会发送告警信息。

![image](./images/monitor/mon52.png)

![image](./images/monitor/mon53.png)



---
