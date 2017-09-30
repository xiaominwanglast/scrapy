#coding=utf-8
import redis

host='172.18.5.162'
port=6379
db=2
r=redis.Redis(host=host,port=port,db=db)
print r.lpush('url:start_urls','sdasd:435435')
r.delete('url:start_urls')
'''
#r.flushdb()

for i in range(1,11):
    r.lpush('dingdian:start_urls','http://www.23us.com/class/'+str(i)+'_1.html')
#r.lpush('dingdian:start_urls','http://www.23us.com/quanben/1'

print (r.lrange('dingdian:start_urls',0,-1))
print r.llen('dingdian:start_urls')
#r.move('dingdian:start_urls',1)
'''
#print r.lpop('dingdian:start_urls')
#print r.lrange('dingdian:start_urls',0,-1)
#r.sadd('dingdian:start_urls','http://www.23us.com/class/12_1.html')
#print r.get('dingdian:start_urls')
#r.delete('dingdian:start_urls')
#print r.llen('dingdian:start_urls')