# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class BaidunewstestSpider(scrapy.Spider):
    name = "baidunewstest"
    allowed_domains = ["news.baidu.com"]
    start_urls = ['http://news.baidu.com/ns?ct=0&pn=0&rn=50&ie=utf-8&tn=newstitle&word=%E5%9C%A8%E7%BA%BF%E6%97%85%E6%B8%B8']
    '''
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse,headers=self.header)
    '''
    def parse(self, response):
        divs=response.xpath('//div[@class="result title"]')
        for div in divs:
            print div.xpath('div[@class="c-title-author"]/text()').extract()

