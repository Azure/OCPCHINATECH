# Playbook（剧本）

Dynamics 365 面向销售人员正在引入 Playbook, 这是一种新功能, 可帮助您自动执行可重复的销售活动并响应外部事件。

在客户的时代, 购买人员在与卖家的关系中占据上风。由于对信息的访问几乎是无限的, 他们可以规定自己的客户旅程, 而不是遵循预定义的业务流程。因此, 重要的是从记录系统上的反应过程驱动的数据存储库转向主动和预测事件驱动的指导引擎, 这些引擎可以提出下一个最佳行动, 并开展相关的销售活动, 以成功应对外部事件。准

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8901.jpg)

Playbook 为用户提供有关定期任务的指导, 在这些任务中, 需要一致的操作。Playbook 还可以包含基于以前在类似情况下工作过的实践的最佳实践。

如果决策者和产品拥护者在交易过程中离开组织, 这可能成为一个有可能危及整个商业交易的事件。

但是, 使用 Playbook, 自动化可以触发游戏, 创建一组纠正这种情况所需的任务和活动。在执行一项任务, 接触客户账户上的当前联系人并确定新的利益攸关方之后, 可以立即打一个介绍性电话, 以更好地了解新的利益攸关方的优先事项。这种精心打造的活动编排确保了新的决策者被成功识别, 并成为产品的新拥护者, 这样交易就可以挽救。

发布的新功能允许组织:

* 针对任何 Dynamics 365 实体配置 Playbook
* 定义一组任务和活动, 以便在触发后自动执行
* 跟踪运行 Playbook 的状态进度, 以了解其结果 (成功与否)

# 演示简介

创建一个Playbook来处理机会变冷的场景。这可以自动化, 但在本例中, 将更多地关注手动方案。

首先, 创建一个新的 Playbook 类别, 然后创建一个新的 Playbook 模板 (与商机实体相关)。该手册将创建一个电话活动和一个预约时间活动, 试图再次加热的机会。创建了Playbook之后, 展望未来, 我们可以使用新的机会记录从任何商机记录中命令栏中的**启动Playbook**命令。

# 演示步骤

导航到**App Setting**(1) 然后**Playbook Categories**(2) 打开**Active Playbook Categories**网格

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8902.jpg)

在**Active Playbook Categories**网格点击**New** (1) 打开**New Playbook category**形式

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8903.jpg)

在**New Playbook category**填写表格**Name**和 (可选) **Description**字段 (1), 然后单击**Save & Close** (3)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8904.jpg)

导航到**Playbook templates** (2)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8905.jpg)

在**All Playbook Templates**网格点击+ **New**(1) 打开**New Playbook template**形式

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8906.jpg)

在**New Playbook template**填写字段

1. **Category**.选择要为其创建Playbook模板的类别。将类别视为要使用此模板解决的事件或问题。
2. **Name**.输入模板的描述性名称。
3. **Track progress**. 选择是否通过在Playbook下创建活动来跟踪Playbook的进度, 而Playbook又链接到Playbook应用于的记录类型。

  例如, 如果您为商机创建了模板, 并且您将**Track Progress**到 "Yes", 所有Playbook活动都是在从以下层次结构中的商机记录启动的Playbook下创建的: 商机记录→Playbook记录→活动。

  如果将其设置为 "No", 则将在以下层次结构中的商机记录下直接创建Playbook活动: 商机记录→活动。

4. **Estimated duration (days)**.输入估计持续时间 (以天为单位), 以指示启动后完成Playbook模板可能需要的时间

点击**Save** (5) 创建 Playbook 模板记录

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8907.jpg)

在 Playbook 模板窗体中, 您将看到几个部分来处理要使用 Playbook 定位的实体, 以及哪些实体活动在Playbook推出时创建。

1. **Select record types that this playbook applies to-**在本节中, **Available for**框中列出了启用使用Playbook的所有实体。选择当前Playbook模板应用到的记录类型并将其移动到**Applies**到框。
2. **Playbook activities-**在本节中, 选择**Add Activity**, 然后选择要创建的活动。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8908.jpg)

我们将选择**Opportunity** (1) 然后再加上一些活动 (2)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8909.jpg)

当您单击**Add Activity**在**Playbook Activities**部分, 将显示包含活动类型 (任务、电话呼叫、约会) 的下拉列表。

选择例如 **Appointment**, 以打开任务窗格**Quick create: Playbook appointment**

在**Quick create: Playbook appointment**任务窗格中, 填写下面的字段 (1), 然后选择 "保存 (2)" 以保存约会活动:

* **Subject**.键入活动目标的简短说明
* **Description**.键入描述Playbook活动的其他信息
* **Relative start date (days)**.输入活动必须在其中开始的天数。此日期相对于Playbook的推出时间
* **Relative start time**.输入一天中必须开始活动的时间
* **Relative end date (days)**.输入活动必须结束的天数。此日期相对于Playbook的推出时间
* **Relative end time**.输入活动必须结束的一天中的时间
* **Priority**.选择活动的优先级

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8910.jpg)

约会活动现在列在**Playbook activities**第 (1) 条。点击**Add Activity** (2) 然后**Phone Call**创建电话呼叫活动

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8911.jpg)

在**Quick create: Playbook phone call**任务窗格填写下面的字段 (1), 然后选择**Save** (2) 保存电话活动

* **Subject**.键入活动目标的简短说明
* **Description**.键入描述Playbook活动的其他信息
* **Relative due date (days)**.输入活动到期的天数。从Playbook的发布日期开始计算天数。此字段仅适用于任务和电话呼叫活动
* **Relative due time (hours)**.输入活动到期的时间
* **Duration**.如果要创建任务或电话呼叫, 请选择任务或电话呼叫活动的持续时间
* **Priority**.选择活动的优先级

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8912.jpg)

电话呼叫活动现在列在**Playbook activities** (1)。

您必须发布Playbook, 以便为用户提供。点击**Publish** (2) 出版Playbook

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8913.jpg)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8914.jpg)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8915.jpg)

一旦Playbook发表我们可以打开一个机会, 并找到一个新的**Launch playbook**中的命令。命令栏(1). 单击命令按钮以显示**Playbook templates**对话框

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8916.jpg)

在**Playbook templates**对话框中选择您创建的Playbook (1), 然后单击 **Launch**推出Playbook

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8917.jpg)

若要查看创建的活动导航到Playbook模板, 请单击**Monitoring**选项卡 (2), 并验证是否有两个播放簿列表条目活动 被创造 (如预期)-注意关于专栏显示机会的名字 ("Social Engagement")。您可以双击要导航到 Playbook 记录的播放簿列表项 (3)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8918.jpg)

在Playbook表格上, 你可以找到Playbook记录的部分, 包括相关的机会 (1) 和活动 (2)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8919.jpg)

您还可以导航到**My Activities**列出并找到那里的活动。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/%E5%87%86%E5%A4%87%E5%A5%BD%E9%80%82%E7%94%A8%E4%BA%8E%E9%94%80%E5%94%AE%E7%9A%84Dynamics365%E4%B8%AD%E7%9A%84%E6%96%B0Playbook%EF%BC%88%E5%89%A7%E6%9C%AC%EF%BC%8920.jpg)

希望这个例子能激励大家去探索 Playbook 如何帮助你成功地应对外部事件。

说明：（本博客引用自Microsoft Lystavlen的文档。）
