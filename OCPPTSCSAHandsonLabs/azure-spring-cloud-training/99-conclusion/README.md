# 总结

**本教程是[Azure Spring Cloud 培训](../README.md)系列之一**


---

## 清理

除非您想要使用Workshop的 Azure 资源执行其他任务（如下面引用的教程），否则必须清理我们创建的资源，以避免产生不必要的成本。

最简单的方法是删除整个资源组。

> 🛑将资源组的名称替换为`$AZ_RESOURCE_GROUP`下面：

```bash
az group delete -g "$AZ_RESOURCE_GROUP" --yes --no-wait
```

## 其他资源

作为本Workshop的附加练习，建议完成[使用带有 Azure Spring Cloud的警报和Action Group的教程](https://docs.microsoft.com/azure/spring-cloud/spring-cloud-tutorial-alerts-action-groups/?WT.mc_id=azurespringcloud-github-judubois) 来实现检测和响应异常情况。

此外，请查看我们的教程[部署Azure Spring Cloud到虚拟网络](https://docs.microsoft.com/azure/spring-cloud/spring-cloud-tutorial-deploy-in-azure-virtual-network).

也可以通过[Azure Spring Cloud文档](https://docs.microsoft.com/azure/spring-cloud/)来学习更多快速开始、教程和参考材料。

了解更多有关监控能力的 - [带应用洞察的Spring Cloud](https://docs.microsoft.com/en-us/azure/spring-cloud/spring-cloud-howto-application-insights?WT.mc_id=java-13165-sakriema).

---

⬅️上一个教程：[12 - 微服务间的相互调用](../12-making-microservices-talk-to-each-other/README.md)
