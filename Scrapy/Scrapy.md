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
