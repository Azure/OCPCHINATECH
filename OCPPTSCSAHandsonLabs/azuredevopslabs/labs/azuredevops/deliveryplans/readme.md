---
title: Managing project schedules across teams with Delivery Plans 
layout: page
sidebar: vsts
permalink: /labs/azuredevops/deliveryplans/
folder: /labs/azuredevops/deliveryplans/
version: Lab version - 1.37.1
updated: Last updated - 9/9/2019
---
<div class="rw-ui-container"></div>
<a name="Overview"></a>

## Overview ##

It takes several teams to develop large software projects. Very large projects require multiple autonomous teams that can manage their own backlog and priority while contributing to a unified direction for that project. Regular reviews of the project schedule with these teams help ensure that the teams are working toward common goals. Delivery Plans provide the needed multi-team view of your project schedule.


<div class="bg-slap"><img src="./images/mslearn.png" class="img-icon-cloud" alt="MS teams" style="
    width: 48px; height: 48px;">Want additional learning? Check out the <a href="https://docs.microsoft.com/en-us/learn/modules/manage-delivery-plans/" target="_blank"><b><u> Manage Agile software delivery plans across teams </u></b></a> module on Microsoft Learn.</div>

<a name="Prerequisites"></a>
### Prerequisites ###

- This lab requires you to complete task 1 from the <a href="../prereq/">prerequisite</a> instructions

<a name="Exercise1"></a>
## Exercise 1: Managing Delivery Plans with Azure DevOps ##

<a name="Ex1Task1"></a>
### Task 1: Installing the Delivery Plans extension ###

1. Navigate to your team project on Azure DevOps.

1. Delivery Plans is provided as a marketplace extension. From the **Marketplace** navigation dropdown, select **Browse Marketplace**.

    ![](images/000.png)

1. Search for **"Delivery Plans"**.

    ![](images/001.png)

1. Select the **Delivery Plans** option.

    ![](images/002.png)

1. Click **Get it free**.

    ![](images/003.png)

1. Select the organization to install **Delivery Plans** into. This should be the organization that contains your Parts Unlimited project. Click **Install**.

    ![](images/004.png)

1. Click **Proceed to organization**.

    ![](images/005.png)

1. Click the Parts Unlimited project link to return to its dashboard.

    ![](images/006.png)

<a name="Ex1Task2"></a>
### Task 2: Creating a delivery plan ###

1. From the **Boards** dropdown, select **Plans**.

    ![](images/007.png)

1. Click **New plan**.

    ![](images/008.png)

1. Since you may want to have multiple delivery plans for different aspects of your project, provide the specific name **"Web delivery"**. It should default to the **Parts Unlimited Team**, so select **Features** and click **Create**. Note that you could also organize your deliveries by **Stories** if you used that model instead. There is also the option to add additional teams and criteria to filter stories/features by, but we'll revisit those later.

    ![](images/009.png)

1. Due to the iteration reconfiguration performed earlier, the "Today" marker is right at the beginning of **Sprint 2**. We have a number of stories listed for delivery in the previous sprint, and we can also see an empty **Sprint 3**. Note that some of the stories shown are **Done**. Although it's useful to see the progress of work, we'll use that as an example by which to filter items out in a moment.

    ![](images/010.png)

1. Click the **Configure plan settings** button.

    ![](images/011.png)

1. Select the **Field criteria** tab and click **Add criteria**.

    ![](images/012.png)

1. Set the new criteria to filter down to items where **State** does not equal (**<>**) **Done**.

    ![](images/013.png)

1. We can also add a custom marker to keep track of significant dates. Select the **Markers** tab and click **Add marker**.

    ![](images/014.png)

1. Select the fourth Friday from today (it will be the Friday in the middle of **Sprint 3**) and set the **Label** to **"Team offsite"**. Select magenta as the **Color** and click **Save**.

    ![](images/015.png)

1. The first thing to notice is that the "Closed" story is no longer visible on the delivery plan due to the criteria set in the configuration. In addition, there is now a magenta marker in the middle of **Iteration 3** that says **"Team offsite"** when clicked.

    ![](images/016.png)

1. Another neat feature of the delivery plan extension is the ability to easily scale the calendar. Drag the **Scale** slider all the way to the left to view multiple months at once.

    ![](images/017.png)

1. Slide it all the way to the right to zoom in to a much more precise view.

    ![](images/018.png)

<a name="Ex1Task3"></a>
### Task 3: Adding an external team to the project ###

1. Our delivery plan has been pretty simple so far because we only have the one team. However, the real power of delivery planning comes into play when orchestrating multiple autonomous teams across their efforts. Open the settings page using the **Project Settings** navigation located at the bottom left of the page.

    ![](images/019.png)

1. From the **Teams** tab, click **New team**.

    ![](images/020.png)

1. This new team will be responsible for the efforts that involve integrating with external services, such as 3rd party services for things like weather forecasts and payment processing. Set the **Team name** to **"External integration team"** and click **Create team**.

    ![](images/021.png)

1. Select the **Project configuration** tab under **Boards**.

    ![](images/022.png)

1. Note the dates of **Sprint 2** and **Sprint 3**, which will vary for your account based on when you generated the project data. We're going to add two new iterations for the external services team that do not align exactly with the main team's schedule.

    ![](images/023.png)

1. With the root **PartsUnlimited** node select, click **New child**.

    ![](images/024.png)

1. Set the **Iteration name** to **"Iteration 50"**. Use today as the **Start date** and set the **End date** to three Fridays from today. This will also happen to be the day of the team offsite. Click **Save and close**.

    ![](images/025.png)

1. Use the same process to add an **Iteration 51** that starts the Monday after **Iteration 50** ends and has an end date three Fridays later.

    ![](images/026.png)

1. Now we need to configure the new team to use those new project sprints as its iterations. Select the **Teams** tab and click **External integration team**.

    ![](images/027.png)

1. Click **Iterations and areas**.

    ![](images/028.png)

1. Select the **Iterations** tab.

    ![](images/029.png)

1. Click **Select iterations** and use the **+ Iteration** button to select **Iteration 50** and **Iteration 51**. Click **Save and close**.

    ![](images/030.png)

<a name="Ex1Task4"></a>
### Task 4: Making delivery decisions ###

1. From the **Boards** dropdown, select **Plans**.

    ![](images/031.png)

1. Click the **Configure plan settings** button.

    ![](images/032.png)

1. Select the **Teams** tab and click **Add team**.

    ![](images/033.png)

1. Select the **External integration team** and **Features**. Click **Save**.

    ![](images/034.png)

1. Use the **Scale** slider to fit the width of **Iteration 50** and **Iteration 51**.

    ![](images/035.png)

1. The new team doesn't have any stories added yet. Fortunately, you can add them directly to their team and iteration using the inline functionality. Select the **Iteration 50** iteration. Click the **New item** button that appears.

    ![](images/036.png)

1. Enter **"Integrate with weather service"** and press **Enter**. That item is now in the backlog with its area and iteration configured.

    ![](images/037.png)

1. Follow the same process to add an item for integrating with corporate branding assets to **Iteration 51**.

    ![](images/038.png)

1. Now we can step back to see how these two teams are working toward our common goals. Upon closer examination, it appears that the main team is planning to reuse some corporate branding assets during the current sprint that will not be available until well after it's over. It's a good thing we have this view to catch these sort of potential problems early on.

    ![](images/039.png)

1. The first thing we should do is to move the branding integration work to an earlier iteration. Drag and drop the corporate branding story onto **Iteration 50**. In order to free up the bandwidth, drag the weather service story onto **Iteration 51**.

    ![](images/040.png)

1. Next, drag the branding work item from **Sprint 1** to **Sprint 3** so that there's a chance the dependencies will be available in time for this team to be unblocked.

    ![](images/041.png)

1. Now we can review the delivery plan again. It should be more feasible now.

    ![](images/042.png)

1. There are a lot of ways to quickly customize the view of the delivery plan. For example, pressing the **'t'** key will toggle between showing all configured fields and showing just the title. Try that now.

    ![](images/043.png)

1. You can also collapse all teams (or specific teams) using the toggle buttons next to their names.

    ![](images/044.png)

## Reference

Thanks to **Nagaraj Bhairaji** for making a video on this lab. You can watch the following video that walks you through all the steps explained in this lab

<figure class="video_container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/WlWVJyxY-l8" frameborder="0" allowfullscreen="true"> </iframe>
</figure>