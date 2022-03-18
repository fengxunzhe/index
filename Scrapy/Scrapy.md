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
