---
title: Azure DevOps实验
layout: homepage
sidebar: vsts
permalink: /OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/
folder: /OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/
description: 提供Level 200-300的动手实验，赋能技术人员及客户使用Azure DevOps更好的实现敏捷业务
---


#  Azure DevOps动手实验
## 实验背景
**Parts Unlimited**是一家全国性的汽车零部件制造商和零售商（虚构），其营业额达40亿美元，组织财务状况不佳。他们需要要节省成本，而且要使其具有市场竞争力和获得盈利。于是计划一个对业务的未来至关重要的项目**Phoenix Project**（凤凰城项目），该项目代表了IT推动的业务转型，其中零售运营部是该项目的业务所有者。要求IT运营副总裁领导的IT部门确保“凤凰城项目”获得成功。刚晋升的IT运营副总裁，但很快就不知所措...

项目在初始执行时面临如下挑战：

**1.项目成本大大超出预算**  
**2.面临着大量积压的工作、未解决的问题和未实现的功能**  
**3.零售运营部不断提出新的想法和要求**

CEO要求IT部门必须在90天内解决问题，否则整个部门将被...

**您面临的挑战是使用DevOps原理及运用Azure DevOps 工具并将其应用到这一严肃的业务模拟中**

   ![](/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/images/PhoenixProject.PNG)  
   


 
</div>
</div>
</div>
<div class="tab-content bg-color-wit-mlr">
<div id="services-labs" class="container tab-pane active">

<div class="col-sm-12">
   <h2>动手实验章节</h2>
   <div class="row equal-height-columns">
      <div class="col-sm-4 col-xs-12">

   <div>
      <p>使用Azure DevOps服务简化并加快DevOps流程。 以下实验将帮助您使用Azure DevOps服务自动执行软件交付满足Parts Unlimited业务需求。</p>
   </div>
         <div class="bg-color-grey equal-height-column mar-left-40">
            <ul>
               <li><a href="/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/agile/" class="barleft">使用Azure Boards进行敏捷规划和项目组合管理 </a></li>
               <li><a href="/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/git/" class="barleft">在Visual Studio Code和Azure DevOps中使用Git进行版本控制  </a></li>
               <li><a href="/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/packagemanagement/" class="barleft">使用Azure Artifacts进行程序包管理</a></li>
               <li><a href="/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/continuousintegration/" class="barleft">使用Azure Pipelines实现持续集成</a></li>
               <li><a href="/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/yaml/" class="barleft">通过Azure Pipelines拥抱持续交付</a></li>
               <li><a href="/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/testmanagement/" class="barleft">使用Azure Test Plans进行测试计划和管理</a></li>
               <li><a href="/OCPPTSCSAHandsonLabs/azuredevopslabs/labs/azuredevops/exploratorytesting/" class="barleft">使用Azure Test Plans测试计划进行探索性测试</a></li>
     





   </div>
</div>

<div class="col-sm-10" style="padding-top:20px">
   <h2>初次使用Azure DevOps?</h2>
   <div style="margin-top:2px">
     还没有帐号？不用担心！立即
<a href="https://go.microsoft.com/fwlink/?LinkId=2014881" class="barleft">免费注册 </a>

 <ul class="tick">
         <li>可配置Kanban boards</li>
         <li>免费的无限私人Git存储库</li>
         <li>自动CI/CD流水线</li>
         <li>广泛的基于云的自动化负载测试工具。</li>
</div>


<div class="col-sm-12">
   <h2>动手实验开始前的准备工作</h2>
   为了完成这些实验，您需要：
   <ul>
      <li>
         <strong>Azure DevOps services Organization:</strong> 您需要有一个Azure DevOps services account. 如果没有，您可以从这里注册<a href="https://www.visualstudio.com/" target="_blank">here</a>
      </li>
      <li>
         <strong>Microsoft Azure Account</strong>: 您需要一个Azure账号. 如果没有, 
         <ul>
            <li>
               您可以创建一个<a href="https://azure.microsoft.com/en-us/free/" target="_blank">免费 Azure account</a> and enjoy 12 months of free Azure services
            </li>
            <li>
               如果您是Visual Studio Active Subscriber，则有权每月获得$ 50- $ 150的信用额。 你可以参考这个<a href="https://azure.microsoft.com/en-us/pricing/member-offers/msdn-benefits-details/" target="_blank">link</a> 了解更多信息，包括如何激活和开始使用您的每月Azure信用额。
            </li>
         </ul>
      </li>
      <li>
         <a href="https://azuredevopsdemogenerator.azurewebsites.net" target="_blank"><strong> Azure DevOps演示生成器：</strong> </a>您可以使用Azure DevOps演示生成器将包含预定义数据的项目置备到Azure DevOps服务组织中。
      </li>
   </ul>
</div>
