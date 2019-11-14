  话说这篇 Blog 应该是 Azure 账单分析系列，请原谅拖延症晚期患者，一直到现在才扫尾。
  在类似账单分析的场景，我们会定期收到新的原始数据文件，分析时需要汇总所有数据。

  如何汇总所有数据？最简单的方法是把所有文件合并成一个文件。但是这样通常需要调整格式（如删除多余的表头等），不方便操作。
  而 PBI 可以直接导入多个文件，进行分析。那么新文件加入时，是否可以直接发现新文件，自动合并数据？
## 本地多文件分析
  在 PBI Desktop 检出数据源，我们发现可以将文件夹作为数据源：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%201.png)
  现在将一个文件夹作为数据源连接至 PBI：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%202.jpg)
  因为文件夹里已经有了一个数据文件（file.xlsx），所以会直接显示：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%203.jpg)
  因为要将这个文件夹里所有的文件合并分析（包括未来新加入的文件），所以这里要选择“组合-合并和加载（或合并和编辑）”：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%204.jpg)
  这里做 demo 的原始文件意见做好数据整理，所以直接选择“合并和加载”将数据导入：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%205.jpg)
  这里会将第一个文件（或指定的某一个文件）的内容显示出来供确认；点击“确定”后进入 PBI 的分析页面，和文件数据源一样：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%206.jpg)
  根据其中数据做一个简单的饼图如下：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%207.jpg)
  现在将准备好的第二个文件（file02.xlsx）也放入该文件夹，文件内容如下：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%208.jpg)
  和第一个文件结构一致。
  现在 PBI Desktop 的界面点击“刷新”：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%209.jpg)
   file02 的数据已经被 PBI 抓取并进行了分析：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2010.jpg)
  可以看到，PBI Desktop 如果是将文件夹作为数据源，可以自动加载里边所有的文件做分析展现。如果有新的数据文件，放入该文件夹即可。
## 在线多文件分析
### PBI 报表发布
  通常我们会将 PBI 作为 Saas 服务，报表发布到网上供老板或同事查看。
  在 PBI Desktop 的界面有一个发布按钮，点击即可发布做好的报表：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2011.jpg)
  发布前首先要保存，即将 PBI 抓取的数据保存成为 PBI 格式（pbix）的文件：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2012.jpg)

  然后发布到 PBI 上预先创建好的一个工作区：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2013.jpg)
  发布完成：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2014.jpg)
  在 PBI 网页可以看到报表：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2015.jpg)
### 本地文件夹数据源
  将新文件 file03.xlsx 放入目标文件夹，然后在网页点击刷新，可以发现报表没有变化。
  其实发布报表，就是将 pbix 格式文件放入 PBI 网页的数据集里；所以刷新时网页上的 pbix 文件没有变化，当然展现的图标也不会变化。
  那么，如何能将本地文件夹的数据变化刷新到网上？在数据集的设置里可以看到，如果要实现这个功能，需要在本地安装一个个人网关并添加数据源，负责将本地数据的变化刷新到网上，这样才能更新报表：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2016.jpg)
  但这个方法有个缺陷，如果本地有任何故障，例如网关没正常运行，文件夹名字发生变化，电脑没开机等，都会影响数据刷新。
### 在线数据源
  解决这个缺陷的方法很简单，将数据放在网上，不依赖于本地电脑即可。
  在 PBI 网页版中，支持多种在线文件存储：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2017.jpg)
  但是这些数据源都只支持到文件，没法添加文件夹。
  不过在 PBI Desktop 里，可以将 Azure Blob 作为数据源，如果将 container 作为数据源，是否可以实现多文件自动导入分析？
  现在 Azure 创建好 Blob 存储及 container：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2018.jpg)
  将 file01 上传到 container：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2019.jpg)
  在 PBI Desktop，选择 Azure Blob 作为数据源：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2020.jpg)
  输入 Azure Blob 的账户名（Azure Global）或 URL（Azure China）：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2021.jpg)
  输入存储账户的 key：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2022.jpg)
  该存储账户下的container自动列出：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2023.png)
  container中的文件自动列出：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2024.png)
  此处我们并不是要导入Blob的信息，而是要导入其中文件的信息，所以不能直接加载，需要点击“编辑”，进入编辑界面：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2025.png)
  注意Content旁边的并列向下箭头：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2026.png)
  点击即可进入合并文件的界面，如同本地文件一样：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2027.png)
  点击“确定”，然后再编辑器界面即可看到文件内容：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2028.png)
  点击“关闭并应用”，导入数据，如同本地文件一样创建一个示范用饼图：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2029.png)
  然后发布到PBI 网页版（注意同一个工作区的名字不能相同）：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2030.png)
  可以在PBI网页看到报表：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2031.png)
  现将file02上传到同一个container：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2032.png)
  刷新仍然没变化
  检查新数据集（demoazure）的设置，发现数据源凭据无效：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2033.png)
  因为数据集上传时，不会带凭据，需要手工编辑。点击“编辑凭据”，输入存储账户的key，并登录：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2034.png)
  现在刷新数据集：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2035.png)
  回到报表界面刷新报表，即可看到新的数据：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2036.png)
  所以，通过Azure Blob，我们可以实现脱离本地电脑的PBI网页多文件查询分析，只需要将文件上传到固定的container即可。到这里唯一需要干预的是新文件上传后手工刷新数据集。
  其实，PBI已经提供了数据集自动刷新的功能，即按计划的刷新：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2037.png)
  可以根据实际情况安排每天的刷新时间，甚至一天多次刷新：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/天下大势%EF%BC%8C分久必合——PowerBI自动多文件分析%2038.png)
  这样，每天到了设置的时间，数据集自动刷新，如果有新文件加入或者旧文件修改删除，将自动导入最新的数据供分析。
