---
title: 使用Azure Test Plans进行测试计划和管理
layout: page
sidebar: vsts
permalink: /OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/testmanagement/
folder: /OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/testmanagement/
version: Lab version - 15.8.2
updated: Last updated - 9/6/2018
redirect_from: "/labs/vsts/testmanagement/index.htm"
---
<div class="rw-ui-container"></div>
<a name="概述"></a>



 ## 概述  ##

在本实验中，您将学习如何使用Azure DevOps管理项目的测试生命周期。该项目将指导您创建旨在有效验证软件里程碑的测试计划。您还将创建并执行手动测试，这些手动测试可以在每个发行版的过程中一致地进行复制。

<a name="先决条件"></a>
### 先决条件 ###  

-本实验要求您按照<a href="../prereq/">先决条件</a>指令完成任务1和2。


<a name="Exercise1"> </a>
## 练习1：管理测试计划，套件和案例 ##

在本练习中，您将学习如何创建和管理测试计划，测试套件和测试用例。

<a name="Ex1Task1"> </a>
### 任务1：了解测试计划，套件和案例 ###  

1. 导航到Azure DevOps上的团队项目。

2. 选择 **Test Plans** 以导航到 **Test Hub**。测试中心为所有测试计划，执行和分析提供了一个中心位置。

 ![](images/000.png)


3. 一般来说，项目中的每个主要里程碑都应有自己的 **test plan**。每个测试计划中都有 **test suites**，它们是旨在验证工作项（例如功能实现或错误修复）的 **test cases** （以及可选的其他测试套件）的集合。每个测试用例都旨在确认一种特定的行为，并且可能属于一个或多个测试套件。零件无限制项目有一个测试计划，该计划位于 **Parts Unlimited Team** 下，称为**Parts Unlimited_TestPlan1** 。选择 **Parts Unlimited_TestPlan1** 。

 ![](images/001.png)

4. 为该故事选择测试套件 **As a customer, I would like to store my credit card details securely** 。这组测试重点在于该工作项，而该工作项恰好是一项功能。请注意，每次您为实验室生成演示数据时，工作项编号都会有所不同。

 ![](images/002.png)

5. 在右侧，您可以看到该测试套件具有三个测试用例，旨在确认功能实现的预期行为。双击 **Verify that user is allowed to save his credit card detail** 测试用例。

 ![](images/003.png)

6. 此对话框提供了有关此测试用例所需的所有信息。找到 **Related Work** 面板，并注意此测试用例已链接到它所属的套件。单击工作项以导航到它。

 ![](images/004.png)

7. 在测试套件中，我们可以看到所有链接的工作项，它们恰好是测试用例。

 ![](images/005.png)

8. 但是，它尚未与旨在测试的功能相关联，我们现在可以将其链接。点击**Add link \| Existing item**。

 ![](images/006.png)

9. 将 **Link type** 设置为 **Parent** ，然后搜索 **"credit card"** 。

 ![](images/007.png)

10. 选择**Credit Card Purchase** 的 **Feature** 。

 ![](images/008.png)

11. 单击 **OK** 。

 ![](images/009.png)

12. 父功能现在与对其进行测试的套件相关联，并且任何人都可以在它们之间导航以查看其与所涉及的其他工作项的关系。

 ![](images/010.png)

13. 单击 **Save & Close**。

 ![](images/011.png)

14. 关闭原始的测试用例对话框。

<a name="Ex1Task2"> </a>
 ### 任务2：管理测试 ###  

1. 有时应按特定的顺序运行一组测试用例，以使效率最大化。可以直接长按并拖动测试用例来改变顺序。

 ![](images/012new.png)

2. 虽然可以单独运行这些测试用例以确认行为，但最好先运行拒绝无效卡的测试用例。然后，测试人员可以确认可以保存有效卡，然后是测试用例以编辑已保存的卡。将第二个测试用例拖放到第一个测试用例上方，然后单击列头 **Order** 进行重新排序。

 ![](images/013new.png)

3. 现在，您可以看到 **Order** 已更新，并且列表已按其排序。


4. 测试的另一个重要方面与运行每个测试的环境有关。对于此Web应用程序，浏览器和操作系统是关键考虑因素。目前，所有测试仅使用一种配置：Windows 10。

 ![](images/015.png)

5. 选择 **Configurations** 选项卡。

 ![](images/016.png)

6. 请注意，有一个 **Windows 10** 现有的配置。每个测试配置都包括名称和描述，以及一组可自定义的**Configuration variables**。该项目为 **Operating System** 设置了一个配置变量。您可以轻松添加更多和/或编辑每个条目的可用条目。点 **Add configuration variable** 。

 ![](images/017.png)

7. 选择 **Browser** 变量并将其设置为 **Microsoft Edge** 。

 ![](images/018.png)

8. 单击 **Save** 以保存配置。

 ![](images/019.png)

9. 现在，假设测试团队已经购买了iPhone X，并希望将其添加到测试矩阵中。将环境注册为新配置非常容易，以便测试用例可以指定它。不过，在添加之前，我们需要针对 **iOS 10** 的 **Operating System** （操作系统）选项。单击 **Operating System** 配置变量。

 ![](images/020.png)

10. 单击 **Add new value** 并为 **iOS 12** 添加一个条目。

 ![](images/021.png)

11. 单击 **Save**。

 ![](images/022.png)

12. 现在，我们拥有添加iPhone X所需的一切。单击 **Add** 下拉列表，然后选择 **New test configuration** 。

 ![](images/023.png)

13. 将 **Name** 设置为 **"iPhone X"**。

 ![](images/024.png)

14. 双击 **Add configuration variable** ，然后将**Browser** 设置为 **Safari** ，将 **Operating System** 设置为 **iOS 12** 。

 ![](images/025.png)

15. 单击 **Save** 以保存新配置。

 ![](images/026.png)

16. 返回 **Test Plans** 选项卡。

 ![](images/027.png)

17. 单击到目前为止我们一直在使用的测试套件旁边的下拉列表，然后选择 **Assign configurations to test suite**。

 ![](images/028new.png)

18. 选中 **iPhone X** 选项，然后单击 **Save**。

 ![](images/029.png)

19. 请注意，每个测试用例均已使用 **iPhone X** 的附加配置进行了复制。现在可以分别测试和跟踪每个环境。

 ![](images/030new.png)

<a name="Ex1Task3"> </a>
  ###  任务3：编写测试  ###  

1. 展开测试计划旁边的下拉菜单，然后选择 **New static suite.** 测试用例的 **static suite** 是已手动分配用例的套件。您还可以基于通用需求 ( **requirement-based suite** ) 或测试用例和/或工作项的查询( **query-based suite** )来创建套件。

 ![](images/031new.png)

2. 将新套件的名称设置为 **Shipping tests**。这些测试将全部集中在与运输相关的功能上。请记住，您可以轻松地在套件之间共享测试用例，因此，在有许多重叠套件时，冗余度很小。

 ![](images/032.png)

3. 展开新创建的套件旁边的下拉菜单，然后选择 **New requirement-based suite**。

 ![](images/033new.png)

4. 您可以自定义用于指定要检索哪些需求的查询，但只需保留默认值，然后单击 **Run query**即可。找到并选择与运输相关的三个产品待办事项, 按住Ctrl来进行多选。单击 **Create suites** 以为每个套件创建一个测试套件。

 ![](images/034.png)

5. 选择一个新创建的套件，例如与跟踪程序包状态关联的套件。

 ![](images/035.png)

6. 虽然可以一次创建一个测试用例，但有时使用网格布局来快速添加许多测试用例会更容易。在测试用例面板中，选择 **New Test Case \| Add test case using grid**。

 ![](images/036new.png)

7. 输入一些测试用例，然后单击 **Save All** 按钮。 **Title** 将是测试用例的最终标题。 **Step Action** 将是测试的第一步（可能也是唯一一步）。如果该步骤具有预期结果，则可以将其指定为 **Step Expected Result**。

 ![](images/037.png)

8. 您可以选择继续在网格视图中添加和编辑工作项。如果满意，请单击 **Close Grid** 切换返回列表视图。

 ![](images/038.png)

9. 列表视图显示相同的数据，但视图不同。

 ![](images/039.png)

10. 创建套件的另一种方法是通过工作项查询。展开 **Shipping tests** 套件旁边的下拉菜单，然后选择 **new query-based suite**。

 ![](images/040new.png)

11. 假设您想从与项目中交付相关的测试用例中创建一个测试套件。将 **Work Item Type** 更改为 **Microsoft.TestCaseCategory** 以搜索测试用例，然后单击 **Run query**。现在，您将获得一个测试用例列表，可以选择从中创建套件。

 ![](images/041-2.png)

12. 按 **Esc** 关闭对话框。

<a name="Exercise2"> </a>
 ## 练习2：创作，运行和分析手动测试 ##

在本练习中，您将学习如何创建手动测试计划并按步骤进行填充。以后可以运行该计划，以确认软件的预期行为。在本实验中，我们将专注于创建新的手动测试用例并运行它。

<a name="Ex2Task1"> </a>
  ###  任务1：安装测试和反馈扩展  ###  

1. 从[http://google.com/chrome](http://google.com/chrome)安装 **Google Chrome** 。本练习的其余部分将使用Chrome作为其浏览器。如果您已经在使用Chrome，则只需为下一组步骤打开一个新实例即可。

2. 导航至[http://marketplace.visualstudio.com](http://marketplace.visualstudio.com/)上的 **Azure DevOps Marketplace** 。

3. 选择 **Azure DevOps** 选项卡。搜索 **feedback**  ，然后单击 **Test & Feedback** 扩展插件。

 ![](images/042.png)

4. 在详细信息页面上单击 **Install** 按钮。

 ![](images/043.png)

5. 点击 **Install** 以安装Chrome扩展程序。

 ![](images/044new.png)

6. 在 **Chrome Web Store**中，单击**Add to Chrome**。

 ![](images/045.png)

7. 询问时确认安装。

 ![](images/046.png)

8. 要打开扩展名，请单击出现在地址栏右侧的扩展名图标。选择 **Connection Settings** 选项卡。输入Azure DevOps实例的URL，例如 **https://dev.azure.com/[YOURTEAM]** 作为 **Server URL** ，然后单击 **Next**。

 ![](images/047new.png)

9. 该扩展名可以在两种模式下使用： **Connected** 和 **Standalone** 模式。如果您有Azure DevOps或Team Foundation Server（TFS），请选择“连接模式”。独立模式适用于没有Azure DevOps或TFS并希望使用扩展程序来提交错误并与团队共享报告的用户。

10. 连接到Azure DevOps之后，您将需要选择与这些工作相关联的团队。在 **Parts Unlimited** 项目下选择**Parts Unlimited Team** ，然后单击 **Save** 以继续。

 ![](images/048.png)

<a name="Ex2Task2"> </a>
 ### 任务2：编写手动测试计划 ###  

1. 在Chrome浏览器中，导航到 **Parts Unlimited** 项目。

2. 和以前一样，导航至 **Test Plans** 中枢Hub。

 ![](images/049.png)

3. 展开测试计划旁边的下拉列表，然后选择 **New static suite** 。

 ![](images/050new.png)

4. 将新套件命名为 **"End-to-end tests"** ，然后按 **Enter**。

 ![](images/051.png)

5. 从右边栏，点击 **New Test Case** ，以创建新的测试用例。

 ![](images/052new.png)

6. 在 **Title** 框中，键入 **Confirm that order number appears after successful order** 作为新测试用例的名称。

 ![](images/053.png)

7. 至此，我们准备为该手动测试添加步骤。每个步骤都包含一 **Action**，它描述了测试人员需要执行的操作。可选地，一个步骤可以包括 **Expected Result**，它描述了给定操作的预期结果。在 **Steps** 面板中，为以下每个 **Actions** 创建一个步骤，其中只有一个具有 **Expected Result** 。

    |Action|Expected Result|
    --- | ---
    |Open project site||
    |Click Brakes||
    |Click Disk and Pad Combo||
    |Click Add to Cart||
    |Click Checkout||
    |Enter @Email, @Password||
    |Enter @Name, @Phone, @Email, @Address, @City, @State, @PostalCode, @Country, @Promo||
    |Click Submit Order||
    |Confirm order page has order #|Order # should appear on order confirmation page|
    |Log out||
    |Close browser||

   **注意：** 如果最后空了一步，请将其删除。


8. 此时， **Steps** 面板应类似于以下内容：

 ![](images/054.png)

9. 注意 "Enter @Email, @Password" and "Enter @Name, @Phone, @Email, @Address, @City, @State, @PostalCode, @Country, @Promo"  步骤。在这些步骤中，我们使用 **@** 符号表示在手动测试过程中将使用特定于迭代的变量。我们可以通过向下滚动到此表单的 **Parameter Values** 部分并为每次迭代输入它们来定义要使用的变量。请注意，您可能需要使用测试用例对话框最右侧的滚动条来查看此部分。

 ![](images/055.png)

10. 使用下表设置两次迭代的值。



   |Fields|Iteration 1|Iteration 2|
   --- | --- | ---
   |Email|admin@test.com|sachin@test.com|
   |Password|P@ssw0rd|P@ssw0rd|
   |Name|Admin User|Sachin Raj|
   |Phone|425-555-1234|555-555-5555|
   |Address|One Microsoft Way|Two Tailspin Trail|
   |City|Redmond|Springfield|
   |State|WA|IL|
   |PostalCode|98052|11135|
   |Country|USA|USA|
   |Promo|FREE|FREE|



11. 现在， **Parameter Values**  部分应如下所示。请注意，您可以根据需要输入尽可能多的迭代来完全测试场景的广度。

 ![](images/056.png)

12. 单击 **Save & Close** 以保存测试用例。

 ![](images/057.png)

<a name="Ex2Task3"> </a>
  ###  任务3：运行手动测试计划  ###  

1. 在此任务中，您将学习如何运行我们之前创建的手动测试计划。请注意，触发自动测试运行的过程遵循类似的工作流程。 [文档](https://docs.microsoft.com/en-us/vsts/build-release/test/run-automated-tests-from-test-hub)中了解有关此内容的更多信息。

2. 右键单击先前创建的测试用例，然后选择 **Run with options** 以开始手动测试运行。

 ![](images/058new.png)

3. 您可以使用一些选项来自定义每个测试运行。第一个选项是选择 **Runner**，它将是这种情况下的浏览器。接下来，您可以选择指定要收集哪种 **类型数据** 。最后，您可以选择指定要测试的构建，以便更轻松地将结果与它们来自的构建相关联。单击 **OK** 继续。

 ![](images/059.png)

4. 如果没有出现 **Test Runner** 窗口，请检查它是否被弹出窗口阻止程序阻止。如果是这样，请单击**Pop-up blocker** 按钮，选择 **Always allow pop-ups...**，然后单击 **Done**。然后，您可以成功再次启动测试运行。

5. 在 **Test Runner** 窗口中，展开 **Test 1 of 1: Iteration 1** 下拉菜单。请注意，这里有两次迭代：对于测试用例中指定的每组参数，一次迭代。在第一次迭代中，使用 [admin@test.com](mailto:admin@test.com) 帐户。在第二个中，将使用 [sachin@test.com](mailto:sachin@test.com) 。

 ![](images/060.png)

6. 测试的第一步是打开项目站点。为此，请切换到已加载 **Parts Unlimited** solution的 **Visual Studio** 实例。从 **IIS Express** 目标下拉列表中，选择 **Browse With...**。

 ![](images/061.png)

7. 选择 **Google Chrome** ，然后单击 **Browse**。

 ![](images/062.png)

8. 如果您在大屏幕上工作，则调整新窗口的大小以适合 **Test Runner** 窗口旁边可能会更容易。否则，您可以来回切换。

 ![](images/063.png)

9. 网站载入后，返回 **Test Runner** 并单击 **Pass test step** 按钮。完成此测试的后续步骤时，请确保也检查它们的 **Pass test step** 按钮。

 ![](images/064.png)

10. 下一步是单击 **Brakes** 菜单。

 ![](images/065.png)

11. 然后单击 **Disk and Pad Combo** 产品。

 ![](images/066.png)

12. 下一步是单击 **Add to cart**。

 ![](images/067.png)

13. 在下一页上，单击 **Checkout**。

 ![](images/068.png)

14. 使用下一步中指定的凭据登录。

 ![](images/069.png)

15. 不幸的是，这将失败，因为没有[admin@test.com](mailto:admin@test.com)帐户。

 ![](images/070.png)

16. **Test Runner** 提供了三种有价值的方式来记录测试运行中的媒体。第一种选择是截取屏幕截图。第二个是在图像操作日志中捕获每个用户操作。最后是将屏幕录制为视频。单击**Capture screenshot** 按钮以捕获屏幕快照。

 ![](images/071.png)

17. 缩小屏幕以显示登录表单和错误消息。指定名称 **"No admin account"** ，然后单击“确认”按钮。

 ![](images/072.png)

18. 右键单击失败的步骤，然后选择 **Add comment**。

 ![](images/073.png)

19. 输入注释 **"Admin account does not exist by default"** ，然后使用 **Fail test step** 按钮使测试失败。

 ![](images/074.png)

20. 单击 **Create bug** 以记录新的错误。

 ![](images/075.png)

21. 输入错误标题 **"Admin account does not exist by default"** ，然后单击 **Save & Close** 以记录该错误。

 ![](images/076.png)

22. 由于由于与测试功能不直接相关的错误而无法完成测试，因此请展开 **Mark test case result** 下拉菜单并选择 **Block test** 。单击**Save and close** 以保存测试运行。

 ![](images/077.png)

23. 关闭测试浏览器窗口。

<a name="Ex2Task4"> </a>
  ###  任务4：分析手动测试结果  ###  

1. 在此任务中，您将学习如何查看手动测试运行的结果。

2. 返回托管 **Test Hub**的浏览器窗口。选择 **Runs** 标签。

 ![](images/078.png)

3. 双击最新的测试运行以将其打开。您可能需要刷新数据才能看到它。

 ![](images/079.png)

4.  **Run summary** 选项卡提供测试运行的概述，以及运行中包含的所有测试结果的高级详细信息。

 ![](images/080.png)

5. 选择 **Test results** 选项卡。此选项卡列出了运行中包含的每个测试案例的结果及其结果。由于此处仅包含一个测试用例，因此双击它以将其打开。

 ![](images/081.png)

6. 您可以从此处查看此特定测试用例的所有详细信息。

 ![](images/082.png)

7. 滚动到底部以找到迭代。展开第一次迭代。

 ![](images/083.png)

8. 查看此迭代中每个步骤的结果以及失败的登录步骤，该步骤显示了测试运行过程中随附的屏幕截图。

 ![](images/084.png)

<a name="Ex2Task5"> </a>
  ###  任务5：创建共享步骤  ###  

1. 在此任务中，您将学习如何创建共享步骤。共享步骤将通常按顺序执行的多个步骤组合为一个逻辑步骤，可以在测试之间共享。如果将来由共享步骤定义的过程发生变化，则可以在一处更新共享步骤，它将在引用该共享步骤的所有测试中得到反映。

2. 单击 **Summary** 部分中的测试用例链接。

 ![](images/085.png)

3. 双击案例以在测试案例编辑器中将其打开。

 ![](images/086.png)

4. 选择步骤2-4（使用 **Shift+Click**），然后单击 **Create shared steps** 按钮。

 ![](images/087.png)

5. 将这些共享步骤的名称设置为 **"Add Disk and Pad Combo to cart"** ，然后单击 **Create** 。

 ![](images/088.png)

6. 现在，您可以看到以前的步骤已被共享步骤替换。双击共享步骤以打开。

 ![](images/089.png)

7. 如有必要，您可以稍后重新访问这些步骤，以针对新要求更新它们。

 ![](images/090.png)

8. 按 **Esc** 关闭 **Shared Steps** 对话框。

9. 单击 **Save & Close** 以保存测试用例。

 ![](images/091.png)
