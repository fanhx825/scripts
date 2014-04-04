#!/usr/bin/env python
#encoding=utf8
"""
作者：范洪星
描述：使用python浏览pub_dimdetails.sh产生的目录
时间：2014年4月1日 星期二 上午
总结：1.os.popen执行shell命令，并返回执行结果。
	  2.日期的转化和加减操作
	  3.字典的处理
"""

import sys
import datetime
import time
import os
import re

#调用系统命令
def popen(cmd):
	pipe = os.popen(cmd)
	return pipe.readlines()

if __name__ == "__main__":
	if len(sys.argv) != 3: #命令行参数
		print "please input 2 args ,first is start date,second is end date..."
		sys.exit(1) #退出程序
	
	#时间的加减运算
	start = datetime.datetime.strptime(sys.argv[1],"%Y%m%d") #打印出的start变量是带时分秒的
	end = datetime.datetime.strptime(sys.argv[2],"%Y%m%d")
	delta = datetime.timedelta(days=1)
	current = start

	#记录值的hash结构
	hash_type = {}

	while current < end:
		cmd = "hadoop dfs -ls /user/autolog/autodc_index/pub_data/pub_dimdetails/" 	#hadoop 命令

		print current.strftime("%Y%m%d")
		
		cmd = cmd + current.strftime("%Y%m%d") + "/*/part*"
		
		content = popen(cmd)
		
		for line in content:
			line = line.strip()
			cols = re.split("\s+",line) #正则分割字符串
			if "pvlog_model" in line: #字符串和字典的查找
				if "pvlog_model" in hash_type:
					hash_type["pvlog_model"][1] += int(cols[4])
				else:
					hash_type["pvlog_model"] = [cols[5] + " " + cols[6],int(cols[4])]
			elif "dealer_order" in line:
				if "dealer_order" in hash_type:
					hash_type["dealer_order"][1] += int(cols[4])
				else:
					hash_type["dealer_order"] = [cols[5] + " " + cols[6],int(cols[4])]
			elif "compare_model" in line:
				if "compare_model" in hash_type:
					 hash_type["compare_model"][1] += int(cols[4])
				else:
					hash_type["compare_model"] = [cols[5] + " " + cols[6],int(cols[4])]
			else:
				print "Not have the things what you want"

		for (k,v) in hash_type.items():
			print k,v[0],v[1]
		hash_type.clear()
		current += delta
