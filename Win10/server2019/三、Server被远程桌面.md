### 方法一、 1、点击设置 --- >> 系统 --->> 远程桌面 -->> 开    2、此电脑 ---  属性  --- 远程设置  -- 允许远程   3、ok
###### 远程不上的原因： 1、网络能否ping通   2、是否启用远程连接功能(上面这个)  3、防火墙是否关闭  4、windows防护墙--高级设置--入站规则--开启文件打印和共享(回显请求-ICMPv4-In)--ping网络

### 方法二、Server实现被多人同时远程(多用户登录)
###### windows server 默认只允许2个用户可以同时远程桌面，多了则不可以登录
###### 参考：https://www.bilibili.com/video/BV175411b7De/?spm_id_from=333.788.recommend_more_video.3

###### 1、添加远程桌面服务
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/66.png)
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/77.png)

其他一路next;重启生效
###### 2、修改组策略

gpedit.msc --- >>> 计算机配置 --- 管理模板 --- windows组件 --- 远程桌面服务 --- 远程桌面会话主机 --- 连接 --- 限制连接的数量 --- 已启用(勾选),运行最大远程连接数99999
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/88.png)

###### 3、RD授权

control --->>> 管理工具 --- 远程桌面服务 --- 远程桌面授权管理器 --- 激活服务器 --- 公司信息(随便填) --- 一路next ---添加许可证代码 -- 许可证计划(选择企业协议) --- 填信息后勾选完成重建RD信息
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/99.png)
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/100.png)

###### 4、修改组策略

gpedit.msc --- >>> 计算机配置 --- 管理模板 --- windows组件 --- 远程桌面服务 --- 远程桌面会话主机 --- 授权 --- 设置远程桌面授权模式 --- 已启用(勾选)---授权模式(按用户)
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/110.png)

gpedit.msc --- >>> 计算机配置 --- 管理模板 --- windows组件 --- 远程桌面服务 --- 远程桌面会话主机 --- 授权 --- 使用指定的远程桌面许可证服务器 --- 已启用(勾选)---127.0.0.1
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/120.png)

gpedit.msc --- >>> 计算机配置 --- 管理模板 --- windows组件 --- 远程桌面服务 --- 远程桌面会话主机 --- 授权 --- 隐藏有关RD授权。。。 --- 已启用(勾选)

gpedit.msc --- >>> 计算机配置 --- 管理模板 --- windows组件 --- 远程桌面服务 --- 远程桌面会话主机 --- 会花时间限制 ---设置已中断会话时间限制--15分钟
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/120.png)

gpedit.msc --- >>> 计算机配置 --- 管理模板 --- windows组件 --- 远程桌面服务 --- 远程桌面会话主机 --- 会花时间限制 ---设置活动但空闲的远程桌面会话事件限制--15分钟
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/150.png)

###### 5、远程设置
![imag](https://github.com/fengxunzhe/index/blob/main/Win10/130.png)


