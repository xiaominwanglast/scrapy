#coding=utf-8
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from dingdian import settings

DeclatativeBase=declarative_base()

def db_connect():
    return create_engine(URL(**settings.DATABASE))

def create_table(engine):
    DeclatativeBase.metadata.create_all(engine)

class Book(DeclatativeBase):
    __tablename__='book'
    id=Column(Integer,primary_key=True)
