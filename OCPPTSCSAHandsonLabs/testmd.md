＃使用Azure工件进行程序包管理

>在https://aka.ms/devopslabs上查看教程“使用Azure Artifacts进行程序包管理”以及更多内容。

[Home]（https://azuredevopslabs.com//default.html）/使用Azure Artifacts进行程序包管理

** Azure Artifacts **是一个扩展，可轻松发现，安装和发布Azure DevOps中的NuGet，npm和Maven程序包。它与Build等其他枢纽进行了深度集成，因此程序包管理可以成为您现有工作流程的无缝组成部分。

* Visual Studio 2017或更高版本
    
*本练习要求您按照[前提条件]（chrome-extension：// cjedbglnccaioiolemnfhjncicchinao / prereq /）的说明完成任务1和2。
    

** Azure Artifacts **是Azure DevOps Services和Azure DevOps Server的扩展。它已预安装在Azure DevOps Services，Azure DevOps Server 2019，Team Foundation Server（TFS）2017和2018中。

###任务1：创建并连接到Feed

1.导航到“工件”中心。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/000.png）
    
2.点击**创建供稿**。该供稿将是可供组织内的用户使用的NuGet软件包的集合，并且将与公共NuGet供稿一起作为对等源。本实验中的场景将重点放在使用Azure Artifacts的工作流上，因此实际的体系结构和开发决策仅是说明性的。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/createfeed.png）
    
3.该提要将包含可以在该组织中的各个项目之间共享的通用功能。选择此实验室的范围作为“组织”。将名称设置为**“淧artsUnlimitedShared” *，然后单击“创建”。保留默认选项。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/create-feed-window2.png）
    
4.任何想要连接到此NuGet feed的用户都必须配置其环境。点击**连接到Feed **。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/003.png）
    
5.在“连接到提要”窗口中，选择“ Visual Studio”并复制“源” URL。这是Visual Studio和NuGet唯一需要开始利用新的提要的东西。在浏览器中将对话框保持打开状态。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/connect-feed.png）
    
6.启动** Visual Studio **的**新**实例。请勿使用通过克隆主要的“ Parts Unlimited”解决方案而打开的实例。
    
7.选择**工具| NuGet软件包管理器|软件包管理器设置**。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/packagemanagersettings.png）
    
8.找到“软件包来源”部分，然后单击“添加”按钮以添加新的软件包来源。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/005.png）
    
9.将“名称”设置为“ artsUnlimitedShared”，然后粘贴之前复制的“源” URL。单击“更新”，然后单击“确定”。现在，Visual Studio已连接到新的提要。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/006.png）
    
10.关闭并重新打开用于克隆PartsUnlimited存储库的另一个Visual Studio实例（[前提条件]（chrome-extension：// cjedbglnccaioiolemnfhjncicchinao / prereq /）任务2），以便它显示此新源。
    

###任务2：创建和发布NuGet包

1.从** Visual Studio **的主菜单中，选择**文件|新增|项目**（VS2019中的“创建一个新项目”）。现在，我们将创建一个共享程序集，该程序集将以NuGet程序包的形式发布，以便其他团队可以集成该程序集并保持最新状态，而不必直接与项目源代码合作。
    
2.从“ Visual C＃”部分中，选择“类库（.NET Framework）”模板，然后将“名称”设置为“ artsUnlimited.Shared”。单击“确定”以创建项目。 （如果使用VS2019，请在查找器中查找“ lass”，然后选择“类库（.NET Framework）”并选择版本4.5.1）
    
    ** VS2017 **
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/007.png）
    
    ** VS2019 **
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/create-project-vs2019.png）！[]（chrome-extension：// cjedbglnccaioiolemnfhjncicchinao / labs / azuredevops / packagemanagement / image project-vs2019.png）
    
3.在“解决方案资源管理器”中，删除“ Class1.cs **”。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/008.png）
    
4.右键单击项目节点，然后选择“属性”。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/009.png）
    
5.将“目标框架”设置为“ .NET Framework 4.5.1”，然后单击“是”以确认更改。 （如果使用VS2019，请确认相同）
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/010.png）
    
6.按Ctrl + Shift + B生成项目。在下一个任务中，我们将使用** NuGet.exe **直接从已构建的项目中生成NuGet包，但是它要求首先构建该项目。
    
7.返回到Azure DevOps浏览器选项卡。在之前创建的供稿上，单击“连接到供稿” ** | ** NuGet.exe ** | **获取工具**。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/getthetools.png）
    
8.单击**下载最新的Nuget **。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/downloadthenuget.png）
    
9.在打开的窗口中，选择nuget.exe版本** v5.5.1 **
    
10.返回** Visual Studio **。在“解决方案资源管理器”中，右键单击“ PartsUnlimited.Shared”项目节点，然后选择“在文件资源管理器中打开文件夹”。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/013.png）
    
11.将下载的** nuget.exe **文件移到包含**。csproj **文件的文件夹中。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/014.png）
    
12.在同一“ Windows资源管理器”窗口中，选择“文件|文件”。打开Windows PowerShell |以管理员身份打开Windows PowerShell **。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/015.png）
    
13.执行以下行，从项目中创建一个**。nupkg **文件。请注意，这是将NuGet位打包在一起以进行部署的快捷方式。 NuGet是非常可定制的，并为为消费者提供详细信息提供了极大的灵活性。您可以在[NuGet程序包创建页面]上了解更多信息（https://docs.microsoft.com/zh-cn/nuget/create-packages/overview-and-workflowhttps:/docs.microsoft.com/zh-cn / nuget / create-packages / overview-and-workflow）。
    
         ./nuget.exe包./PartsUnlimited.Shared.csproj
        
    
14. NuGet根据能够从项目中提取的信息构建一个最小的程序包。例如，请注意名称为** PartsUnlimited.Shared.1.0.0.nupkg **。该版本号是从程序集中提取的。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/016.png）
    
15.返回** Visual Studio **。在** Solution Explorer **中，打开** Properties \\ AssemblyInfo.cs **。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/017.png）
    
16. ** AssemblyVersion **属性指定要构建到程序集中的版本号。每个NuGet发行版都需要一个唯一的版本号，因此，如果我们继续使用此方法来创建软件包，则需要记住在构建之前将其递增。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/018.png）
    
17.返回** PowerShell **窗口并执行以下命令（它应该在一行上）。请注意，您需要提供“ PI密钥”？可以是任何非空字符串。我们在这里使用**“ STS” *。询问时使用您的Azure DevOps凭据登录。
    
         ./nuget.exe push -source“ PartsUnlimitedShared” -ApiKey VSTS PartsUnlimited.Shared.1.0.0.nupkg
        
    
18.该命令应在几秒钟后成功执行。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/019.png）
    
19.返回浏览器窗口，打开对Azure DevOps并“刷新”窗口。现在您应该看到该组织的NuGet包已在Feed中发布。单击它以查看详细信息。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/020.png）
    
20.详细信息已导入，现在可供其他人使用。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/021.png）
    

1.切换到具有完整** Parts Unlimited **解决方案的** Visual Studio **实例。
    
2.在“解决方案资源管理器”中，右键单击“ PartsUnlimitedWebsite”项目下的“ References”节点，然后选择“ Manage NuGet Packages”。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/022.png）
    
3.单击“浏览”选项卡，然后将“包来源”更改为“ PartsUnlimitedShared **”。唯一的软件包将是我们刚刚添加的软件包，因此请单击“安装”以将其添加到项目中。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/023.png）
    
4.如果询问，请单击“确定”确认添加。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/024.png）
    
5.按Ctrl + Shift + B生成项目。它应该成功。 NuGet包还没有添加任何值，但是至少我们在那里知道。
    

1.切换到已打开** PartsUnlimited.Shared **项目的** Visual Studio **实例（NuGet源项目）。
    
2.在“解决方案资源管理器”中，右键单击“ PartsUnlimited.Shared”项目节点，然后选择“添加”。新物品**。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/025.png）
    
3.选择“类别”模板，然后输入“名称”“ axService.cs” *。点击**添加**以添加课程。我们可以假装将税收计算合并到此共享的类中并进行集中管理，以便其他团队可以简单地使用NuGet程序包。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/026.png）
    
4.用下面的代码替换新文件中的代码。目前，它将仅硬编码10％的费率。
    
         命名空间PartsUnlimited.Shared
         {
             公共类TaxService
             {
                 静态公共十进制CalculateTax（十进制应纳税，字符串postalCode）
                 {
                     应纳税所得额*（十进制）.1;
                 }
             }
         }
        
    
5.由于我们正在更新程序集（和程序包），因此请返回** AssemblyInfo.cs **并将** AssemblyVersion **更新为** 1.1.0.0 **。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/027.png）
    
6.按Ctrl + Shift + B生成项目。
    
7.返回** PowerShell **窗口并执行以下行以重新打包NuGet程序包。请注意，新软件包将具有更新的版本号。
    
         ./nuget.exe包PartsUnlimited.Shared.csproj
        
    
8.执行以下行以发布更新的软件包。请注意，版本号已更改以反映新的软件包。
    
         ./nuget.exe推送-source“ PartsUnlimitedShared” -ApiKey VSTS PartsUnlimited.Shared.1.1.0.nupkg
        
    
9.返回浏览器窗口，打开对Azure DevOps的页面并刷新页面。您仍将查看该软件包的1.0.0版本，但是可以通过选择“版本”标签并选择“ 1.1.0 **”来更改该版本。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/028.png）
    
10.切换回打开主** PartsUnlimited **项目（带有** PartsUnlimitedWebsite **）的** Visual Studio **实例。
    
11.在“解决方案资源管理器”中，打开“ PartsUnlimitedWebsite \\ Utils \\ DefaultShippingTaxCalculator.cs **”。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/029.png）
    
12.在** 20 **行附近找到对** CalculateTax **的调用，并在开头添加限定符**“。artsUnlimited.Shared.TaxService。” *。原始代码称为此类的内部方法，因此我们添加到该行开头的代码将其重定向到NuGet程序集中的代码。但是，由于该项目尚未更新NuGet程序包，因此它仍引用1.0.0.0，并且没有可用的这些新更改，因此将无法构建代码。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/030.png）
    
13.在“解决方案资源管理器”中，右键单击“参考”节点，然后选择“管理NuGet软件包”。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/031.png）
    
14. NuGet知道我们的更新，因此请单击“更新”选项卡以查看详细信息。单击“更新”以放下新版本。如果“更新”选项卡尚未更新，则仍可以从“浏览”选项卡更新软件包。请注意，可能有许多可用的NuGet更新，但是您只需要更新** PartsUnlimited.Shared **。请注意，该软件包可能需要一些时间才能完全可用于更新。如果出现错误，请稍等片刻，然后重试。
    
    ！[]（chrome-extension：//cjedbglnccaioiolemnfhjncicchinao/labs/azuredevops/packagemanagement/images/032.png）
    
15.如果询问，请单击“确定”以批准更新。
    
16.按** F5 **生成并运行该站点。它应该按预期工作。


[来源]（https://www.azuredevopslabs.com/labs/azuredevops/packagemanagement/）