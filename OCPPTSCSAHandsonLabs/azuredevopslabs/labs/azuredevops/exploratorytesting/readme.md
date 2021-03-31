---
title: 使用Azure Test Plans测试计划进行探索性测试
layout: page
sidebar: vsts
permalink: /OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/exploratorytesting/
folder: /OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/exploratorytesting/
version: Lab version - 1. 38.0
updated: Last updated - 9/11/2019
redirect_from: "/labs/vsts/exploratorytesting/index.htm"
---
<div class="rw-ui-container"></div>
<a name="概述"></a>


## 概述 ##
在本实验中，您将了解“测试与反馈”扩展中提供的探索性测试和反馈管理功能。您将了解探索性测试（也称为XT或敏捷测试）如何成为工具集中的一流体验。这使测试人员可以更灵活地测试基础软件，而不必完全依赖正式的测试用例。您还将了解如何管理引发和管理客户反馈生命周期的过程。


<a name="先决条件"></a>
### 先决条件 ###

- 本实验要求您按照 <a href="../prereq/">先决条件</a>指令完成任务1和2。

<a name="Exercise1"> </a>
## 练习1：探索性测试 ##

<a name="Ex1Task1"> </a>
### 任务1：安装Chrome扩展程序 ###

1. 从[http://google.com/chrome](http://google.com/chrome)安装  **Google Chrome** 。本练习的其余部分将使用Chrome作为其浏览器。如果您已经在使用Chrome，则只需为下一组步骤打开一个新实例即可。

2. 导航至 **Azure DevOps Marketplace** : [http://marketplace.visualstudio.com](http://marketplace.visualstudio.com/).

3. 选择 **Azure DevOps** 选项卡。搜索 **feedback** ，然后单击“  **Test & Feedback** 扩展程序。

 ![](images/000.png)


4. 在详细信息页面上单击 **Install** 按钮。

 ![](images/001.png)

5. 点击 **Install** 以安装Chrome扩展程序。

 ![](images/002.png)

6. 在 **Chrome Web Store**中，单击 **Add to Chrome**。

 ![](images/003.png)

7. 询问时确认安装。

 ![](images/004.png)

8. 要打开扩展程序，请单击出现在地址栏右侧的扩展名图标。选择 **Connection Settings** 选项卡。输入您的Azure DevOps实例的URL，例如 **https://dev.azure.com/MYTEAM** 作为 **Server URL** ，然后单击 **Next**。

 ![](images/005.png)

9. 该扩展名可以在两种模式下使用： **Connected** 和 **Standalone** 模式。如果您具有Azure DevOps或Azure DevOps服务器，请选择“连接模式”。独立模式适用于既没有用户又不想使用扩展程序来提交错误并与团队共享报告的用户。

10. 连接到Azure DevOps之后，您将需要选择与这些工作相关联的团队。在 **Parts Unlimited**项目下选择 **Parts Unlimited Team** ，然后单击 **Save** 以继续。

 ![](images/006.png)

<a name="Ex1Task2"> </a>
### 任务2：使用Chrome扩展程序进行探索性测试 ###

1. 在 **Visual Studio**中，按 **F5** 本地构建并运行 **Parts Unlimited** 项目。

2. 要启动探索性测试会话，请单击扩展工具栏上的 **Start session** 按钮。

 ![](images/007.png)

3. 导航到 [http://localhost:5001](http://localhost:5001/)。

4. 在搜索框中输入 **"jumper lead"**  ，并按 **Enter** 键。

 ![](images/008.png)

5. 您将看到如下所示的搜索结果。

 ![](images/009.png)

6. 现在，在搜索框中输入 **"jumper leads"** 并按 **Enter** 键。

 ![](images/010.png)

7. 您可以看到没有搜索结果。当您搜索 **jumper lead** 时，它会显示结果。但是，当您搜索 **jumper leads** 时，它没有显示任何结果。这似乎是一个错误。

 ![](images/011.png)

8. 单击 **Exploratory Testing** 图标按钮，然后选择 **Capture screenshot | Browser** 。

 ![](images/012.png)

9. 选择屏幕的一部分，然后将屏幕快照的名称更改为更具描述性的名称。请注意，有许多可用的绘图工具可以真正帮助您理解要点。点击 **Blur area** 按钮。

 ![](images/013.png)

10. 突出显示屏幕截图的一部分，该部分将变得模糊不清，变得难以辨认。这使得报告错误和创建其他工作项变得容易，而不会冒敏感信息的风险。点击 **Save screenshot** 按钮，将其添加到当前会话的时间轴中。

 ![](images/014.png)

11. 单击 **Add note** 按钮开始注释。输入具有洞察力的内容，然后单击“保存”以将注释保存到会话的时间轴中。

 ![](images/015.png)

12. 您还可以录制屏幕视频以捕获不稳定的问题，例如闪烁，Web应用程序的异常行为等，这些问题很难单独使用屏幕快照捕获。要录制屏幕，请点击 **Record screen** 按钮，然后点击 **Start recording**。

 ![](images/016.png)

13. 从 **Application Window** 选项卡中选择要记录的适当屏幕。在这种情况下，请选择404页面，然后点击 **Share**。所选屏幕的录制已开始。

 ![](images/017.png)

14. 搜索 **"jumper lead"** 并显示结果。然后搜索 **jumper leads** ，并显示结果不足。

 ![](images/018.png)

15. 单击扩展名上的 **Stop recording** 按钮以停止录制屏幕。屏幕录像被保存。

 ![](images/019.png)

16. 单击 **View session timeline** 按钮。您可以看到所有内容-您捕获的屏幕截图，注释和视频都可以在当前会话的时间轴中找到。您可以从此处打开屏幕截图，阅读笔记或播放视频。

 ![](images/020.png)

<a name="Ex1Task3"> </a>
### 任务3：使用Chrome扩展程序创建错误 ###

1. 单击 **Create bug** 图标按钮，然后单击展开的 **Create bug** 文本按钮。

![](images/021.png)

2. 输入 **"Search for jumper leads fails"** 作为错误的名称。先前捕获的所有屏幕截图和视频已经是该错误的一部分。除此之外，还为您插入了图像操作日志（用户操作），以便其他人可以轻松地重现该问题。单击 **Save** ，将错误保存到Azure DevOps。

 ![](images/022.png)

3. 此扩展的另一个重要功能是它能够查看类似的错误，从而减少冗余问题。假设您是另一位测试人员，恰巧发现了这个错误，却不知道它已被记录。再次单击 **Create bug** 图标按钮，然后再单击扩展的“Create bug”文本按钮，以启动新的错误表单。

 ![](images/023.png)

4. 在为错误键入标题 **"jumper leads** "时，您会注意到扩展名已检测到积压工作中已经存在另一个标题相似的错误。单击 **1 similar** 以查看类似的错误。

 ![](images/024.png)

5. 此错误似乎与我们将要提交的错误相同，因此，请选择它并单击**Edit** 以编辑现有错误，而不是提交新的错误。

 ![](images/025.png)

6. 此时，新的再现步骤已添加到图像操作日志中。实际上，您现在将查看之前已经存在的相似步骤，以确定你找到的那个已存在的Bug是否使用其他方法，在这种情况下，您将更新内容以指示您的方法是另外的重现。单击 **Save** 以保存错误。

 ![](images/026.png)

7. 单击 **View session timeline** 图标按钮，然后单击最后创建的 **Bug** 链接以将其打开。

 ![](images/027.png)

8. 现在回到Azure DevOps站点，您可以根据需要更新错误，例如，将错误分配给某人或调整严重性。

 ![](images/028.png)

9. 在Chrome浏览器中，通过单击 **Stop Session** 按钮结束测试会话。

 ![](images/029.png)
