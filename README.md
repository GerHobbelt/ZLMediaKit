![logo](https://raw.githubusercontent.com/xia-chu/ZLMediaKit/master/www/logo.png)

[english readme](https://github.com/xia-chu/ZLMediaKit/blob/master/README_en.md)

# 一个基于C++11的高性能运营级流媒体服务框架

[![license](http://img.shields.io/badge/license-MIT-green.svg)](https://github.com/xia-chu/ZLMediaKit/blob/master/LICENSE)
[![C++](https://img.shields.io/badge/language-c++-red.svg)](https://en.cppreference.com/)
[![platform](https://img.shields.io/badge/platform-linux%20|%20macos%20|%20windows-blue.svg)](https://github.com/xia-chu/ZLMediaKit)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-yellow.svg)](https://github.com/xia-chu/ZLMediaKit/pulls)
[![Build Status](https://travis-ci.org/xia-chu/ZLMediaKit.svg?branch=master)](https://travis-ci.org/xia-chu/ZLMediaKit)

## 项目特点

- 基于C++11开发，避免使用裸指针，代码稳定可靠，性能优越。
- 支持多种协议(RTSP/RTMP/HLS/HTTP-FLV/WebSocket-FLV/GB28181/HTTP-TS/WebSocket-TS/HTTP-fMP4/WebSocket-fMP4/MP4/WebRTC),支持协议互转。
- 使用多路复用/多线程/异步网络IO模式开发，并发性能优越，支持海量客户端连接。
- 代码经过长期大量的稳定性、性能测试，已经在线上商用验证已久。
- 支持linux、macos、ios、android、windows全平台。
- 支持画面秒开、极低延时([500毫秒内，最低可达100毫秒](https://github.com/xia-chu/ZLMediaKit/wiki/%E5%BB%B6%E6%97%B6%E6%B5%8B%E8%AF%95))。
- 提供完善的标准[C API](https://github.com/xia-chu/ZLMediaKit/tree/master/api/include),可以作SDK用，或供其他语言调用。
- 提供完整的[MediaServer](https://github.com/xia-chu/ZLMediaKit/tree/master/server)服务器，可以免开发直接部署为商用服务器。
- 提供完善的[restful api](https://github.com/xia-chu/ZLMediaKit/wiki/MediaServer%E6%94%AF%E6%8C%81%E7%9A%84HTTP-API)以及[web hook](https://github.com/xia-chu/ZLMediaKit/wiki/MediaServer%E6%94%AF%E6%8C%81%E7%9A%84HTTP-HOOK-API)，支持丰富的业务逻辑。
- 打通了视频监控协议栈与直播协议栈，对RTSP/RTMP支持都很完善。
- 全面支持H265/H264/AAC/G711/OPUS。

## 项目定位

- 移动嵌入式跨平台流媒体解决方案。
- 商用级流媒体服务器。
- 网络编程二次开发SDK。


## 功能清单
### 功能一览
<img width="800" alt="功能一览" src="https://user-images.githubusercontent.com/11495632/114176523-d50fce80-996d-11eb-81f8-0a2e2715ba7b.png">

- RTSP[S]
  - RTSP[S] 服务器，支持RTMP/MP4/HLS转RTSP[S],支持亚马逊echo show这样的设备
  - RTSP[S] 播放器，支持RTSP代理，支持生成静音音频
  - RTSP[S] 推流客户端与服务器
  - 支持 `rtp over udp` `rtp over tcp` `rtp over http` `rtp组播`  四种RTP传输方式 
  - 服务器/客户端完整支持Basic/Digest方式的登录鉴权，全异步可配置化的鉴权接口
  - 支持H265编码
  - 服务器支持RTSP推流(包括`rtp over udp` `rtp over tcp`方式)
  - 支持H264/H265/AAC/G711/OPUS编码，其他编码能转发但不能转协议

- RTMP[S]
  - RTMP[S] 播放服务器，支持RTSP/MP4/HLS转RTMP
  - RTMP[S] 发布服务器，支持录制发布流
  - RTMP[S] 播放器，支持RTMP代理，支持生成静音音频
  - RTMP[S] 推流客户端
  - 支持http[s]-flv直播
  - 支持websocket-flv直播
  - 支持H264/H265/AAC/G711/OPUS编码，其他编码能转发但不能转协议
  - 支持[RTMP-H265](https://github.com/ksvc/FFmpeg/wiki)
  - 支持[RTMP-OPUS](https://github.com/xia-chu/ZLMediaKit/wiki/RTMP%E5%AF%B9H265%E5%92%8COPUS%E7%9A%84%E6%94%AF%E6%8C%81)

- HLS
  - 支持HLS文件生成，自带HTTP文件服务器
  - 通过cookie追踪技术，可以模拟HLS播放为长连接，可以实现HLS按需拉流、播放统计等业务
  - 支持HLS播发器，支持拉流HLS转rtsp/rtmp/mp4
  - 支持H264/H265/AAC/G711/OPUS编码
  
- TS
  - 支持http[s]-ts直播
  - 支持ws[s]-ts直播
  - 支持H264/H265/AAC/G711/OPUS编码
  
- fMP4
  - 支持http[s]-fmp4直播
  - 支持ws[s]-fmp4直播
  - 支持H264/H265/AAC/G711/OPUS编码

- HTTP[S]与WebSocket
  - 服务器支持`目录索引生成`,`文件下载`,`表单提交请求`
  - 客户端提供`文件下载器(支持断点续传)`,`接口请求器`,`文件上传器`
  - 完整HTTP API服务器，可以作为web后台开发框架
  - 支持跨域访问
  - 支持http客户端、服务器cookie
  - 支持WebSocket服务器和客户端
  - 支持http文件访问鉴权

- GB28181与RTP推流
  - 支持UDP/TCP国标RTP(PS或TS)推流服务器，可以转换成RTSP/RTMP/HLS等协议
  - 支持RTSP/RTMP/HLS转国标推流客户端，支持TCP/UDP模式，提供相应restful api
  - 支持H264/H265/AAC/G711/OPUS编码
  - 支持海康ehome推流

- MP4点播与录制
  - 支持录制为FLV/HLS/MP4
  - RTSP/RTMP/HTTP-FLV/WS-FLV支持MP4文件点播，支持seek
  - 支持H264/H265/AAC/G711/OPUS编码
  
- WebRTC(体验,请使用dev分支)
  - 支持WebRTC推流，支持转其他协议
  - 支持WebRTC播放，支持其他协议转WebRTC     
  
- 其他
  - 支持丰富的restful api以及web hook事件 
  - 支持简单的telnet调试
  - 支持配置文件热加载
  - 支持流量统计、推拉流鉴权等事件
  - 支持虚拟主机,可以隔离不同域名
  - 支持按需拉流，无人观看自动关断拉流
  - 支持先拉流后推流，提高及时推流画面打开率
  - 提供c api sdk
  - 支持FFmpeg拉流代理任意格式的流
  - 支持http api生成并返回实时截图
  - 支持按需解复用、转协议，当有人观看时才开启转协议
  

## 编译以及测试
**编译前务必仔细参考wiki:[快速开始](https://github.com/xia-chu/ZLMediaKit/wiki/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)操作!!!**

## 怎么使用

 你有三种方法使用ZLMediaKit，分别是：

 - 1、使用c api，作为sdk使用，请参考[这里](https://github.com/xia-chu/ZLMediaKit/tree/master/api/include).
 - 2、作为独立的流媒体服务器使用，不想做c/c++开发的，可以参考[restful api](https://github.com/xia-chu/ZLMediaKit/wiki/MediaServer%E6%94%AF%E6%8C%81%E7%9A%84HTTP-API)和[web hook](https://github.com/xia-chu/ZLMediaKit/wiki/MediaServer%E6%94%AF%E6%8C%81%E7%9A%84HTTP-HOOK-API).
 - 3、如果想做c/c++开发，添加业务逻辑增加功能，可以参考这里的[测试程序](https://github.com/xia-chu/ZLMediaKit/tree/master/tests).

## Docker 镜像

你可以从Docker Hub下载已经编译好的镜像并启动它：

```bash
docker run -id -p 1935:1935 -p 8080:80 -p 8554:554 -p 10000:10000 -p 10000:10000/udp panjjo/zlmediakit
```

你也可以根据Dockerfile编译镜像：

```bash
bash build_docker_images.sh
```

## 合作项目

 - 可视化管理网站
    - [一个非常漂亮的可视化后台管理系统](https://github.com/MingZhuLiu/ZLMediaServerManagent)
    - [基于ZLMediaKit主线的管理WEB网站](https://gitee.com/kkkkk5G/MediaServerUI) 
    - [基于ZLMediaKit分支的管理WEB网站](https://github.com/chenxiaolei/ZLMediaKit_NVR_UI)
    
 - 流媒体管理平台
   - [功能强大的流媒体控制管理接口平台,支持GB28181](https://github.com/chatop2020/StreamNode)
   - [GB28181-2016网络视频平台](https://github.com/648540858/wvp-GB28181-pro)
   - [node-js版本的GB28181平台](https://gitee.com/hfwudao/GB28181_Node_Http)
   - [Go实现的海康ehome服务器](https://github.com/tsingeye/FreeEhome)

 - 客户端
   - [基于C SDK实现的推流客户端](https://github.com/hctym1995/ZLM_ApiDemo)
   - [C#版本的Http API与Hook](https://github.com/chengxiaosheng/ZLMediaKit.HttpApi)
   - [DotNetCore的RESTful客户端](https://github.com/MingZhuLiu/ZLMediaKit.DotNetCore.Sdk)

## 授权协议

本项目自有代码使用宽松的MIT协议，在保留版权信息的情况下可以自由应用于各自商用、非商业的项目。
但是本项目也零碎的使用了一些其他的开源代码，在商用的情况下请自行替代或剔除；
由于使用本项目而产生的商业纠纷或侵权行为一概与本项目及开发者无关，请自行承担法律风险。
在使用本项目代码时，也应该在授权协议中同时表明本项目依赖的第三方库的协议。

## 联系方式

 - 邮箱：<1213642868@qq.com>(本项目相关或流媒体相关问题请走issue流程，否则恕不邮件答复)
 - QQ群：542509000

## 怎么提问？

如果要对项目有相关疑问，建议您这么做：

 - 1、仔细看下readme、wiki，如果有必要可以查看下issue.
 - 2、如果您的问题还没解决，可以提issue.
 - 3、有些问题，如果不具备参考性的，无需在issue提的，可以在qq群提.
 - 4、QQ私聊一般不接受无偿技术咨询和支持([为什么不提倡QQ私聊](https://github.com/xia-chu/ZLMediaKit/wiki/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E5%BB%BA%E8%AE%AEQQ%E7%A7%81%E8%81%8A%E5%92%A8%E8%AF%A2%E9%97%AE%E9%A2%98%EF%BC%9F)).

## 特别感谢

本项目采用了[老陈](https://github.com/ireader) 的 [media-server](https://github.com/ireader/media-server) 库，
本项目的 ts/fmp4/mp4/ps 容器格式的复用解复用都依赖media-server库。在实现本项目诸多功能时，老陈多次给予了无私热情关键的帮助，
特此对他表示诚挚的感谢！

## 致谢

感谢以下各位对本项目包括但不限于代码贡献、问题反馈、资金捐赠等各种方式的支持！以下排名不分先后：

[老陈](https://github.com/ireader)
[Gemfield](https://github.com/gemfield)
[南冠彤](https://github.com/nanguantong2)
[凹凸慢](https://github.com/tsingeye)
[chenxiaolei](https://github.com/chenxiaolei)
[史前小虫](https://github.com/zqsong)
[清涩绿茶](https://github.com/baiyfcu)
[3503207480](https://github.com/3503207480)
[DroidChow](https://github.com/DroidChow)
[阿塞](https://github.com/HuoQiShuai)
[火宣](https://github.com/ChinaCCF)
[γ瑞γミ](https://github.com/JerryLinGd)
[linkingvision](https://www.linkingvision.com/)
[茄子](https://github.com/taotaobujue2008)
[好心情](<409257224@qq.com>)
[浮沉](https://github.com/MingZhuLiu)
[Xiaofeng Wang](https://github.com/wasphin)
[doodoocoder](https://github.com/doodoocoder)
[qingci](https://github.com/Colibrow)
[swwheihei](https://github.com/swwheihei)
[KKKKK5G](https://gitee.com/kkkkk5G)
[Zhou Weimin](<zhouweimin@supremind.com>)
[Jim Jin](https://github.com/jim-king-2000)
[西瓜丶](<392293307@qq.com>)
[MingZhuLiu](https://github.com/MingZhuLiu)
[chengxiaosheng](https://github.com/chengxiaosheng)
[big panda](<2381267071@qq.com>)
[tanningzhong](https://github.com/tanningzhong)
[hctym1995](https://github.com/hctym1995)
[hewenyuan](https://gitee.com/kingyuanyuan)
[sunhui](<sunhui200475@163.com>)
[mirs](fangpengcheng@bilibili.com>)
[Kevin Cheng](kevin__cheng@outlook.com>)
[Liu Jiang](root@oopy.org>)
[along](alongl@users.noreply.github.com>)
[qingci](xpy66swsry@gmail.com>)
[lyg1949](zh.ghlong@qq.com>)
[zhlong](zh.ghlong@qq.com>)
[Luke](automan@easydarwin.org>)
[大裤衩](3503207480@qq.com>)
[droid.chow](droid.chow@gmail.com>)
[陈晓林](https://github.com/musicwood)

## 使用案例

本项目已经得到不少公司和个人开发者的认可，据作者不完全统计，
使用本项目的公司包括知名的互联网巨头、国内排名前列的云服务公司、多家知名的AI独角兽公司，
以及一系列中小型公司。使用者可以通过在 [issue](https://github.com/xia-chu/ZLMediaKit/issues/511) 上粘贴公司的大名和相关项目介绍为本项目背书，感谢支持！


## 捐赠

您的捐赠将用于支付该项目的一些费用支出以及激励开发者，
欢迎捐赠以便更好的推动项目的发展，谢谢您的支持!
同时欢迎捐赠公网服务器用于在线展示效果。

[支付宝](https://gitee.com/xia-chu/other/raw/master/IMG_3919.JPG)

[微信](https://gitee.com/xia-chu/other/raw/master/IMG_3920.JPG)


----

\[Google Translate:]


# A high-performance operational-level streaming media service framework based on C++11

# Project Features
* Based on C++11 development, avoid using raw pointers, the code is stable and reliable, and the performance is superior.
* Support multiple protocols (RTSP/RTMP/HLS/HTTP-FLV/WebSocket-FLV/GB28181/HTTP-TS/WebSocket-TS/HTTP-fMP4/WebSocket-fMP4/MP4/WebRTC), support protocol conversion.
* Use multiplexing/multithreading/asynchronous network IO mode development, superior concurrency performance, support massive client connections.
* The code has undergone a large number of long-term stability and performance tests, and has been commercially verified online for a long time.
* Support linux, macos, ios, android, windows all platforms.
* Support the screen to open in seconds, very low delay (within 500 milliseconds, the lowest can reach 100 milliseconds).
* Provide complete standard C API, can be used as SDK, or for other languages ​​to call.
* Provide a complete MediaServer server, which can be directly deployed as a commercial server without development.
* Provide complete restful api and web hook, support rich business logic.
* The video surveillance protocol stack and the live broadcast protocol stack have been opened up, and the RTSP/RTMP support is very complete.
* Fully supports H265/H264/AAC/G711/OPUS.

## Project positioning
* Mobile embedded cross-platform streaming media solutions.
* Commercial-grade streaming media server.
* Network programming secondary development SDK.

## Function list
Features at a glance

### RTSP[S]

* RTSP[S] server, supports RTMP/MP4/HLS to RTSP[S], supports devices such as Amazon echo show
* RTSP[S] player, supports RTSP proxy, supports generating mute audio
* RTSP[S] Push streaming client and server
* Support rtp over udp rtp over tcp rtp over http rtp multicast four kinds of RTP transmission methods
* Server/client fully supports login authentication in Basic/Digest mode, fully asynchronous and configurable authentication interface
* Support H265 encoding
* The server supports RTSP streaming (including rtp over udp rtp over tcp)
* Support H264/H265/AAC/G711/OPUS encoding, other encodings can be forwarded but not transferred to protocol

### RTMP[S]

* RTMP[S] Play server, support RTSP/MP4/HLS to RTMP
* RTMP[S] publishing server, supports recording and publishing stream
* RTMP[S] player, supports RTMP proxy, supports generating mute audio
* RTMP[S] streaming client
* Support http[s]-flv live broadcast
* Support websocket-flv live broadcast
* Support H264/H265/AAC/G711/OPUS encoding, other encodings can be forwarded but not transferred to protocol
* Support RTMP-H265
* Support RTMP-OPUS


### HLS

* Support HLS file generation, with HTTP file server
* Through cookie tracking technology, HLS playback can be simulated as a long connection, and services such as HLS on-demand streaming and playback statistics can be realized.
* Support HLS broadcaster, support streaming HLS to rtsp/rtmp/mp4
* Support H264/H265/AAC/G711/OPUS encoding

### TS

* Support http[s]-ts live broadcast
* Support ws[s]-ts live broadcast
* Support H264/H265/AAC/G711/OPUS encoding

### fMP4

* Support http[s]-fmp4 live broadcast
* Support ws[s]-fmp4 live broadcast
* Support H264/H265/AAC/G711/OPUS encoding



### HTTP[S] and WebSocket

* The server supports catalog index generation, file download, form submission request
* The client provides a file downloader (supports resumable upload), an interface requester, and a file uploader
* Complete HTTP API server, which can be used as a web background development framework
* Support cross-domain access
* Support http client, server cookie
* Support WebSocket server and client
* Support http file access authentication


### GB28181 and RTP streaming

* Support UDP/TCP national standard RTP (PS or TS) push server, which can be converted into RTSP/RTMP/HLS and other protocols
* Support RTSP/RTMP/HLS to national standard push streaming client, support TCP/UDP mode, provide corresponding restful api
* Support H264/H265/AAC/G711/OPUS encoding
* Support Haikang ehome push streaming


### MP4 on-demand and recording

* Support recording as FLV/HLS/MP4
* RTSP/RTMP/HTTP-FLV/WS-FLV support MP4 file on demand, support seek
* Support H264/H265/AAC/G711/OPUS encoding

### WebRTC (experience, please use the dev branch)

* Support WebRTC push stream, support transfer to other protocols
* Support WebRTC playback, support other protocols to WebRTC



### other

* Support rich restful api and web hook events
* Support simple telnet debugging
* Support configuration file hot loading
* Support traffic statistics, push-pull flow authentication and other events
* Support virtual host, can isolate different domain names
* Support on-demand streaming, automatic shutdown of streaming when no one is watching
* Support to pull the stream first and then push the stream, improve the opening rate of the timely push stream screen
* Provide c api sdk
* Support FFmpeg to pull streams in any format
* Support http api to generate and return real-time screenshots
* Support on-demand demultiplexing and protocol transfer, and the transfer protocol will be turned on when someone is watching


### Compile and test

Be sure to refer to the wiki carefully before compiling: get started quickly!!!

### how to use

You have three ways to use ZLMediaKit, they are:

1. Use c api and use it as sdk, please refer to here.
2. As an independent streaming media server, if you don't want to do c/c++ development, you can refer to restful api and web hook.
3. If you want to do c/c++ development and add business logic to increase functions, you can refer to the test program here.

### Docker image

You can download the compiled image from Docker Hub and start it:

    docker run -id -p 1935:1935 -p 8080:80 -p 8554:554 -p 10000:10000 -p 10000:10000/udp panjjo/zlmediakit


You can also compile the image according to the Dockerfile:

    bash build_docker_images.sh


### Cooperation projects

#### Visual management website

* A very beautiful visual background management system
* Management WEB website based on ZLMediaKit main line
* Management WEB website based on ZLMediaKit branch


#### Streaming media management platform

* Powerful streaming media control management interface platform, support GB28181
* GB28181-2016 network video platform
* Node-js version of GB28181 platform
* Haikang ehome server implemented by Go


#### Client

* Push streaming client based on C SDK
* C# version of Http API and Hook
* DotNetCore's RESTful client


### License agreement

The project's own code uses the loose MIT protocol, and can be freely applied to their respective commercial and non-commercial projects while retaining copyright information. However, this project also uses some other open source code piecemeal, please replace or remove it by yourself in the case of commercial use; commercial disputes or infringements arising from the use of this project have nothing to do with the project and the developer, please bear the law by yourself risk. When using the code of this project, the license agreement should also indicate the agreement of the third-party library that this project relies on.

### contact details

Email: 1213642868@qq.com (For questions related to this project or streaming media, please follow the issue process, otherwise no email reply will be made)
QQ group: 542509000


### How to ask questions?

If you have any questions about the project, we suggest you do this:

1. Read the readme and wiki carefully, and check the issue if necessary.
2. If your problem has not been resolved, you can submit an issue.
3. For some questions, if they are not of reference, they do not need to be mentioned in the issue, they can be mentioned in the qq group.
4. QQ private chat generally does not accept free technical consultation and support (why not advocate QQ private chat).

### Special thanks to

This project uses the old Chen's media-server library. The reuse and demultiplexing of the ts/fmp4/mp4/ps container format of this project all rely on the media-server library. In the realization of many functions of this project, Lao Chen has repeatedly given the key help of selfless enthusiasm, and hereby express my sincere thanks to him!

### Thanks

Thank you for your support to this project including but not limited to code contributions, problem feedback, fund donations, etc.! The following rankings are in no particular order:

Old Chen Gemfield Nan Guantong bumpy slow chenxiaolei prehistoric bug Qing astringent green tea 3503207480 DroidChow Asai fire xuan γ Rui ミ linking vision eggplant good mood ups and downs Xiaofeng Wang doodoocoder qingci swwheihei KKKKK5G Zhou Weimin Jim Jin watermelon, MingZhuLiu 1995 hechengxiaosheng sunwen big panda hctym tanningzhongyuan mirs Kevin Cheng Liu Jiang along qingci lyg1949 zhlong Luke big pants droid.chow Chen Xiaolin

### Use Cases

This project has been recognized by many companies and individual developers. According to the author's incomplete statistics, companies using this project include well-known Internet giants, top domestic cloud service companies, many well-known AI unicorn companies, and A series of small and medium companies. Users can endorse this project by pasting the company's name and related project introduction on the issue, thank you for your support!

### Donate

Your donation will be used to pay for some expenses of the project and to motivate developers. Donations are welcome to better promote the development of the project, thank you for your support! At the same time, you are welcome to donate public network servers for online display effects.

Alipay 

