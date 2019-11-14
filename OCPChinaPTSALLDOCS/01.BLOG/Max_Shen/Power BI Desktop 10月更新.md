本月的 Power BI Desktop更新在整个产品中都有小的和大的改进。一个巨大的更新是Power BI服务支持复合模型和聚合预览。我们本月还有两个重要的数据准备功能: 合并查询和数据分析以帮助识别质量问题时的模糊匹配功能。

主要更新：

# [报表](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#reporting)

* [过滤器搜索](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#search)

* [提升可访问的创作体验](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#accessibility)

* [ArcGIS Map性能提升](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#esri)



# [模型](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#modeling)

* [DAX 编辑器提升](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#daxEditor)



# [分析](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#analytics)

* [Power BI 服务中的复合模型和聚合支持 (预览版)](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#compositeModels)

* [Explain the increase for non-additive measures](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#Insights)



# [自定义视图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#customVisuals)

* [Mapbox 更新 - 填充地图3D 拉伸 & more](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#mapbox)

* [Various bar & column chart visuals by Akvelon](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#akvelon)

* [3AG Systems – 带小倍数柱状图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#smallMultiples)

* [3AG Systems –带绝对方差的条状图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#barVariance)

* [3AG Systems –带相对方差的柱状图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#columnVariance)



# [数据连接](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dataConnectivity)

* [Web By Example connector正式可用](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#webByExample)

* [SAP BW Connector implementation v2 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#sapBW)

* [SAP BW Message Server Connector 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#sapBWMessageServer)

* [Vertica connector 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#vertica)

* [Dynamics NAV and Dynamics 365 Business Central connectors 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dynamics)

* [New Dynamics 365 Business Central On-premises connector](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dynamicsOnPrem)



# [数据准备](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dataPrep)

* [查询编辑器中的数据分析 (预览)](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dataProfiling)

* [合并查询的模糊匹配选项 (预览)](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#fuzzyMatching)



# [其他](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#other)

* [控制报表的导出数据选项](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#exportControl)

* [传输层安全设置](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#tls)



# [报表](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#reporting)

* [过滤器搜索](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#search)



自2016年6月更新以来, 已经在切片器中进行了搜索, 现在随着本月的更新, 我们也将其添加到基本的过滤卡中。此功能在我们的切片器中非常受喜爱和使用,

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B001.jpg)

* [提升可访问的创作体验](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#accessibility)

作为我们持续的可访问性工作的一部分, 在 Power BI 团队和整个 Microsoft, 这个月我们有很多与创作和修改报告相关的改进。我们的领域现在可以只使用键盘导航, 并与屏幕阅读器进行良好的交互。为了帮助提高使用屏幕阅读器和键盘编辑图表的可用性, 我们还在字段的上下文菜单中添加了新选项, 以便在井内上下移动字段或移动到其他井中。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B002.jpg)

Q &A 总是工作很好的键盘导航, 现在它也可以很好地与屏幕阅读器。此更新适用于 power bi desktop和 power bi 服务, 适用于所有 "q&a" 显示的位置, 包括Q&A资源管理器", 并使用Q&A在报表中创建视觉对象。这是用户在使用辅助技术时快速轻松地创建视觉对象的好方法, 它将真正为每个人打开报表创建。

* [ArcGIS Map性能提升](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#esri)

对于 Power BI 的 ArcGIS map 的最新更新, 所有地图的加载速度将加快50%。交叉高亮显示、过滤、平移和缩放也有重大性能改进。由于这些性能改进, 地图还可以支持在地图上绘制更多位置。对于纬度/经度点位置, 每个地图现在支持3万点。对于标准边界 (例如邮政编码、省份等), 地图现在可以绘制多达1.5万个区域。[在 Esri 博客文章中阅读有关这些更新的详细信息](https://www.esri.com/arcgis-blog/products/maps-power-bi/analytics/massive-performance-improvements-just-arrived-in-arcgis-maps-for-power-bi/)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B003.gif)

# [模型](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#modeling)

* [DAX 编辑器提升](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#daxEditor)

我们增强了 DAX 编辑器, 使其更强大!新编辑器具有新的键盘快捷键、行号和缩进线。该体验将非常类似于您对其他 Microsoft 编辑器 (如 VS 代码) 所拥有的内容。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B004.jpg)

一些快捷方式, 您可能会发现有用:

 

| **Alt+ ↑ / ↓** | **Move line up/down** |
| ---- | ---- |
| Shift+Alt + ↓ / ↑	| Copy line up/down |
| Ctrl+Enter	| Insert line below |
| Ctrl+Shift+Enter	| Insert line above |
| Ctrl+Shift+\	| Jump to matching bracket |
| Ctrl+] / [	| Indent/outdent line |
| Alt+Click	| Insert cursor |
| Ctrl+I	| Select current line |
| Ctrl+Shift+L	| Select all occurrences of current selection |
| Ctrl+F2	| Select all occurrences of current word |
 


# [分析](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#analytics)

* [Power BI 服务中的复合模型和聚合支持 (预览版)](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#compositeModels)

我们的复合模型和聚合预览本月有一个巨大的更新!现在, 您可以将使用复合模型或聚合的文件发布到 Power BI 服务, 并且它们将按预期方式工作。这将打开您开始测试复合模型和聚合端到端。此外, 还通过其他几种方式更新了复合模型。"空白查询" 体验根据 community.powerbi.com 论坛用户的反馈进行了大修。当然, 我们还在继续强化功能, 提高其可靠性。基于所有这些变化, 我们正变得非常接近的点, 我们可以使复合模型一般可用, 所以如果你有任何更多的反馈, 请告诉我们!

* [Explain the increase for non-additive measures](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#Insights)

我们的 "解释增加" 和 "解释减少" 的见解问题现在可用于所有度量类型, 而不仅仅是求和和计数!它的工作方式与它的总和和计数度量值相同, 因此从视觉上, 只需右键单击某个点, 然后选择 "分析" 解释增加。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B005.jpg)

您返回的视觉对象将取决于您使用的度量类型。您将继续获得瀑布图, 显示附加措施 (总和和计数) 的细分。对于平均值或比率的度量值, 您将看到一个点图解视觉对象, 对于其他所有内容, 您将看到一个聚集的柱形图。无论发生什么, 他们都将准备回答你问的问题: 为什么这项措施的价值增加或减少。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B006.jpg)

为平均值和比率获取的点图解显示了为选定的两个期间绘制的度量值。周期将在 x 轴上, 并在 y 轴上测量。气泡的大小反映度量值的权重。

 

# [自定义视图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#customVisuals)
* [Mapbox 更新 - 填充地图3D 拉伸 & more](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#mapbox)

通过其自定义视觉对象的最新版本, 您可以使用3D 拉伸将额外的尺寸添加到填充贴图中。除了动态填充颜色外, 您现在还可以向多边形添加数据驱动的高度。您所要做的就是将度量值放入大小存储桶中, 并设置相对挤压高度。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B007.gif)

为了与3D 型材一起使用, 他们添加了一个选项来设置默认贴图间距, 通常需要为了在多边形高度上获取最多的上下文。Mapbox 还提供了一些他们的首要要求:

* 变焦到选定的形状-现在, 每当您筛选填充贴图时, 地图将变焦到所选内容。

* 关闭地图控件的功能-您还可以在地图上添加更多的房地产, 方法是关闭地图控件以进行缩放和选择, 如果您不需要使用它们。

* 更智能的工具提示-工具提示现在将自动显示基础维度的格式, 而工具提示现在足够智能, 仅显示是否指定了某些内容。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B008.gif)

最后, 您现在可以将搜索栏添加到地图中。这是非常有用的, 如果您有大量的数据在许多位置, 允许您快速跳转到地图的任何部分。所有您需要做的是开始键入一个位置, Mapbox 将自动填充建议的位置为您。您甚至可以选择在该位置放置 。

* [Various bar & column chart visuals by Akvelon](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#akvelon)

Akvelon 最近发布了一组新的条形图和柱形图表自定义视觉对象。它们与我们的内置条形图和柱形类似, 具有支持矩形套索选择的附加功能。您可以单击并拖动以选择矩形区域内的多个条形图, 然后根据所选内容交叉筛选报表的其余部分。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B009.jpg)

它们有6个版本

· [Stacked Bar Chart by Akvelon](https://appsource.microsoft.com/en-us/product/office/WA104381824?src=office&corrid=7d6df104-b39e-42eb-8fd0-ef0a0103a781&omexanonuid=63e58fc3-993e-4fa9-a0e6-efbfca09cc0a)

 

· [Stacked Column Chart by Akvelon](https://appsource.microsoft.com/en-us/product/office/WA104381825?src=office&corrid=5c6ea09b-4d77-4bd8-b3c3-7911e14d61d0&omexanonuid=63e58fc3-993e-4fa9-a0e6-efbfca09cc0a)

 

· [Clustered Bar Chart by Akvelon](https://appsource.microsoft.com/en-us/product/office/WA104381822?src=office&corrid=d19015b5-0f71-4b32-9322-54b2a039d14f&omexanonuid=63e58fc3-993e-4fa9-a0e6-efbfca09cc0a)

 

· [Clustered Column Chart by Akvelon](https://appsource.microsoft.com/en-us/product/office/WA104381823?src=office&corrid=75b18dd7-61cd-494c-a41b-29f6cc3db65c&omexanonuid=63e58fc3-993e-4fa9-a0e6-efbfca09cc0a)

 

· [100% Stacked Bar Chart by Akvelon](https://appsource.microsoft.com/en-us/product/power-bi-visuals/WA104381805?src=office&tab=Overview)

 

· [100% Stacked Column Chart by Akvelon](https://appsource.microsoft.com/en-us/product/office/WA104381818?src=office&corrid=b5deb0ef-fb01-4270-8169-f7e3864019d7&omexanonuid=63e58fc3-993e-4fa9-a0e6-efbfca09cc0a)

 

* [3AG Systems – 带小倍数柱状图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#smallMultiples)

通过3AG 系统的小倍数自定义可视化柱形图, 您可以为组中的每个元素创建多个重叠的列图。它比较两种方案, 如实际 vs. 预测, 并显示重叠的柱形图。从那里, 它将打破这一类别的每个值, 你选择和可视化的图表彼此相邻。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B010.jpg)

虽然可视化功能可用于显示不同类别 (例如部门、区域、产品等) 的实际、预测、计划和往年数据, 但如果您仅具有实际值, 也可以使用小倍数。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B011.jpg)

* [3AG Systems –带绝对方差的条状图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#barVariance)

带有绝对方差自定义视觉对象的条形图由3AG 系统自动计算绝对方差, 并显示带有方差的重叠条形图。可视化计算两种方案之间的绝对方差, 并生成一个重叠条形图, 该图表显示与图表平行的方差条形图的两种方案。可视化是为了比较实际的、预测的、计划的和上一年的数据, 并且最适合于 y 轴上的分类数据。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B012.jpg)

* [3AG Systems –带相对方差的柱状图](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#columnVariance)

具有相对方差自定义视觉对象的柱形图由3AG 系统计算百分比变化, 并显示带棒糖方差的重叠柱形图。它计算两种方案之间的相对或百分比方差, 并生成一个重叠柱形图, 该图表显示与图表平行的棒糖图表的相对方差。可视化是为了比较实际、预测、计划和上一年的数据, 在 x 轴上使用时序变量时效果最佳。该视觉对象有很多格式选项, 包括反转红色和绿色的颜色、调整数据标签字号、隐藏数据标签和调整单位 (到千 K、百万米、亿字节)。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B013.jpg)

 

 

# [数据连接](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dataConnectivity)

* [Web By Example connector正式可用](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#webByExample)

* [SAP BW Connector implementation v2 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#sapBW)

* [SAP BW Message Server Connector 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#sapBWMessageServer)

* [Vertica connector 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#vertica)

* [Dynamics NAV and Dynamics 365 Business Central connectors 正式发布](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dynamics)

* [New Dynamics 365 Business Central On-premises connector](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dynamicsOnPrem)

 

# [数据准备](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dataPrep)

* [查询编辑器中的数据分析 (预览)](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#dataProfiling)

Power 查询编辑器为您提供了数以百计的数据转换, 用于转换、筛选和准备数据以进行分析。但是, 识别质量问题, 如错误、空值和异常点可能是相当困难的。通过本月的 power BI 桌面版本, 我们正在将数据分析功能添加到 power 查询编辑器中, 以便在数据预览中轻松识别错误和空值。可以从 "文件 >> 选项" 对话框的 "预览功能" 选项卡启用数据分析。启用该功能后, 您应该能够看到列标题下方的质量栏, 指示是否找到任何错误值。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B014.jpg)

请注意, 您还可以通过在 "视图" 选项卡下打开 "列质量" 选项来启用进一步的数据分析信息。这允许您查看错误、有效或空值的计数。此外, 您可以直接从 "移除" 菜单中执行操作以删除错误。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B015.jpg)

在此版本中添加的另一个数据分析功能是 "列分布" (也可以从 "视图" 选项卡启用)。通过列分布, 您可以了解数据预览中某列内值的总体分布情况, 包括不同值的计数 (给定列中找到的不同值的总数) 和唯一值 (总值数只在给定列中出现一次)。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B016.jpg)

您还可以直接从该视图执行操作, 以便删除重复项。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B017.jpg)

我们非常高兴在 Power 查询编辑器中发布此新的数据分析功能。我们在这个领域有许多新的功能计划, 包括查看更详细的价值分布信息的能力, 以及能够对特定值应用过滤器 (相当于当前的单元级上下文菜单过滤器)可用)。

[合并查询的模糊匹配选项 (预览)](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#fuzzyMatching)

通过合并查询, 您可以轻松地将多个表中的数据合并到 Power 查询编辑器中。在本月的发布中, 除了现有的 "完全匹配" 选项之外, 我们还添加了一个选项, 用于比较列中的值以匹配使用模糊匹配逻辑。可以从 "选项" 对话框的 "预览要素" 列表中启用模糊合并。完成此操作后, 您将能够从 "合并查询" 对话框中访问新的模糊匹配选项。选择模糊匹配选项后, 您还可以 (可选) 进一步调整模糊匹配设置。这包括配置相似性阈值, 是否忽略大小写/空格, 指定每个值的最大匹配量, 甚至指定自定义转换表, 以便不同的值可以视为等效 (即使它们的相似性分数低)。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B018.jpg)

这将允许非精确匹配作为合并的一部分执行, 如以下示例中所示 (匹配 "will" 具有多个变体:Bill, bill, Will, will等)

 

# [其他](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#other)

* [控制报表的导出数据选项](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#exportControl)

现在, 您可以灵活地控制将报表发布到 Power BI 服务时, 您的用户可以使用哪些类型的数据导出选项。您可以选择:允许仅导出汇总数据 (这将是报告的新默认值)允许导出汇总和基础数据 (这是所有旧报表的默认值)不允许导出任何数据您可以通过 "报告设置" 下的 "选项" 对话框在 Power BI 桌面中设置此功能。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B019.jpg)

还可以通过 "报表设置" 窗格在 Power BI 服务中更新此设置。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Power%20BI%20Desktop%2010%E6%9C%88%E6%9B%B4%E6%96%B020.jpg)

* [传输层安全设置](https://powerbi.microsoft.com/zh-cn/blog/power-bi-desktop-october-2018-feature-summary/#tls)

安全性是 Microsoft 的一个优先事项, 我们有公司范围内的程序, 以确保客户能够控制与 Microsoft 服务的通信安全。IT 和网络安全管理员可能希望强制使用最新版本的 TLS (传输层安全性), 以便在其网络上进行任何安全通信, Power BI 桌面现在将尊重用于管理此问题的 Windows 注册表项，例如, 您可以通过在 Windows 注册表中设置以下内容来禁用客户端应用程序使用旧的 TLS 1.0:

* [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client] "Enabled"=dword:00000000

* [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client] "DisabledByDefault"=dword:00000001

Power BI 指定的注册表项, 并且仅使用正确的 TLS 版本创建连接。此处提供了有关 Windows TLS 文档站点的更多信息:

https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/manage-ssl-protocols-in-ad-fs

https://docs.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings

 

# 即将发布

本月, 我想将 "即将到来" 部分集中在视觉相关功能上, 这是我们视觉对象中颜色饱和度特性的一个巨大更新。现在很长一段时间, 我们有两种不同的方法来动态地根据视觉类型对视觉对象的数据点进行颜色着色。我们的笛卡尔图表在字段中有一个颜色饱和度选项, 为您提供基本控件, 表和矩阵视觉对象具有条件格式。在过去一年中, 我们为表和矩阵的条件格式体验添加了大量功能, 但笛卡尔图表的颜色饱和度特征还没有得到太多的爱。这很快就会发生变化, 因为我们正在积极地使用颜色饱和度的所有视觉对象进行升级, 这将切换它们, 还可以使用已用于表和矩阵的条件格式体验。完成该功能后, 您将能够对所有视觉类型使用相同的对话框和相同的选项 (包括规则部分)。这也意味着, 随着我们继续改进条件格式, 所有视觉对象都将受益!
