# 1. 前言
Hello，大家好！第一篇正式的博客，我们先来说说WSL。WSL可以让开发者在 Windows 10 下通过Bash Shell 运行原生的 Ubuntu 用户态二进制程序，工程师们不用再苦恼所用的 Windows 平台上没有合适的 Linux 工具和库了。对于 Linux 的重度用户来说，福音来了。之所以第一篇技术博客介绍 WSL，也是因为我未来技术博客中的实验环境都会以此为基础。那还等什么，让我们来动手实战一下，感受一下 WSL 的强大吧 ！


# 2. WSL简介和原理
WSL 相关代码早在 2016 年 1 月下旬便被微软悄悄内置进了 Windows 10 Build 14251 预览版中，此后微软的开发人员制订了 lxcore.sys 与 lxss.sys 这两个新的子系统文件，让其成为 Windows 程序员开发 Linux 应用程序的桥梁。WSL 是由 Windows 内核团队与 Canonical 合作设计和开发的，可以让 Windows 10 下的开发者们在拥有 Windows 中那些强力支持之外，还能使用 Linux 下丰富的开发环境与工具而不用启动另外的操作系统或者使用虚拟机。这绝对是一个“来自开发者，服务开发者”的 Windows 10 特色，它的目的是让开发者们每天的开发工作都变得顺畅而便捷。我们先来看一下 WSL 的架构和原理图：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Win10%E5%BC%BA%E5%A4%A7%E7%9A%84WSL(Windows%20Subsystem%20for%20Linux)01.jpg)

WSL 对于 Windows 系统来说属于用户态程序，通过虚拟文件系统接口，以 DriveFs 文件系统挂载到 Windows 从而提供和 Windows 的互操作能力。 lxss.sys 和 lxcore.sys 这两个驱动负责模拟 Linux 内核并实时拦截系统调用。相应的驱动会将 Linux 内核调用映射为对应的 Windows 内核调用。根据从微软内部的压力测试工具据来看，WSL 的性能表现非常接近用相同硬件直接运行 Linux 的性能，几乎可以获得同等的 CPU、内存和 I/O 性能，这证明 WSL 在性能方面的表现很出色。


# 3. WSL配置

## 3.1 启用 WSL Feature

顺序：Windows 设置 -> 应用和功能 -> 右侧的程序和功能 -> 启动或关闭windows功能 -> 勾选适用于 Linux 的 Windows 子系统

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Win10%E5%BC%BA%E5%A4%A7%E7%9A%84WSL(Windows%20Subsystem%20for%20Linux)02.jpg)

## 3.2 安装 WSL

Microsoft store 提供了很多 Linux 发行版本可供选择，用户可以根据自己的爱好和习惯去选择自己喜欢的 Linux 发行版本。本文选择 Ubuntu 进行安装，点击启动，第一次会进行初始化安装。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Win10%E5%BC%BA%E5%A4%A7%E7%9A%84WSL(Windows%20Subsystem%20for%20Linux)03.jpg)

初始化安装完成，需要设置帐号密码 ，此处可以根据用户习惯去设置，直接使用 root 或者配置其他用户 sudo 免密切换 root，本文选择使用 sudo 模式。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Win10%E5%BC%BA%E5%A4%A7%E7%9A%84WSL(Windows%20Subsystem%20for%20Linux)04.jpg)

## 3.3 配置 WSL

具体的使用方式和 Ubuntu Linux 一样，可以选择启动Ubuntu Bash Terminal来使用，或者可以将 Bash 放到后台，通过 Termius SSH 远程连接到 Ubuntu，本文即采用该模式。

### 3.3.1 配置sudo免密登陆

```
$ sudo su -
[sudo] password for adminuser:     ##### input password once #####
$ echo "adminuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
```

### 3.3.2 重装openssh并启动

```
$ apt-get remove openssh-server
$ apt-get update     ##### 默认源 ubuntu canonical, 如果无法访问，可以根据网络状况自行修改或者科学上网 #####
$ apt-get install openssh-server
$ vi /etc/ssh/sshd_config
  修改 PasswordAuthentication no 为 PasswordAuthentication yes
  :wq 保存退出
$ service ssh --full-restart
```

### 3.3.3 通过Termius远程连接
Termius 是 Windows 10 上远程连接 Linux 的终端工具，Microsoft store 可以下载，UI、功能性都不错，可以一用。如果大家有自己喜爱的工具，也可以选择喜欢的工具。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Win10%E5%BC%BA%E5%A4%A7%E7%9A%84WSL(Windows%20Subsystem%20for%20Linux)05.jpg)

## 3.4 Bash放到后台，SSH服务开机启动

现在有一个问题，每次 Windows 关机开机之后都需要手动启动 Bash.exe，然后 start ssh service 才可以远程连接使用。每次都需要这样做一次，很繁琐。下面就来介绍一下 SSH 服务如何开机启动吧~

### 3.4.1 sudo免密登陆

根据目前的操作系统的用户，先配置免密登陆，具体参考 3.3.1。

### 3.4.1 通过VB script开机启动SSH

写一个 VB 通过调用 Bash.exe 启动 SSH 服务的脚本，例如 startssh.vbs：

```
set ws=wscript.createobject("wscript.shell")
ws.run "C:\Windows\System32\bash.exe",0
ws.run "C:\Windows\System32\bash.exe  -c 'sudo /usr/sbin/service ssh start'",0
```

然后将startssh.vbs放到如下目录(**需要管理员权限**)。

```
%AppData%\Microsoft\Windows\Start Menu\Programs\Startup
```

开机启动配置完毕。


# 4. 总结
总体上，WSL的配置就结束了。现在可以在此基础上去配置所需要的开发或者其他组件了，其实WSL也可以像虚拟机一样去备份、回滚等等，很多的其他的功能或玩法，有待大家自己开发了~
