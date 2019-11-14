仍然是一篇动手实验，实验演示如何在Azure的虚拟机内部署一个Web服务器，并且使用Azure Mysql PaaS作为本应用的数据库。此实验的目的一方面是为了演示Azure IaaS层和PaaS服务配合使用的常规操作，另一方面是为之后的文章打基础，后续会以此应用程序和架构为基础，介绍更多Azure的相关服务（如Azure Web 应用，Application Insights，等）。话不多说，直接进入正题吧。
实验开始之前，先介绍下开发环境：
开发语言：Python（3.6）; 项目框架：Django（2.0）;Web服务器：Nginx；wsgi服务器：uwsgi.
## 一、本地配置连接Azure Database for MySQL。
为了方便后期服务器的配置，我们先在本地调试好程序，Azure Database for MySQL的对接比较简单，遵循了Django的常规要求，首先我们在azure portal上创建一个mysql服务：（详细创建过程可以参考官方文档 https://docs.azure.cn/zh-cn/mysql/quickstart-create-mysql-server-database-using-azure-portal ）

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用Azure%20VM%20%2B%20Azure%20Database%20for%20MySQL搭建Web服务1.png)

创建完成后查看服务器信息，记下服务器名称和管理员登录名。
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用Azure%20VM%20%2B%20Azure%20Database%20for%20MySQL搭建Web服务2.png)
然后回到Django项目里的settings.py文件，找到Database部分修改：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用Azure%20VM%20%2B%20Azure%20Database%20for%20MySQL搭建Web服务3.png)
简单介绍下参数：ENGINE表示Django调用数据库的引擎，这里填 ‘django.db.backends.mysql’；NAME表示你要写入和调用的数据库的名称，Portal上创建完Mysql后默认创建**information_schema、mysql、performance_schema 和 sys**这四个数据库，所以你需要在上一步创建服务完成后用工具连接到服务器自己为这个项目创建一个数据库，这里我命名为‘djangopro’；USER和PASSWORD就是你登录数据库的用户名和密码，最后HOST指的是这台server的地址，把上面图里的数据库名称复制在这里就好。到这里还需要在Azure Portal配置下服务器级防火墙规则，去服务器的概述页面，点击左侧的【连接安全性】，点击【添加客户端IP】，保存，这样本机就可以访问数据库了（更多信息可以参考：https://docs.azure.cn/zh-cn/mysql/howto-manage-firewall-using-portal）。
最后因为我们修改了数据库配置，需要重新cd 到你的文件目录下运行：
```
>>python3 manage.py makemigrations
>>python3 manage.py migrate
>>python manage.py createsuperuser 
```
（修改完数据库配置需要重新创建一个超级用户才能登陆后台admin页面）
最后运行 python3 manage.py runserver 0.0.0.0：8000在本地浏览器查看程序，用刚刚创建的superuser登陆后台写入两条数据，再去Azure数据库查看对应的表有没有写进去，没有问题的话这里本地调试就完成了。
## 二、创建VM，安装Python3+Django+Nginx+uwsgi
首先去Azure Portal创建一台VM（这里我用的是Ubuntu 18.10），然后远程登录到VM上安装环境,

**Python3:**
```
sudo apt-get install python3-dev
sudo apt-get install libpcre3 libpcre3-dev
sudo apt install python3-pip
```

**uwsgi:**
```
sudo pip3 install uwsgi
```
安装完uwsgi后需要测试一下，可以在当前目录下创建一个test.py文件，编辑如下：
```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
```
然后执行
```
uwsgi --http-socket :8001 --wsgi-file test.py
```
这里用到了8001端口，因此我们还需要在Azure VM 概述这里把这个端口打开（顺便也可以把80端口打开，后面有用），到portal上添加【入站端口规则】：

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用Azure%20VM%20%2B%20Azure%20Database%20for%20MySQL搭建Web服务4.png)
 
 然后就可以在浏览器中输入 这台机器的IP地址：8001  进行测试了。如果显示Hello World说明uwsgi正常运行。
 
**代码环境：**

```
#安装Django
sudo apt install python3-django

#验证Django

django-admin startproject blog #创建blog项目
cd blog #进入项目
python3 manage.py makemigrations/migrate/runserver 0.0.0.0:8001 #运行django项目

#修改settings.py
ALLOWED_HOSTS = ['VM的IP地址', 'localhost', '127.0.0.1']

#安装python plugin
sudo apt-get install -y uwsgi-plugin-python3
sudo apt-get install uwsgi-plugins-all

#验证uwsgi
uwsgi --http :8001 --chdir /home/ruchan/blog --wsgi-file blog/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9192
#浏览器输入 VM IP地址:8001 出现Django的欢迎界面表示Django项目和uwsgi连接成功
```
**Nginx：**
sudo apt-get install nginx
## 三、本地项目部署到VM上
**验证程序:**
首先先本地的程序文件包上传到VM的某个位置，然后运行，运行过程中可能会报一些错，得自己调试下环境，首先要保证VM的Python版本和Django版本与本地相同，其次可能会缺少一些依赖项，这个就需要看报的什么错进行调试了，以下是我用到的命令：
pip3 install pymysql 
pip3 install django==2.0.2 #更新下Django版本，否则可能会有cannot import '' from django 的错误
sudo apt-get install libmysqld-dev
sudo pip3 install mysqlclient
 
这里还需要修改一下数据库的配置，因为现在是VM访问mysql，所以还需在azure portal上开启一下允许Azure服务的访问（当然这种一开所有Auzre服务都能访问这个库了，细颗粒的还是可以通过IP去做）

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用Azure%20VM%20%2B%20Azure%20Database%20for%20MySQL搭建Web服务5.png)
 
**配置Nginx，uwsgi：**

首先要去代码的settings改下：
```
ALLOWED_HOSTS = ['VM IP地址', 'localhost', '127.0.0.1']
　DEBUG = False #让Nginx来处理静态文件
　STATIC_ROOT = os.path.join(BASE_DIR, '../collectedstatic')#指定下Django收集的静态文件的目录
```

然后修改下uwsgi的配置文件：

```
# hello_uwsgi.ini file
[uwsgi]

# Django-related settings

socket = :8001

# the base directory (full path)
chdir           = /home/ruchan/root0/firstsite #项目地址

# Django s wsgi file
module          = firstsite.wsgi

# process-related settings
# master
master          = true

# maximum number of worker processes
processes       = 4

# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true
# pidfile for record run pid
pidfile        =pid.uwsgi
# 设置日志目录
daemonize    = UWSGI.log
```
 
最后修改下Nginx配置文件：

```
server {
    listen 80;
    server_name VM IP;
    charset utf-8;

    location /static {
    autoindex on;
        alias /home/ruchan/root0/collectedstatic;#项目里Django收集的静态文件的目录地址
        }

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8001;#端口与uwsgi.ini配的一致
        
    }


}
```

然后运行：

```
sudo /etc/init.d/nginx restart 
uwsgi --ini uwsgi.ini
```

最后浏览器输入IP地址看一下效果吧：
![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/用Azure%20VM%20%2B%20Azure%20Database%20for%20MySQL搭建Web服务6.png)
总结：
这个架构还是比较简单粗暴型的，首先没有域名，其次VM高可用暂时没考虑（这点是一个错误示范），不过没关系，后续我们会慢慢完善这些方面的应用和相关内容的添加的。总的来说这是一类应用比较多的场景，自己做了一遍先码在这里，希望能对大家有帮助~
