# 基于Azure IoT Hub的远程监控


### 实验一：在Azure中创建IoT Hub	
 1.	登陆Azure管理门户	
 2.	新建IoT Hub	
 3.	查看IoT Hub基本信息	

### 实验二：前端设备向IoT Hub发送消息	
 1.	设备注册	
 2.	创建模拟设备向IoT Hub发送消息	
 3.	通过DeviceExplorer查看发送到IoT Hub的消息

### 实验三：通过Azure Stream Analytics进行流数据处理	
 1.	新建Stream Analytics Job	
 2.	配置Stream Analytics Job输入	
 3.	配置Stream Analytics Job输出	
 4.	配置Stream Analytics Job查询

### 实验四：通过Power BI进行数据展现	
 1.	通过Power BI Desktop连接Azure Blob Storage	
 2.	通过 Power BI创建报表	


## 实验一：在Azure中创建IoT Hub
### 1.登陆Azure管理门户

在浏览器中输入 (https://www.azure.cn/) 打开Azure中国区官方网站，然后点击页面右上角的“Azure门户预览”：

![Banner](./Images/1.png)

### 2.新建IoT Hub

输入账户和密码，登陆到管理门户。点击左上角“+新建”按钮，然后依次选择“物联网”，“IoT Hub”，如下图所示：

![Banner](./Images/2.png)

为IoT Hub和新建资源组输入名称，将定价和缩放级别调整为”S1 – 标准”，然后勾选“固定到仪表板”选项，其它配置项保留默认值，然后点击“创建”。
 
### 3.查看IoT Hub基本信息
创建完成后在仪表板中点击刚刚创建好的IoT Hub，然后点击“共享访问策略”，选中iothubowner，然后在屏幕右侧的“连接字符串-主密钥”旁边点击复制按钮，如下图所示：

![Banner](./Images/4.png)
 

## 实验二：前端设备向IoT Hub发送消息
### 1.设备注册
- 运行CreateDeviceIdentity

打开Visual Studio，依次点击”文件-打开-文件夹”，找到下载的位置，打开[Azure_IoT_Hub/Code/CreateDeviceIdentity](./src/CreateDeviceIdentity)，并运行。
 
![Banner](./Images/5.png)
 
![Banner](./Images/8.png)

返回浏览器中，在IoT Hub的管理界面中依次点击“概述”，“设备”，可以看到刚刚注册过的名为“myFirstDevice”的设备，其状态为”enabled”：
 
![Banner](./Images/9.png)

点击”myFirstDevice”，并复制其主密钥，如下图所示：
 
![Banner](./Images/10.png)


### 2.创建模拟设备向IoT Hub发送消息

首先在Azure Portal上获取IoT Hub的主机名和设备的主密钥：

![Banner](./Images/2-2-1.png)

![Banner](./Images/10.png)

下载[IoTDempApp](./src/IoTDemoApp)并打开IoTDemoApp.sln, 替换/Code/IoTDemoApp/Program.cs 中的 {iot hub hostname} 及 {device key}

![Banner](./Images/2-2-2.png)

运行IoTDemoApp.sln，启动程序，可以看到模拟程序每秒向IoT Hub发送一组消息，消息中包含随机生成的风速、温度和湿度的数据，如下图所示：

![Banner](./Images/2-2-3.png)

在Azure管理界面中，可以看到IoT Hub已经接收到消息：

![Banner](./Images/2-2-4.png)

## 实验三：通过Azure Stream Analytics进行流数据处理
### 1.新建Stream Analytics Job
打开Azure管理门户，点击左上角的+号按钮，然后依次点击”Intelligence + Analytics”, “Stream Analytics Job”，如下图所示：

![Banner](./Images/3-1-1.png)

为流分析作业输入名称，并选择使用现有资源组，然后点击“创建”按钮，如下图所示：

<img width="300" height="700" src="./Images/3-1-2.png"/>

### 2.配置Stream Analytics Job输入
等待Stream Analytics Job创建好以后，点击“输入”。点击“添加”按钮，如图所示：

<img width="350" height="800" src="./Images/3-1-3.png"/>

然后输入如下信息，点击“保存”：

<img width="400" height="700" src="./Images/3-2-1.png"/>



### 3.配置Stream Analytics Job输出

接下来我们要为Stream Analytics Job创建输出。此次动手实验中我们将数据输出到Azure Blob Storage中，因此先要配置一个Azure Blob Storage的存储账号。
在Azure门户中，点击左上角的“新建”按钮，然后依次点击“存储”，“存储账户”。
选择刚刚创建的资源组，输入一个存储账户名称，并按如下配置新建一个账号。
![Banner](./Images/3-2-2.png)

在新创建好的存储账户中，点击“+容器”按钮，新建一个容器。为容器起一个名称，访问类型选择“Blob”，然后点击“确定”，如下图所示：

![Banner](./Images/3-2-3.png)

![Banner](./Images/3-2-4.png)

在存储账号的配置界面中，点击“访问密钥”图标，然后记录下存储账户名称和密钥。

关闭存储账户配置界面，在Azure管理门户中打开之前所创建的Stream Analytics Job，点击“输出”，然后点击“+添加 - Blob存储”按钮。输入如下信息，然后点击“保存”：

<img width="400" height="800" src="./Images/3-2-5.png"/>

### 4.配置Stream Analytics Job查询
在创建好的Stream Analytics Job中点击“查询”，然后输入如下查询语句，并点击“保存“：

Select

system.TimeStamp as Time,

Avg(windSpeed) as WindSpeed,

Avg(Temperature) as Temperature,

Avg(Humidity) as Humidity
  
From input

Group by deviceid, 

TumblingWindow(Second, 10)

在Stream Analytics Job界面中，点击“启动‘，如下图所示：

![Banner](./Images/3-3-1.png)


## 实验四：通过Power BI进行数据展现
### 1.通过Power BI Desktop连接Azure Blob Storage
双击打开Power BI Desktop，然后点击“Get Data”。在数据源中选择“Microsoft Azure Blob Storage”，然后点击”Connect”。输入存储账户的URL，然后点击OK。

![Banner](./Images/4-1-1.png)
![Banner](./Images/4-1-2.png)

输入存储账户的密钥，然后点击“Connect”，如下图所示：

<img width="250" height="500" src="./Images/4-1-3.png"/>

勾选对应的容器，然后点击“Load”按钮，如下图所示：

![Banner](./Images/4-1-4.png)

点击右侧数据边的“...”，再单击“编辑查询”：

![Banner](./Images/4-1-5.png)

在出现的界面中点击“Content”旁边的展开按钮，然后点击OK。

右键点击Source.Name字段，然后点击Remove。右键点击time字段，然后选择Change Type，勾选Date/Time；然后将wind speed，temperature和humidity字段类型设置为”Decimal Number”，然后点击Close&Apply按钮。

### 2.通过 Power BI创建报表
选择折线图展示数据，其中横轴为时间字段，对应的数值为平均风速、平均温度以及平均湿度，最终的展示结果如下图所示：

![Banner](./Images/4-1-6.png)



## 附：安装Power BI Desktop

下载Power BI Desktop： 搜索“Power BI Desktop”并下载

安装 Power BI Desktop，步骤如下：

- 双击，run
- 下一步 
- 接受许可，下一步
- 后续一路默认，下一步，安装完成







