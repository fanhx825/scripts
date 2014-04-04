#!/usr/bin/env python
#encoding=utf8
"""
@作者：范洪星
@描述：测试redis主从复制以及内存限制
@时间：2014年3月25日 星期二 下午
"""

import redis
import time
from p_mysqldb import *

sql = "SELECT  p1.ID AS picId,p1.PIC_TYPE,p1.colorid,p2.COLOR_NAME FROM pics p1 \
		LEFT JOIN \
		model_color_conf p2 \
		ON p1.colorid=p2.id WHERE p1.colorid <> 0"

host = "10.10.77.6"
user = "wanjiang"
passwd = "wanjiang0310"
port = 3306
dbname = "auto_warehouse"
charset = "utf8"

##连接master节点
def getRedis():
	r = redis.Redis(host="10.10.83.20",port=6380,db=1)
	return r

if __name__ == "__main__":
	
	conn = getConn(host,user,passwd,port,dbname,charset)
	cursor = getCursor(conn)
	cursor.execute(sql)

	r = getRedis()

	for (picId,picType,picColorId,picColorName) in cursor.fetchall():
		print "%s\t%s\t%s\t%s" %(picId,picType,picColorId,picColorName)
		r.rpush(picId,picType)
		r.rpush(picId,picColorId)
		r.rpush(picId,picColorName)
		#time.sleep(1)

	cursor.close()
	conn.close()
	
