1、参考链接：https://www.jianshu.com/p/13f45e24b1de
  
  大致流程：
    一、安装NodeJS，会自动配置环境；执行命令node -v查看node版本
=    

    二、修改全局依赖包下载路径
=

      默认情况下，我们在执行npm install -g XXXX下载全局包时，这个包的默认存放路径位C:\Users\用户名\AppData\Roaming\npm\node_modules下，可以通过CMD指令npm root -g查看
      C:\Users\liaijie\AppData\Roaming\npm\node_modules
      
      但是有时候我们不想让全局包放在这里，我们可以自定义存放目录,在CMD窗口执行以下两条命令修改默认路径：
      
      npm config set prefix "C:\node\node_global"
      
      npm config set cache "C:\node\node_cache"
      
      或者打开c:\node\node_modules\npm\.npmrc文件，修改如下：

      prefix =C:\node\node_global
      cache = C:\node\node_cache
      
      然后：接下来，使用npm install -g 下载的包 会自动存放到 node_global
                   缓存会自动存到  node_cache 中
                   
    三、下载的包如何在cmd下直接输入快捷命令可以启动
=

      如：anyproxy 默认下载到 node_global 文件夹中，anyproxy.bat是启动文化
      
      此时我们在环境变量中配置PATH 加入C:\node\node_global的路径
      
      就可以实现在cmd下输入anyproxy启动该服务
                        
