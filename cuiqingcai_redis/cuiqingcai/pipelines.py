# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient
import settings
from items import CuiqingcaiItem

class CuiqingcaiPipeline(object):
    def __init__(self):
        cn=MongoClient('127.0.0.1',27017)
        db=cn[settings.Mongodb_DBNAME]
        self.table=db[settings.Mongodb_DBTable]
    def process_item(self, item, spider):
        if isinstance(item,CuiqingcaiItem):
            try:
                self.table.insert(dict(item))
            except Exception, e:
                pass
            return item



class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('cqcall.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
