# 任务四：循迹而至

## 背景

在之前的任务中，您构建了一个卷积神经网络（CNN）来分类产品图像数据。组成一个 CNN 通常需要多个卷积（*convolutional*）、池化（*pooling*）和失活（*dropout*）层从图像中提取特征，以及一个或多个全连接（*fully-connected*）层把这些特征映射到分类的类别上去。

迁移学习（*Transfer Learning*）是一种常用的机器学习技术。在迁移学习中，您利用已有模型的提取特征的那些层，加入您新的全连接层，以从那些提取的特征来预测新的分类。

## 先决条件

* 一台数据科学虚拟机（DSVM）。
* 在之前任务中处理完成的经过缩放的  ***gear*** 图像数据集。
* 安装好您和您的团队所选择的深度学习框架的最新版本。具体可见页面最后的 **参考** 部分。

## 任务

本任务同样由三个子任务组成：

1. 探索一个迁移学习模型的例子。
2. 基于一个已有的模型，使用迁移学习技术训练一个分类器。
3. 将新的数据应用于您的模型。

### 1. 探索一个迁移学习模型的例子

在 **OCPOpenHack/Azure_Deep_Learning/notebooks** 文件夹中，仔细阅读 **04-Transfer Learning (*framework*).ipynb** notebook 文件中的代码和说明。这是一个使用迁移学习来训练一个 CNN 的例子。

### 2. 使用迁移学习技术训练一个模型

使用用迁移学习技术，从一个已有模型的特征提取层之上创建一个新的 CNN 的分类器。

#### 提示

* 在 DSVM 的 Jupyterhub 环境中，使用 **Python 3.5** 内核。
* 从提供的例子开始构建您的初始方案。
* 您可以使用您选定的深度学习框架支持的任意基础模型。
* 您需要缩放图像数据，以符合基础模型的训练要求。

### 3. 将新的数据应用于您的模型

使用您训练完成的模型来预测至少 5 张 **没有** 包含在 ***gear*** 数据集内的图像的产品分类。如果您在之前的任务中得到过这些图片，您可以复用它们。

## 成功条件

* 成功地从一个已有的模型训练出一个新的 CNN 。
* 按照 **子任务3** 的要求搜集至少 5 张图片，并能按如下格式呈现对它们的预测结果：

  ![Gear predictions](images/predicted_images.png)

  *(备注：模型不要求100%预测正确，但如果达到100%预测正确，团队值得庆贺一下。)*

如果您和您的团队确认已经全部达成上述成功条件，那么恭喜恭喜！您和您的团队已经完成了这个动手实验的全部任务！

## 参考

* <a href="http://cs231n.github.io/transfer-learning/" target="_blank">Transfer Learning Notes</a>
* <a href="https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html" target="_blank">Transfer Learning with PyTorch</a>
* <a href="https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html" target="_blank">Transfer Learning with Keras</a>
* <a href="https://www.tensorflow.org/hub/tutorials/image_retraining" target="_blank">Transfer Learning with TensorFlow</a>
* <a href="https://cntk.ai/pythondocs/CNTK_301_Image_Recognition_with_Deep_Transfer_Learning.html" target="_blank">Transfer Learning with CNTK</a>
