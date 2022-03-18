# scrapy 第一天，爬取豆瓣书名，分页
import scrapy
from bs4 import BeautifulSoup
from cs.items import CsItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=0&type=T']

    def __init__(self):
        print("+==============+")
        super(ExampleSpider, self).__init__()


    def start_requests(self):  # 比parse更底层的方法，默认不显示

        for i in range(20, 100, 20):
            yield scrapy.Request(f"https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={i}&type=T", callback=self.parse)  # 回调parse函数


    def parse(self, response): # 默认执行的方法
        csItems = CsItem()
        resp = BeautifulSoup(response.text, 'lxml')
        titles = resp.select('li.subject-item div.info h2 a')
        for i in titles:
            csItems['title'] = i.text.strip()
            csItems['url'] = i['href']
            print(csItems['title'], csItems['url'])
        pass
