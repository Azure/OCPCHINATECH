# 任务三 - 云上漫步

## 背景

能构建出一个具有世界领先水准的机器学习模型并不是终极目标，您还需要知道如何去部署模型，这样，您的团队成员、软件开发人员甚至是 Adventure Works 之外的第三方都能在应用程序或服务中使用它，进而为客户提供有价值的功能。

在本任务中，您将使用 *Azure Machine Learning Services* 和 *Azure Machine Learning SDK* 把您的模型变成一个在云端的推断服务，具体而言，是一个容器化的 Web 服务。这样，Adventure Works 内部的软件开发人员可以在给顾客的应用程序中使用这个推断服务进行预测。

## 先决条件

* 一台数据科学虚拟机（DSVM）。
* 在之前的任务中所完成的训练一个图像分类模型的代码。

## 任务

本任务也由三个子任务组成：

1. 探索 Azure 机器学习的部署。
2. 把您的登山工具分类模型部署成一个 Web 服务。
3. 使用您的 Web 服务。

### 1. 探索 Azure 机器学习的部署

在 **OCPOpenHack/Azure_Deep_Learning/notebooks** 文件夹中，仔细阅读 **03-Azure ML (*framework*).ipynb** notebook 文件中的代码和说明。这个例子展示了如何使用 Azure 机器学习来把一个模型部署成一个容器化的 Web 服务。

### 2. 把您的分类模型部署成一个 Web 服务

使用 *Azure Machine Learning SDK* 创建一个 Azure Machine Learning Workspace，并且把您的登山工具分类模型部署为运行在 Azure 容器实例（ACI）服务中的容器上的一个 Web 服务。

### 提示

* 在 DSVM 的 Jupyterhub 环境中，使用 **Python 3.6 - Azure ML** 内核。
* 您的部署必须包含一个评分（Scoring）脚本，在脚本中完成载入模型、根据输入数据生成一个预测，和返回该预测结果。对训练数据执行的那些预处理操作，也别忘记对要预测的输入数据进行同样的操作。
* 您需要在一个 .yml 文件中指定评分脚本必需使用的那些 Python 库。这样当部署时，这些库才会被安装在容器镜像中。
* 对于输入和输出数据的预期格式必须非常小心，因为在部署后它们是通过 HTTP 来交换的。

### 3. 使用您的 Web 服务

编写一些代码来调用您部署好的 Web 服务，它应当根据您选定一张新的图像返回预测的类别。

## 成功条件

* 部署完成一个包含您的模型的容器镜像。
* 运行的 Python 代码能顺利调用您部署的 Web 服务，展现其对新的图像数据的预测结果。

如果您和您的团队确认已经全部达成上述成功条件，可以继续进入 [下一任务](Challenge04.md) 接受挑战。

## 参考

* <a href="https://docs.microsoft.com/en-us/azure/machine-learning/service/overview-what-is-azure-ml" target = "_blank">What is Azure Machine Learning Service?</a>
* <a href="https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-deploy-to-aci" target="_blank">Deploy models with the Azure Machine Learning service</a>