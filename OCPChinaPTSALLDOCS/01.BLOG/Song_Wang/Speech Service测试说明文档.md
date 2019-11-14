一. 创建Speech Service

1. 登录到azure.com portal，左上角点击创建，在搜索框输入“Speech”，选择Speech Service，未来必应语音API会集成到Speech Service，所以直接使用Speech Service测试即可。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A301.png)

2. 创建选择“东亚”，香港数据中心，选择S0的定价层，F0是免费使用，超过一定时间会有限制
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A302.png)

3. 具体S0定价层参考：https://azure.microsoft.com/zh-cn/pricing/details/cognitive-services/speech-services/

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A303.png)

4. 创建完成后进入到Speech Service，点击到key，这是我们使用过程中需要用到的
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A304.png)

5. 创建完成后就可以进行测试，以Java SDK为例，参考sample code，可以把如下图的key和region两个参数替换，key就是用创建服务的key，region为：eastasia，https://docs.microsoft.com/zh-cn/azure/cognitive-services/speech-service/how-to-recognize-speech-java

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A305.png)

6. SDK参考，https://docs.microsoft.com/zh-cn/azure/cognitive-services/speech-service/，左侧是文档的目录介绍，可以参考。
 
![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A306.png)

7. 关于语音转文本的 介绍：可以参考：https://docs.microsoft.com/zh-cn/azure/cognitive-services/speech-service/speech-to-text，
https://azure.microsoft.com/zh-cn/services/cognitive-services/speech-to-text/

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A307.png)

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/Speech%20Service%E6%B5%8B%E8%AF%95%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A308.png)

8． 关于其他文字转语音，翻译功能类似POC可以参考。
