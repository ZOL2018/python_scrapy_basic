import scrapy
from python_scrapy_basic.items import PythonScrapyBasicItem

class Baidu(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    url = ['https://www.baidu.com/']
    def parse(self, response):
        item = PythonScrapyBasicItem()
        bd = response.xpath("//input[@id='su']/text()").extract()
        item['baidu'] = bd
        yield item