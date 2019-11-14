一、 注册Global Azure试用账户

1. 用浏览器打开“隐私浏览模式”，这样会避免一些缓存账户信息的问题，打开azure.com点击右上角“免费账户”，在之前先注册个liveid，此操作以marsworkshop@outlook.com为例，仅为操作说明时候用。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C01.png)

2. 点击免费开始

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C02.png)

3. 登录live id，marsworkshop@outlook.com，按照如下填写信息

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C03.png)

4. 短信进行验证

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C04.png)

5. 验证信用卡

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C05.png)

6. 持卡人姓名：WANG SONG，两个名字之间有空格，验证通过，勾选同意，点击注册即可。注册成功后，信用卡会扣1刀费用，之后会返还，部分信用卡有两笔费用，1刀+10 CNY，这个跟信用卡银行有关系，我使用的是招行visa，扣了两笔。

点击转到门户即可使用

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C06.png)

7. 登录进来，点击左上角创建资源

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C07.png)

8. 为了保证费用不超支：请参考如下：https://docs.microsoft.com/zh-cn/azure/billing/billing-avoid-charges-free-account，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C08.png)

 

二、 创建DSVM操作说明：

1. 点击计算，点击查看全部，

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C09.png)

2. 在搜索中输入：“DSVM”，选中如下红色圈出部分，进行VM创建。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C10.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C11.png)

3. 按照提示进行信息输入，区域选择东南亚（新加坡），东亚（香港）都可以，资源组的概念是逻辑的概念，资源的集合的概念，随便起个唯一的名字就行。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C12.png)

4. 选择机型，这一块2c，16g及其以上的都可以，因为有200刀的免费额度，注意账单。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C13.png)

5. 配置可选功能，因为只做hands on 的测试，所以不用做操作，点击确定即可。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C14.png)

6. 点击创建，等待机器创建好。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C15.png)

7. 因为是预装了很多Data Service的软件，所以创建的时间比linux VM的时间会长，20多分钟，然后看到显示部署成功，点击转到资源
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C16.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C17.png)

8. 打开windows远程桌面连接登录，输入公网IP和用户名密码登录

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C18.png)

9. 登录进去显示如下即可。如果登录不成功，删除资源组，请重新按照以上步骤进行VM创建，有客户遇到过Oracle Security patch登录不成功的问题。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C19.png)



三、 创建Data Lake

1. 创建Data Lake，一样的步骤

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C20.png)

2. 在如下区域创建选择，例如美东2，pay-as-you-go,资源组名称类似。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C21.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C22.png)

3. 创建成功如下。
 
 ![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Global%20Azure%E8%AF%95%E7%94%A8%E8%B4%A6%E5%8F%B7%E6%B3%A8%E5%86%8C%E6%93%8D%E4%BD%9C%E5%92%8CDSVM%E5%88%9B%E5%BB%BA%E6%89%8B%E5%86%8C23.png)
 
