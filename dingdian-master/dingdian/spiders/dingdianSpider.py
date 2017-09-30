#coding=utf-8
import scrapy
from scrapy import Request
import os
from ..items import DingdianItem
from scrapy_redis.spiders import RedisSpider

class DingdianSpider(RedisSpider):
    name = 'dingdian'
    redis_key = 'dingdian:start_urls'
    allowed_domains=['23us.com']

    # def __init__(self,*args,**kwargs):
    #     domain=kwargs.pop('domain','')
    #     self.allowed_domains=filter(None,domain.split(','))
    #     super(DingdianSpider,self).__init__(*args,**kwargs)

    def parse2(self,response):
        links = response.xpath('//table/tr/td[1]/a[2]/@href').extract()
        book_names = response.xpath('//table/tr/td[1]/a[2]/text()').extract()
        authors = response.xpath('//table/tr/td[3]/text()').extract()
        wordCounters = response.xpath('//table/tr/td[4]/text()').extract()
        status = response.xpath('//table/tr/td[6]/text()').extract()

        for i in range(len(links)):
            item = DingdianItem()
            item['name'] = book_names[i]
            item['author'] = authors[i]
            item['wordCounter'] = wordCounters[i]
            item['status'] = status[i]
            yield item

    def parse(self, response):
        links=response.xpath('//table/tr/td[1]/a[2]/@href').extract()
        book_names=response.xpath('//table/tr/td[1]/a[2]/text()').extract()
        authors=response.xpath('//table/tr/td[3]/text()').extract()
        wordCounters=response.xpath('//table/tr/td[4]/text()').extract()
        status = response.xpath('//table/tr/td[6]/text()').extract()

        for i in range(len(links)):
            item=DingdianItem()
            item['name']=book_names[i]
            item['author']=authors[i]
            item['wordCounter']=wordCounters[i]
            item['status']=status[i]
            yield item

        lenth=response.xpath('//*[@id="pagelink"]/a[14]/text()').extract()[0]
        lenth=int(lenth)
        try:
            base_url=response.url[:response.url.rindex('_')+1]
            for i in range(2, lenth + 1):
                url = base_url + str(i) + '.html'
                yield Request(url, callback=self.parse2)
        except Exception,e:
            base_url='http://www.23us.com/quanben/'
            for i in range(2, lenth + 1):
                url = base_url + str(i)
                yield Request(url, callback=self.parse2)

