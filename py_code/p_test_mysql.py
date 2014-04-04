#! /usr/bin/python
#encoding=utf8
"""
@作者	范洪星
@描述	测试p-mysqldb.py
@时间	2014年3月20日 星期四 下午
"""

import sys
from p_mysqldb import * #一定要注意不能使用-符号

##这个本机不能使用localhost
if __name__ == "__main__":
	host = "127.0.0.1"
	user = "root"
	passwd = "mysql"
	dbname = "test"
	port = 3306
	charset = "utf8"

	sql = "SELECT * from test"
	conn = getConn(host,user,passwd,port,dbname,charset)
	cursor = getCursor(conn)
	cursor.execute(sql)
	
	for (a) in cursor.fetchall():
		print a
