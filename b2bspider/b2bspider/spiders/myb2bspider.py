# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import redis
from ..items import B2BspiderItem
import requests
import re
from bs4 import BeautifulSoup
class Myb2bspiderSpider(scrapy.Spider):

    name = "myb2bspider"
    allowed_domains = ["http://b2b.huangye88.com/"]
    places=['jiangxi','jiangsu']
    business_types=['lipin','fuzhuang']
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    def __init__(self):
        super(Myb2bspiderSpider,self).__init__()
        self.r=redis.Redis(host='172.18.5.162',port=6379,db=0)
    def start_requests(self):
        for place in self.places:
            for business_type in self.business_types:
                url=self.allowed_domains[0]+place+'/'+business_type+'/'
                yield Request(url=url,callback=self.parse,meta={"cookiejar":1,
                                                                'search_place':place+'_'+business_type,'business_type':business_type})
    def parse(self, response):
        rq=requests.get(response.url,headers=self.header)
        bs=BeautifulSoup(rq.text,'lxml')
        try:
            total_business=re.search('\d+',bs.find('div',class_="tit tit2").span.get_text()).group()
        except:
            pass
        else:
            if divmod(int(total_business),20)[1]==0:
                pages=divmod(int(total_business),20)[0]
            else:
                pages=divmod(int(total_business),20)[0]+1
            for page in range(1,pages+1):
                if page==1:
                    url=response.url
                else:
                    url=response.url+'pn'+str(page)+'/'
                print url
           #     yield Request(url=url,callback=self.parse_url,meta={"cookiejar":1,'search_place':response.meta['search_place'],'business_type':response.meta['business_type']})

    def parse_url(self,response):
        print response.url
        dls=response.xpath('//dl[@onmouseover]')
        for dl in dls:
            if dl.xpath('.//h4/a/@href').extract():
                url=dl.xpath('.//h4/a/@href').extract_first()
            else:
                url=None
            if dl.xpath('.//h4/a/@title').extract():
                title=dl.xpath('.//h4/a/@title').extract_first()
            else:
                title=''
            if url:
                yield Request(url=url,callback=self.parse_item,meta={"cookiejar":1,'search_place':response.meta['search_place'],'business_type':response.meta['business_type'],
                                                                     'business_name':title})

    def parse_item(self,response):
       # items=B2BspiderItem()
        items={}
        items['business_body']=response.xpath('//li[@class="contro-num"]/text()').extract_first()
        items['business_place']=response.xpath('//div[@class="l-content"]/ul[2]/li[-1]/text()').extract_first()
        items['business_person']=response.xpath('//div[@class="l-content"]/ul/li[1]/a/text()').extract_first()
        items['business_iphone']=response.xpath('//div[@class="l-content"]/ul/li[3]/text()').extract_first()
        print items['business_body']
        print items['business_place']
        print items['business_person']
        print items['business_iphone']
        items['search_word']=response.meta['search_place']
        items['business_type']=response.meta['business_type']
        items['business_name']=response.meta['business_name']
      #  yield items
