# 网络原理

#  TCP/IP五层模型 OSI七层模型
## 参考文档：https://mp.weixin.qq.com/s?__biz=Mzg3MjA4MTExMw==&mid=2247495857&idx=2&sn=7c036f2e6c5a2ec3251bf8a657f5e301

## 五层模型 VS 七层模型

   ![avatar](https://images2015.cnblogs.com/blog/705728/201604/705728-20160424234825491-384470376.png)
   
## TCP/IP 协议簇

    TCP/IP 协议说的不仅仅只是 TCP 和 IP 这两种协议，实际上，TCP/IP 指的是协议簇
    
    TCP/IP 协议有以下协议：

  ![avatar](https://mmbiz.qpic.cn/mmbiz_png/A3ibcic1Xe0iaTicuU6kBxkISjlPjd8lZLl4icmhUtRazAIOiaGSq7q85QA7B6OFQbk113W4kWOe0zeafUeC1SlN4D0A/640)
  

## 每层协议

![avatar](https://images2015.cnblogs.com/blog/705728/201604/705728-20160424234824085-667046040.png)

![avatar](https://images2015.cnblogs.com/blog/705728/201604/705728-20160424234827195-1493107425.png)
### 1. 通信链路层

    通信链路层也可以分为 物理层 和 数据链路层

    1. 物理层
    
        物理层是 TCP/IP 的最底层是负责传输的硬件，这种硬件就相当于是以太网或电话线路等物理层的设备
        
        作用：
            定义物理设备标准,网线的接口类型
        
        物理设备：
            中继器 集线器 双绞线
        
    2. 数据链路层
        
        作用：
            数据链路层定义了在单个链路上如何传输数据
            
        物理设备：
             网桥 交换机 网卡
             
### 2. 网络层

        作用：
            
            网络层主要使用 IP协议， 将分组数据包发送到目标主机
            
        物理设备：
            
            三层交换机  路由器
            
        网络层还有一种协议就是 ICMP，因为 IP 在数据包的发送过程中可能会出现异常，当 IP 数据包因为异常而无法到达目标地址时，
        需要给发送端发送一个异常通知，ICMP 的主要功能就在于此了。鉴于此情况，ICMP 也可以被用来诊断网络情况
        
### 3. 传输层
        
     传输层就好像高速公路一样，连接两个城市的道路
     
     传输层的协议主要分为面向有连接的协议 TCP 和面向无连接的协议 UDP
     
     作用：
            
           让应用层的应用程序之间完成通信和数据交换
            
        物理设备：
            
            四层交换机  四层路由器 

### 4. 应用层

    OSI 标准模型中的会话层、表示层都归为了应用层
    
    作用：
        为应用软件提供服务
        
###  ARP协议在哪一层：

    在TCP/IP模型中，ARP协议属于IP层；在OSI模型中，ARP协议属于链路层
    
    TCP/IP模型中，所有定义的协议至少是在网络层
    
    OSI的标准,当数据向下传递时,每层会加上自己的信息,各层互不干扰.这样当网络层的IP包进入链路层时,
    链路层该如何加这个头部的目标信息呢?它要依靠ARP协议来完成.显然如何加链路头并不是网络层的功能.
    而且，ARP协议工作时，并不使用IP的包头。所以也有很多人说，ARP是链路层的
        
## 数据包的发送历程

### 数据包结构
   
   ![avatar](https://mmbiz.qpic.cn/mmbiz_png/A3ibcic1Xe0iaTicuU6kBxkISjlPjd8lZLl4ibeianUVm2oBCsuRfzDo8bWh2ic9wQw84lwiaia5xX42OeeGwpRuIm9nP0A/640)
   
    每个分层中，都会对所发送的数据增加一个 首部，这个首部中包含了该层必要的信息
    
### 数据包发送历程
    
    假设主机 A 和主机 B 进行通信，主机 A 想要向主机 B 发送一个数据包， 经历一下步骤
    
#### 1. 应用层的处理
    
    主机 A 也就是用户点击了某个应用或者打开了一个聊天窗口输入了cxuan，然后点击了发送 ，
    应用层还需要对这个数据包进行处理，包括字符编码、格式化等等， ，这一层其实是 OSI 中表现层做的工作，只不过在 TCP/IP 协议中都归为了应用层
    
    数据包在发送的那一刻建立 TCP 连接，这个连接相当于通道，在这之后其他数据包也会使用通道传输数据
    
#### 2. 传输层的处理

    了描述信息能准确的到达另一方，使用 TCP 协议来进行描述 TCP 会根据应用的指示，负责建立连接、发送数据和断开连接
    
    TCP 会在应用数据层的前端附加一个 TCP 首部字段，TCP 首部包含了源端口号 和 目的端口号，
    这两个端口号用于表明数据包是从哪里发出的，需要发送到哪个应用程序上
    
#### 3. 网络层的处理
    
    网络层主要负责处理数据包的是 IP 协议，IP 协议将 TCP 传过来的 TCP 首部和数据结合当作自己的数据，
    并在 TCP 首部的前端加上自己的 IP 首部， IP 首部包含目的和源地址，紧随在 IP 首部的还有用来判断后面是 TCP 还是 UDP 的信息
    
#### 4. 通信链路层的处理

    经由 IP 传过来的数据包，以太网会给数据附上以太网首部并进行发送处理。以太网首部包含接收端的 MAC 地址、
    发送端的 MAC 地址以及标志以太网类型的以太网数据协议
    
### 完整处理：
   
   ![avatar](https://mmbiz.qpic.cn/mmbiz_png/A3ibcic1Xe0iaTicuU6kBxkISjlPjd8lZLl4IyaULRwFfRLzkR0vzovAfoe8aIJf6rKljtb276ya14bKxovEckticeg/640)
   
    数据包经过每层后，该层协议都会在数据包附上包首部，一个完整的包首部图如下所示
   
   ![avatar](https://mmbiz.qpic.cn/mmbiz_png/A3ibcic1Xe0iaTicuU6kBxkISjlPjd8lZLl4oicgLcibARhfxUxpyXsyYELOLQJTqZSEP2A8K21WfwgpTXWyQPmtrAxA/640)

# HTTP(超文本传输协议)
## 参考文档：https://mp.weixin.qq.com/s/qzzEgRpt9f-UlTLnWGrJEw

## HTTP 基本概念详情
    HTTP的名字「超文本协议传输」，它可以拆成三个部分：1. 超文本 2. 传输 3. 协议
    
    1. 「协议」
            HTTP 是一个用在计算机世界里的协议。它使用计算机能够理解的语言确立了一种计算机之间交流通信的规范
            以及相关的各种控制和错误处理方式（行为约定和规范）
    2. 「传输」
            HTTP 协议是一个双向协议, 专门用来在两点之间传输数据的约定和规范
            
    3. 「超文本」
            它就是超越了普通文本的文本，它是文字、图片、视频等的混合体最关键有超链接，能从一个超文本跳转到另外一个超文本
            
    HTTP 是一个在计算机世界里专门在「两点」之间「传输」文字、图片、音频、视频等「超文本」数据的「约定和规范」
    
    
 ## HTTP 常见的状态码
        类别                        具体含义                                      常见状态码
        
        1xx                         提示信息，是协议处理中的一种中间状态
        2xx                         成功,报文已收到并被正确处理                     200, 204, 206
        3xx                         重定向,资源位置发生变动,需重发请求              301,  302, 304
        4xx                         客户端错误,请求报文有误                         400, 403, 404
        5xx                         服务器错误,服务器处理请求时发生错误              500, 501, 502, 503
        
       「200 OK」是最常见的成功状态码，表示一切正常
       「204 No Content」也是常见的成功状态码，与 200 OK 基本相同，但响应头没有 body 数据
       「206 Partial Content」是应用于 HTTP 分块下载或断电续传，表示响应返回的 body 数据并不是资源的全部，而是其中的一部分
       「301 Moved Permanently」表示永久重定向，说明请求的资源已经不存在了，需改用新的 URL 再次访问
       「302 Moved Permanently」表示临时重定向，说明请求的资源还在，但暂时需要用另一个 URL 来访问
       「304 Not Modified」不具有跳转的含义，表示资源未修改，重定向已存在的缓冲文件，也称缓存重定向，用于缓存控制
       「400 Bad Request」表示客户端请求的报文有错误，但只是个笼统的错误。
       「403 Forbidden」表示服务器禁止访问资源，并不是客户端的请求出错。
       「404 Not Found」表示请求的资源在服务器上不存在或未找到，所以无法提供给客户端
       「500 Internal Server Error」 笼统通用的错误码，服务器发生了错误
       「501 Not Implemented」表示客户端请求的功能还不支持
       「502 Bad Gateway」通常是服务器作为网关或代理时返回的错误码，表示服务器自身工作正常，访问后端服务器发生了错误
       「503 Service Unavailable」表示服务器当前很忙，暂时无法响应服务器
  
  
## HTTP请求
    请求由客户端向服务器端发出, 由4部分内容组成：
        请求头\r\n\r\n请求体
    
        1. 请求方法(Request Method)
                GET	         请求指定的页面信息，并返回实体主体。
                HEAD	     类似于 GET 请求，只不过返回的响应中没有具体的内容，用于获取报头
                POST	     向指定资源提交数据进行处理请求（例如提交表单或者上传文件)
                PUT	         从客户端向服务器传送的数据取代指定的文档的内容
                PATCH	     是对 PUT 方法的补充，用来对已知资源进行局部更新
                DELETE	     请求服务器删除指定的页面。
                CONNECT	     把服务器当作跳板机
                OPTIONS	     允许客户端查看服务器的性能。
                TRACE	     回显服务器收到的请求，主要用于测试或诊断。
        
        2. 请求头(Request Headers)
                协议头	                    说明	                                    示例
                
                Accept	               可接受的响应内容类型	                        Accept: text/plain
                Accept-Charset         可接受的字符集                                Accept-Charset: utf-8
                Accept-Encoding	       可接受的响应内容的编码方式	                Accept-Encoding: gzip, deflate
                Accept-Language	       可接受的响应内容语言列表                      Accept-Language: zh-CN
                Connection	           客户端想要优先使用的连接类型	                Connection: keep-alive
                                                                                    Connection: Upgrade
                Cookie
                Host                    表示服务器的域名以及服务器所监听的端口号      host: www.itbilu.com:80
                Content-Length          以8进制表示的请求体的长度                    Content-Length: 348
                Referer                 标识这个请求是哪个页面发来的                 Referer: http://itbilu.com/nodejs
                User-Agent              浏览器的身份标识字符串
                Content-Type            具体请求中的媒体类型信息                    Content-Type: application/x-www-form-urlencoded
                
        3. 空行(\r\n)
        4. 请求体(Request Body)    
        
        Content-Type 与 POST 提交数据方式的关系
         
                    Content-Type                                        提交数据方式
                application/x-www-form-urlencode                        表单数据(将FORM表单数用&连接，组装成k1=v1&k2=v2格式字符串提交)
                multipart/form-data                                     表单文件上传(将FORM表单数据使用指定的分割字符(boundary)组装成一个字符串提交，可用于提交二进制数据，如上传文件)
                application/json                                        告诉服务端POST提交的是JSON字符串
                text/xxx                                                 文本数据
                
## HTTP响应
    响应由服务器向客户端端发出, 由4部分内容组成：
        响应头\r\n\r\n响应体
        
        1. 响应状态码(Response Status Code)
        
        2. 响应头(Response Headers)
                协议头	                    说明	                                    示例
                
                Allow	                    服务器支持哪些请求方法	                    Allow: GET, HEAD
                Content-Encoding	        响应内容的编码方式	                        Content-Encoding: gzip, deflate
                Content-Length              内容长度                                     Content-Length: 68
                Content-Language	        响应内容所使用的语言                         Content-Language: zh-cn
                Content-Type                当前内容的MIME类型                           Content-Type: text/html; charset=utf-8
                Date：                      此条消息被发送时的日期和时间                  Date: Tue, 15 Nov 1994 08:12:31 GMT
                Expires                     响应过期时间                                 Expires: Thu, 01 Dec 1994 16:00:00 GMT
                Set-Cookie                  告诉浏览器需要将此内容放到Cookie中            Set-Cookie: UserID=itbilu; Max-Age=3600; Version=1
                Server	                    服务器的名称	                                 Server: nginx/1.6.3
        3. 空行(\r\n\r\n)  
        4. 响应体(Response  Body)
	
## application/xml 、 text/xml、text/html、text/plain的区别

    1、text/html是html格式的正文
    2、text/plain是无格式正文
    3、text/xml忽略xml头所指定编码格式而默认采用us-ascii编码
    4、application/xml会根据xml头指定的编码格式来编码
 
## GET和POST请求的不同

    GET和POST本质上就是TCP链接，并无差别。但是由于HTTP的规定和浏览器/服务器的限制，导致他们在应用过程中体现出一些不同

### GET和POST本质上没有区别：
        
    GET和POST是HTTP协议中的两种发送请求的方法，HTTP的底层是TCP/IP， 所以GET和POST的底层也是TCP/IP，也就是说，
    GET/POST都是TCP链接。GET和POST能做的事情是一样一样的。你要给GET加上request body，给POST带上url参数，技术上是完全行的通的
    
    TCP就像汽车，我们用TCP来运输数据，但是如果路上跑的全是看起来一模一样的汽车，那这个世界看起来是一团混乱，
    送急件的汽车可能被前面满载货物的汽车拦堵在路上，整个交通系统一定会瘫痪。为了避免这种情况发生，交通规则HTTP诞生了
    
    HTTP给汽车运输设定了好几个服务类别，有GET, POST, PUT, DELETE等等，HTTP规定，当执行GET请求的时候，
    要给汽车贴上GET的标签（设置method为GET），而且要求把传送的数据放在车顶上（url中）以方便记录。
    如果是POST请求，就要在车上贴上POST的标签，并把货物放在车厢里。
    当然，你也可以在GET的时候往车厢内偷偷藏点货物，但是这是很不光彩；也可以在POST的时候在车顶上也放一些数据，让人觉得傻乎乎的。
    
    不同的浏览器（发起http请求）和服务器（接受http请求）就是不同的运输公司。虽然理论上，你可以在车顶上无限的堆货物（url中无限加参数）
    
    但是运输公司可不傻，装货和卸货也是有很大成本的，他们会限制单次运输量来控制风险，数据量太大对浏览器和服务器都是很大负担。
    （大多数）浏览器通常都会限制url长度在2K个字节，而（大多数）服务器最多处理64K大小的url。超过的部分，恕不处理
    
    如果你用GET服务，在request body偷偷藏了数据，不同服务器的处理方式也是不同的，有些服务器会帮你卸货，
    读出数据，有些服务器直接忽略，所以，虽然GET可以带request body，也不能保证一定能被接收到哦
   
    
### 应用过程上的区别：

    1. GET把参数包含在URL中，POST通过request body传递参数 GET的参数是明文传输，不安全
    2. GET请求会被浏览器主动cache，而POST不会
    3. GET请求只能进行url编码，而POST支持多种编码方式
    4. GET请求在URL中传送的参数是有长度限制的（2048），而POST没有
    5. 对参数的数据类型，GET只接受ASCII字符，而POST没有限制  

### GET和POST 重大区别：

    GET产生一个TCP数据包；POST产生两个TCP数据包。
    
    对于GET方式的请求，浏览器会把http header和data一并发送出去，服务器响应200
    对于POST，浏览器先发送header，服务器响应100 continue，浏览器再发送data，服务器响应200 ok
    
    POST需要两步，时间上消耗的要多一点，看起来GET比POST更有效 但是 在网络环境好的情况下，发一次包的时间和发两次包的时间差别基本可以无视。
    而在网络环境差的情况下，两次包的TCP在验证数据包完整性上，有非常大的优点。并不是所有浏览器都会在POST中发送两次包，Firefox就只发送一次


 ## HTTP 特性
    HTTP 最凸出的优点:
        1. 简单
            HTTP 基本的报文格式就是 header + body，头部信息也是 key-value 简单文本的形式
          
        2. 灵活和易于扩展
            HTTP协议里的各类请求方法、URI/URL、状态码、头字段等每个组成要求都没有被固定死，都允许开发人员自定义和扩充
            
        3. 应用广泛和跨平台
        
     HTTP 的缺点:
         1. 无状态、明文传输
                解决方案： 用 Cookie 技术
         2. 不安全
                解决方案：使用HTTPS, HTTPS 也就是在 HTTP 与 TCP 层之间增加了 SSL/TLS 安全传输层
                
# HTTPS 基本概念
## 参考文档：https://mp.weixin.qq.com/s/qzzEgRpt9f-UlTLnWGrJEw
## 参考文档：https://zhuanlan.zhihu.com/p/27395037

## HTTP 与 HTTPS 有哪些区别？
    1. HTTP 是超文本传输协议，信息是明文传输，存在安全风险的问题。
       HTTPS 则解决 HTTP 不安全的缺陷，在 TCP 和 HTTP 网络层之间加入了 SSL/TLS 安全协议，使得报文能够加密传输。
    
    2. HTTP 连接建立相对简单, TCP 三次握手之后便可进行 HTTP 的报文传输。而 HTTPS 在 TCP 三次握手之后，还需进行 SSL/TLS 的握手过程，才可进入加密报文传输。
    
    3. HTTP 的端口号是 80，HTTPS 的端口号是 443。
    
    4. HTTPS 协议需要向 CA（证书权威机构）申请数字证书，来保证服务器的身份是可信的。
    
 ## HTTPS 解决了 HTTP 的哪些问题？
    HTTP 由于是明文传输，所以安全上存在以下三个风险：

        窃听风险，比如通信链路上可以获取通信内容，用户号容易没。
        
        篡改风险，比如强制入垃圾广告，视觉污染，用户眼容易瞎。
        
        冒充风险，比如冒充淘宝网站，用户钱容易没。
        
## HTTPS 是如何解决上面的三个风险的？
    混合加密的方式实现信息的机密性，解决了窃听的风险。
    
    摘要算法的方式来实现完整性，它能够为数据生成独一无二的「指纹」，指纹用于校验数据的完整性，解决了篡改的风险。
    
    将服务器公钥放入到数字证书中，解决了冒充的风险。
    
# 完整的HTTP请求与响应
## HTTP请求和响应步骤
    1. 建立TCP连接------>2.浏览器向服务器发送请求命令-------->3.浏览器发送请求头信息------>4.服务器应答 ------->
    5.服务器发送应答头信息------>6.服务器向浏览器发送数据-------->7.服务器关闭TCP连接
    
## 浏览器中输入URL到返回页面的全过程
    1. 根据域名，进行DNS域名解析；
    2. 拿到解析的IP地址，建立TCP连接；
    3. 向IP地址，发送HTTP请求；
    4. 服务器处理请求；
    5. 返回响应结果；
    6. 关闭TCP连接；
    7. 浏览器解析HTML；
    8. 浏览器布局渲染；
    
## DNS解析: https://zhuanlan.zhihu.com/p/79350395
    将域名转称IP地址
    
    解析过程：
        浏览器输入地址, 先去浏览器的dns缓存里头查询, dns缓存中没有,浏览器这个进程去调操作系统某个库里的gethostbyname函数
        gethostbyname函数在试图进行DNS解析之前首先检查域名是否在本地 Hosts里, 如果没找到再去DNS服务器上查
        
     
    DNS是如何做域名解析的(解析www.tmall.com的域名)：
        www.tmall.com对应的真正的域名为www.tmall.com.。末尾的.称为根域名，因为每个域名都有根域名，因此我们通常省略
        根域名的下一级，叫做"顶级域名"，比如.com、.net；
        再下一级叫做"次级域名"，比如www.tmall.com里面的.tmall，这一级域名是用户可以注册的
        再下一级是主机名（host），比如www.tmall.com里面的www，又称为"三级域名"
        
        解析流程就是分级查询
            1. 先在本机的DNS里头查，如果有就直接返回了
            2. 本机DNS里头发现没有，就去根服务器里查。根服务器发现这个域名是属于com域，
               因此根域DNS服务器会返回它所管理的com域中的DNS服务器的IP地址
            3. 本机的DNS接到又会向com域的DNS服务器发送查询消息。com域中也没有www.tmall.com这个域名的信息，
               和刚才一样，com域服务器会返回它下面的tmall.com域的DNS服务器的IP地址。

            以此类推，只要重复前面的步骤，就可以顺藤摸瓜找到目标DNS服务器
        
    为什么域名解析用UDP协议?
        因为UDP快啊！UDP的DNS协议只要一个请求、一个应答就好了。而使用基于TCP的DNS协议要三次握手、发送数据以及应答、四次挥手。
       但是UDP协议传输内容不能超过512字节。不过客户端向DNS服务器查询域名，一般返回的内容都不超过512字节，用UDP传输即可。
      
    为什么区域传送用TCP协议？
        TCP协议可靠性好啊！从主DNS上复制内容啊，不用不可靠的UDP, 因为TCP协议传输的内容大啊，用最大只能传512字节的UDP协议
        万一同步的数据大于512字节，会出现问题
 # TCP相关
 ## 参考文档：https://mp.weixin.qq.com/s/pqUFksNEwT9UWDpcKdGpQg
 
 ## TCP的标志位 
        
        SYN 置1时用来发起一个连接。
        ACK 置1时表示确认号合法，为0的时候表示数据段不包含确认信息，确认号被忽略。
        FIN 置1时表示完成发送任务。用来释放连接，表明发送方已经没有数据发送了
        URG 紧急数据标志  表示本数据包中包含紧急数据。用来保证TCP连接不被中断，并督促中间层设备尽快处理这些数据
        PSH 数据包到达接收端后,立即传给应用程序，而不必等到缓冲区满时才传送。
        RST 置1时重建连接。如果接收到RST位时候，通常发生了某些错误。
        
## TCP三次握手
    1.客户端发送SYN（SEQ=x）报文给服务器端，进入SYN_SEND状态。
	    SYN: 同步字符,是TCP/IP建立连接时使用的握手信号.
	    在发送信息或回答之前，都要先发送同步字符，用以实现或保持发送站和接收站之间的同步
	
	2.服务器端收到SYN报文，回应一个SYN （SEQ=y）+ ACK(ACK=x+1）报文，进入SYN_RECV状态。
	    ACK:确认字符，表示发来的数据已确认接收无误。
	        接收站对所收到的报文进行检查，若未发现错误，便向发送站发出确认回答ACK，表明信息已被正确接收，并准备好接收下一份报文
	    NAK:否认字符
	
	3.客户端收到服务器的SYN+ACK包，回应一个ACK(ACK=y+1）报文，进入Established（TCP连接成功）状态。
	
	三次握手完成，TCP客户端和服务器端成功地建立连接，可以开始传输数据了
	
## TCP四次挥手流程

        由于TCP连接是全双工的，因此每个方向都必须单独进行关闭.当一方完成它的数据发送任务后就能发送一个FIN来终止这个方向的连接。
		收到一个 FIN只意味着这一方向上没有数据流动，一个TCP连接在收到一个FIN后仍能发送数据
		
		1. TCP客户端发送一个FIN(结束连接)，用来关闭客户到服务器的数据传送。
		        客户端发送一个FIN=M ,客户端进入FIN_WAIT_1状态。意思是说"我客户端没有数据要发给你了"，
		        但是如果你服务器端还有数据没有发送完成，则不必急着关闭连接，可以继续发送数据。
        
        2. 服务器收到这个FIN，它发回一个ACK
                服务器端收到FIN后，先发送ack=M+1，告诉客户端，你的请求我收到了，但是我还没准备好，请继续你等我的消息。
                服务端进入CLOSE_WAIT(关闭等待)状态，这个时候客户端就进入FIN_WAIT_2 状态，继续等待服务器端的FIN报文。
        
        3. 服务器关闭客户端的连接，发送一个FIN给客户端。
                当服务器端确定数据已发送完成，则向客户端发送FIN=N报文，告诉客户端，好了，我这边数据发完了，准备好关闭连接了。
                服务器端进入LAST_ACK(最后确认)状态
        
        4. 客户端发回ACK报文确认
                客户端收到FIN=N报文后，就知道可以关闭连接了，但是他不相信网络，怕服务器端不知道要关闭，
                所以发送ack=N+1后进入TIME_WAIT(时间等待)状态，如果Server端没有收到ACK则可以重传。
                服务器端收到ACK后，就知道可以断开连接了,进入CLOSED状态。客户端等待了2MSL后依然没有收到回复，则证明服务器端已正常关闭，
                那好，我客户端也可以关闭连接了,进入CLOSED状态。

# Cookie，Session，Token
## 参考文档： https://zhuanlan.zhihu.com/p/63061864
