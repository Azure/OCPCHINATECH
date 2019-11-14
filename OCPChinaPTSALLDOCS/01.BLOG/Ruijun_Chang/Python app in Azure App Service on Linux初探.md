使用Azure应用托管平台服务，可以为运维人员省去大量的基础服务器的管理工作，并且可以和Azure DevOps, GitHub, BitBucket, Docker Hub, Azure Container Registry等配合使用实现持续集成和持续部署。现阶段Global Azure也推出了Azure App Service on Linux 服务，用户可以托管他们的应用在Linux环境下，目前支持大多数开发语言和版本，对Python的支持处于public preview阶段，接下来我们做一个Django项目的操作演示，探索下这项服务的使用。
 
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Python%20app%20in%20Azure%20App%20Service%20on%20Linux初探1.png)

1. 首先我们在本地创建一个Django项目hello,确认运行没问题；
```
django-admin startproject hello
cd hello
python  manage.py makemigrations
python  manage.py migrate
python manage.py createsuperuser
python  manage.py runserver
```
 
2. 然后在项目所在的文件夹下运行：
`
pip freeze > requirements.txt
`
这一步是为了生成本项目所依赖的环境清单，例如
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Python%20app%20in%20Azure%20App%20Service%20on%20Linux初探2.png)
 
 
 因为应用是以Docker container的方式跑在后台的，所以后面部署至Azure的时候容器会自动运行pip install -r requirements.txt来安装这个应用的依赖项。
 3，上传至web app，运行命令：
`
az webapp up -n ruchanappdemo
`
运行完的截图如下：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Python%20app%20in%20Azure%20App%20Service%20on%20Linux初探3.png)
 简单描述一下这个过程，az webapp up这个命令会自动执行以下几步：
(1)，创建一个默认的资源组appsvc_rg_Linux_centralus；
(2)，创建一个默认的app plan appsvc_asp_Linux_centralus；
(3)，创建一个app，名称为ruchanappdemo;
(4)，将项目打包，从现在的目录下部署到创建的web 服务上。
看下这条命令的参数：

目前要求的参数里，支持了指定的订阅，产品组正在把--resource-group 和--plan加进去，方便用户指定特定的资源组和应用服务计划。
上传完成后，浏览器输入https://ruchanappdemo.azurewebsites.net 发现报错了，正常，，因为我们需要把ALLOWED_HOSTS修改下：
```
ALLOWED_HOSTS = ['ruchanappdemo0.azurewebsites.net']
```
修改完了重新运行更新：
`
az webapp up -n ruchanappdemo -l centralus #-l 代表location
`
最后检查结果，可以了。
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Python%20app%20in%20Azure%20App%20Service%20on%20Linux初探4.png)
 几点补充说明的：
1. 修改web app 的python版本：

`
az webapp config set --resource-group <resource-group-name> --name <app-name> --linux-fx-version "PYTHON|3.7"
`

2. 应用的后台默认用guicorn做WSGI和http服务器，支持guicorn的自定义配置，例如：

`
gunicorn --bind=0.0.0.0 --timeout 600 --chdir website hello:myapp
`

如果要用non-Gunicorn 服务器，也可以用命令更改：

`
python3.7 -m aiohttp.web -H localhost -P 8080 package.module:init_func
`

3. 每一个应用部署过程，都会先自动检查有没有Django文件，下来检查有没有Flask,如果两个框架都没找到，就运行一个默认的app出来。如果你想运行一个自定义的docker image，可以参考：https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image 
4. 其他一些比如为应用加自定义域名，查看容器里的日志等，可以参考：https://docs.microsoft.com/en-us/azure/app-service/containers/how-to-configure-python#customize-startup-command.
最后附上一些其他的参考链接：
https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python；
https://docs.microsoft.com/en-us/azure/app-service/containers/how-to-configure-python；
https://docs.microsoft.com/zh-cn/azure/app-service/manage-custom-dns-buy-domain.
