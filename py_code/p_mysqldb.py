#! /usr/bin/python
#encoding=utf8
"""
@作者	范洪星
@描述	抽象出mysql的连接和操作
@时间	2014年3月20日 星期四 下午
@总结	python文件名中不用有"-"
"""

import MySQLdb


##定义数据库连接
def getConn(host,user,passwd,port,dbname,charset):
	conn = None
	try:
		conn = MySQLdb.connect(host=host,user=user,passwd=passwd,port=port,db=dbname,charset=charset)
	except MySQLdb.Error,e:
		print "Error is: %s" % e
	return conn

##定义数据库操作
def getCursor(conn):
	cursor = None
	try:
		cursor = conn.cursor()
	except MySQLdb.Error,e:
		print "Error is: %s" % e
	return cursor

