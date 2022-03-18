### 1、新建项目：scrapy startproject xjb

### 2、目录结构
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
       
### 2、执行流程
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
           
