#! /usr/bin/python
#encoding=utf8
"""
@Author:范洪星
@depict:将图片ID打上标签
@since：2014年3月20日 星期四 中午
"""

import MySQLdb
import sys

##直接打印中文不用加这两句，但是输出重定向需要加
reload(sys)
sys.setdefaultencoding('utf8')

##获取数据库连接
def getConn(host,user,passwd,dbname,port,charset):
	try:
		conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=dbname,port=port,charset=charset)
	except MySQLdb.Error,e:
		print "Error: %s" % e
		conn.close()
	return conn

##获取操作对象
def getCursor(conn):
	try:
		cursor = conn.cursor()
	except MySQLdb.Error,e:
		print "Error: %s" % e
	return cursor

hash_color = {} #装载图片信息

sql_pic = "SELECT ID AS picId,MODELID,PIC_TYPE,colorid FROM pics WHERE colorid <> 0" #图片信息
sql_color = "SELECT ID AS colorId,MODEL_ID,COLOR_NAME FROM model_color_conf"

if __name__ == "__main__":
	conn = getConn("10.10.77.6","wanjiang","wanjiang0310","auto_warehouse",3306,"utf8")
	cursor = getCursor(conn)
	
	##执行颜色操作
	cursor.execute(sql_color)
	for (colorId,MODEL_ID,COLOR_NAME) in cursor.fetchall():
		#print "%s\t%s\t%s\t%s" % (picId,MODELID,PIC_TYPE,colorid)
		hash_color[str(colorId)] = COLOR_NAME
		#hash_color[str(colorId) + "\t" + str(MODEL_ID)] = COLOR_NAME
	##执行图片操作
	cursor.execute(sql_pic)

	for (picId,MODELID,PIC_TYPE,colorid) in cursor.fetchall():
		key = str(colorid)
		##if条件转化图片类型
		if 1000 == PIC_TYPE: #类型一定要一致
			PIC_TYPE = "外观"
		elif 2000 == PIC_TYPE:
			PIC_TYPE = "内饰"
		elif 3000 == PIC_TYPE:
			PIC_TYPE = "底盘/动力"
		elif 5000 == PIC_TYPE:
			PIC_TYPE = "评测"
		elif 6000 == PIC_TYPE:
			PIC_TYPE = "图解"
		elif 7000 == PIC_TYPE:
			PIC_TYPE = "改装"
		elif 8000 == PIC_TYPE:
			PIC_TYPE = "官方"
		elif 9000 == PIC_TYPE:
			PIC_TYPE = "其他"
		##打印结果
		if key in hash_color:
			print "%s\t%s\t%s\t%s\t%s" % (picId,MODELID,PIC_TYPE,colorid,hash_color[key])
		else:
			print "%s\t%s\t%s\t%s\t%s" % (picId,MODELID,PIC_TYPE,colorid,"nothing")
	##关闭持有连接
	cursor.close()
	conn.close()
