### 一、新建项目：scrapy startproject xjb

### 二、目录结构
      xjb---
        ├── xjb
        │   ├── __init__.py
        │   ├── items.py
        │   ├── middlewares.py
        │   ├── pipelines.py
        │   ├── __pycache__
        │   ├── settings.py
        │   └── spiders
        │       ├── __init__.py
        │       └── __pycache__
        └── scrapy.cfg      

       scrapy.cfg ： 项目基础设置文件，设置爬虫启用的功能，如并发，管道文件等，需要在基础设置文件设置
       tems.py 文件 ：此文件俗称模型文件，就是存放字段的文件，定义字段名称，以自己的任意形式存取数据
       pipelines.py 管道文件 ：def process_item为固定写法，当数据交给管道文件处理时，在此文件下
       
### 三、执行流程
##### 2.1、新建项目

            D:\ast-hook-for-js-RE-master>cd demo   

            D:\ast-hook-for-js-RE-master\demo>scrapy startproject myspilder
            New Scrapy project 'myspilder', using template directory 'C:\Users\L4000069\AppData\Roaming\Python\Python37\site-packages\scrapy\templates\project', created in:
                D:\ast-hook-for-js-RE-master\demo\myspilder

            You can start your first spider with:
                cd myspilder
                scrapy genspider example example.com
           主要进入到新建文件夹demo下面，新建一个名为myspilder的项目(scrapy startproject myspilder) ，此时的项目结构为
           
           |Demo
           |  |myspilder  
           |  ├── myspilder
           |  │   ├── __init__.py
           |  │   ├── items.py
           |  │   ├── middlewares.py
           |  │   ├── pipelines.py
           |  │   ├── __pycache__
           |  │   ├── settings.py
           |  │   └── spiders
           |  │       ├── __init__.py
           |  │       └── __pycache__
           |  └── scrapy.cfg      
           |-------------------------------------
##### 2.2、新建项目文件   

           下面会提示如何开始编写You can start your first spider with
           第一步:cd myspilder，通过以下可以看出是进入最上层的myspilder文件夹
            2022/03/18  12:48    <DIR>          myspilder
            2022/03/18  12:48               261 scrapy.cfg
            
           第二步:scrapy genspider example example.com，新建一个爬虫文件，此时的目录结构
           Demo
           |  |myspilder  
           |  ├── myspilder
           |  │   ├── __init__.py
           |  │   ├── items.py
           |  │   ├── middlewares.py
           |  │   ├── pipelines.py
           |  │   ├── __pycache__
           |  │   ├── settings.py
           |  │   └── spiders
           |  │       ├── __init__.py
           |  |       |-- [example.py]
           |  │       └── __pycache__
           |  └── scrapy.cfg      
           |-------------------------------------
           问题1、我们cd的是最上层的myspilder文件夹，为什么建立的文件在第二个myspiler的spilders文件夹中
           
                 答：scrapy genspider example example.com创建文件会首先进入和第一层同级别的scrapy.cfg中的settings代码，而该代码又指向第二个myspilder.settings文件;
                 [settings]
                        default = myspilder.settings
                 在myspilder.settings.py文件 中 指向的是 第二次myspilder.spiders文件中，所以建立的文件夹在spiders中
                        SPIDER_MODULES = ['myspilder.spiders']
                        NEWSPIDER_MODULE = 'myspilder.spiders'
           
           问题2、scrapy genspider example example.com的含义
           
                  D:\ast-hook-for-js-RE-master\demo\myspilder>scrapy genspider example example.com
                  Created spider 'example' using template 'basic' in module:
                  myspilder.spiders.example
           
                 答：genspider用于生成爬虫，与startproject不同的是，它只是生成爬虫模块文件，而startproject是生成整个scrapy项目。默认使用basic模板，
                 使用-l参数可以查看所有可用的模板

                  scrapy genspider -l 查看scrapy创建爬虫文件可用的母版
                        Available templates: 母版说明 　
                               basic　　 　　创建基础爬虫文件
                               crawl　　　　 创建自动爬虫文件 　　
                               csvfeed　　 创建爬取csv数据爬虫文件
                               xmlfeed　　　 创建爬取xml数据爬虫文件
                               
                     example 是生成的文件example.py，也是项目的唯一识别码
                     example.com 是要爬取的域名
                  ---------------------------------   
                  scrapy genspider test  baidu.com   对应的test.py文件   
                  ---------------------------------   
                  class TestSpider(scrapy.Spider):
                      name = 'test'
                      allowed_domains = ['baidu.com']
                      start_urls = ['http://baidu.com/']
                     
##### 2.3、新建爬虫文件example.py分析
            import scrapy
            
            class ExampleSpider(scrapy.Spider): # 继承scrapy.Spider方法
                name = 'example'  # 项目启动的唯一识别码，多个项目的话对应name启动
                allowed_domains = ['example.com'] # 允许爬取的
                start_urls = ['http://example.com/']  # 项目启动首先爬取的

                def parse(self, response):  # respon接受返回的内容
                    pass
         
##### 2.4、项目启动
            scrapy crawl example   项目启动的唯一识别码 启动项目
            scrapy crawl test
            
##### 2.5、测试
            新建两个爬虫文件
            scrapy genspider example example.com
            scrapy genspider test  baidu.com
![imag](https://github.com/fengxunzhe/index/blob/main/Scrapy/img/test01.png)           

### 四、Scrapy项目文件解析

##### 4.1、settings文件
            --  BOT_NAME = 'myspilder'
            
            --  SPIDER_MODULES = ['myspilder.spiders'] --->>>scrapy crawl test爬虫执行首先查找该列表中是否存在ID为test的py文件           
                  如：scrapy genspider test baidu.com  会从SPIDER_MODULES列表中找爬虫文件是否存在，此处不存在，报错
                      SPIDER_MODULES = ['myspilder.spiders','myspilder.Testspiders'] ，此处存在，正常运行
            
            --  NEWSPIDER_MODULE = 'myspilder.Testspiders'-->>> 使用genspider命令创建的文件夹存放在哪个路径     
                  如：scrapy genspider test baidu.com  创建的test.py文件在Testspiders下面
![imag](https://github.com/fengxunzhe/index/blob/main/Scrapy/img/test02.png)   

            --  USER_AGENT = 'myspilder (+http://www.yourdomain.com)'   # USER_AGENT 参数
            
            --  ROBOTSTXT_OBEY = True   # 是否遵循robots协议抓取，True只能抓取rebots的数据
            
            --  CONCURRENT_REQUESTS = 32    # 下载器总共最大处理的并发请求数,默认值16
            
            --  DOWNLOAD_DELAY = 3   # 下载延迟
            
            --  CONCURRENT_REQUESTS_PER_DOMAIN = 16   # 每个域名能够被执行的最大并发请求数目，默认值8
            
            --  CONCURRENT_REQUESTS_PER_IP = 16   # 能够被单个IP处理的并发请求数，默认值0，代表无限制
            
            --  COOKIES_ENABLED = False    # 是否支持cookie，cookiejar进行操作cookie，默认开启
            
            --  TELNETCONSOLE_ENABLED = False   # Telnet用于查看当前爬虫的信息，操作爬虫等...使用telnet ip port ，然后通过命令操作
            
            --  DEFAULT_REQUEST_HEADERS = {    # 协议头
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                     'Accept-Language': 'en',
                   }
                   
            --  SPIDER_MIDDLEWARES = {   # 中间件
                      'myspilder.middlewares.MyspilderSpiderMiddleware': 543,
                  }
                  
            --  DOWNLOADER_MIDDLEWARES = { # 下载中间件
                      'myspilder.middlewares.MyspilderDownloaderMiddleware': 543,
                  }
            
            --  ITEM_PIPELINES = {  # 管道
                      'myspilder.pipelines.MyspilderPipeline': 300,
                  }
                  

            --  AUTOTHROTTLE_START_DELAY = 5 # #起始延迟

            --  AUTOTHROTTLE_MAX_DELAY = 60 # 最大延迟

            --  AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  #每秒并发请求数的平均值，不能高于 CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP，
                        调高了则吞吐量增大强奸目标站点，调低了则对目标站点更加”礼貌“
                        #每个特定的时间点，scrapy并发请求的数目都可能高于或低于该值，这是爬虫视图达到的建议值而不是硬限制

            --  AUTOTHROTTLE_DEBUG = False # 调试

            --  HTTPCACHE_ENABLED = True  # 是否启用缓存策略
            
            --  HTTPCACHE_EXPIRATION_SECS = 0   缓存超时时间
            
            --  HTTPCACHE_DIR = 'httpcache'  # 缓存保存路径
            
            --  HTTPCACHE_IGNORE_HTTP_CODES = []  # 缓存忽略的Http状态码
            
            --  HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'     # 缓存存储的插件 
                  
                  
                  



