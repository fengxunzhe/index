### 方法一、 1、点击设置 --- >> 系统 --->> 远程桌面 -->> 开    2、此电脑 ---  属性  --- 远程设置  -- 允许远程   3、ok
###### 远程不上的原因： 1、网络能否ping通   2、是否启用远程连接功能(上面这个)  3、防火墙是否关闭  4、windows防护墙--高级设置--入站规则--开启文件打印和共享(回显请求-ICMPv4-In)--ping网络

### 方法二、Server实现被多人同时远程(多用户登录)
###### windows server 默认只允许2个用户可以同时远程桌面，多了则不可以登录
###### 参考：https://www.bilibili.com/video/BV175411b7De/?spm_id_from=333.788.recommend_more_video.3

###### 1、添加远程桌面服务
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/44.png)
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/44.png)

其他一路next;重启生效
###### 2、

