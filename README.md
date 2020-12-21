# tiebaRobot
# python顶贴机器人视频演示如下
<br>



[python顶贴机器人演示视频](https://player.youku.com/embed/XNTAxOTIxNjUwMA==)
## 测试版本：

<br>
python 3.7 64位  <br>
火狐浏览器firefox 83.0 (64 位)  <br>
 selenium       3.141.0 <br>
<br>

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221224250688.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70)
 <br>
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221224250510.png)
 
 <br>

## 文件目录结构如下图：

<br>
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221221701406.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70#pic_center)

<br>

## 开发这款小工具，我们需要做一些准备：

 - url.txt：多个需要顶起的帖子地址。
 - reply：多条随机回复的内容。
 - selenium：浏览器自动化测试框架。
<br>
 url.txt-------每行要有回车换行符，因为代码通过读取文件每行的ip地址，可自行修改不同的ip地址，用换行符分割！
 reply.txt-------每行要有回车换行符，因为代码通过读取文件每行的回复内容，可自行修改不同的回复内容，用换行符分割！![url.txt](https://img-blog.csdnimg.cn/20201221222626654.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70)![reply.txt](https://img-blog.csdnimg.cn/20201221222626651.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70)
 - 首先，我们先使用pip完成selenium的安装。
 -   接着，导入pyautogui自动控制鼠标的库。


 
**示例代码：**
```
pip install -U selenium
```
```
pip install pyautogui
```
<br>
selenium实现自动化脚本，pyautogui实现自动控制鼠标，因为之前小编在其他顶贴机器人教程没有使用pyautogui库，所有百度贴吧会识别是机器人的行为，所有要加上自动模拟鼠标认为的操作，小编在此被坑了好久。终于脱坑了~<br>
接下来，我们添加对浏览器的支持，这里使用火狐浏览器。<br>
对应Windows环境下的火狐浏览器，我们需要下载一个小程序：geckodriver.exe

<br>

## 火狐64位浏览器下载地址：
[https://www.techspot.com/downloads/19-mozilla-firefox.html](https://www.techspot.com/downloads/19-mozilla-firefox.html)

## geckodriver.exe驱动大全 firefox官方镜像下载地址：
 1. geckodriver.exe驱动大全 ：[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
 2. firefox官方镜像地址：[https://download-installer.cdn.mozilla.net/pub/firefox/releases/](https://github.com/mozilla/geckodriver/releases)
<br>

## tieba.py的cookie的配置

关于代码文件tieba.py的cookie的配置，请用火狐浏览器登录自己的贴吧账号，打开要顶贴的网址，鼠标右键-->检测元素（或者按F12）-->点开网络-->打开请求的cookie，修改Python代码里面cookie里面的变量，注意键值对的空格和分号！！详细如下图：<br>
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221224813555.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70#pic_center)
<br>

## 完整代码如下图：

tieba.py
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221221418134.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221221417811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221221417665.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDg3OTU4,size_16,color_FFFFFF,t_70)


<br>

**完整代码和下载地址：[https://www.fang1688.cn/python/1380.html](https://www.fang1688.cn/python/1380.html)**

[更多python知识学习，尽在方包博客---www.fang1688.cn](http://www.fang1688.cn)

![关注公众号“优派编程”，搜索关键字获取更多学习资料](https://www.fang1688.cn/wp-content/uploads/2020/07/qrcode_for_gh_1fd2e4a34038_258.jpg)
<strong>关注公众号“优派编程”，搜索关键字获取更多学习资料</strong>
