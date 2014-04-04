#!/usr/bin/env python
#encoding=utf8
"""
作者：范洪星
描述：1.计算九大车型，新能源频道，车型大全，精准选车的url的pv和uv以及转化率
时间：2014年4月3日 星期四 下午
总结：
"""

import sys

#type_one=九大车型 type_two=新能源频道 type_three=车型大全 type_four=精选车型
key_value = {
		"db.auto.sohu.com/a00.shtml":"type_one", #微型车
		"db.auto.sohu.com/a0.shtml":"type_one", #小型车
		"db.auto.sohu.com/a.shtml":"type_one", #紧凑型车
		"db.auto.sohu.com/b.shtml":"type_one", #中型车
		"db.auto.sohu.com/c.shtml":"type_one", #中大型车
		"db.auto.sohu.com/luxury.shtml":"type_one", #豪车
		"db.auto.sohu.com/mpv.shtml":"type_one", #MPV
		"db.auto.sohu.com/suv.shtml":"type_one", #SUV
		"db.auto.sohu.com/sportscars.shtml":"type_one", #跑车
		"auto.sohu.com/newenerge/":"type_two", #新能源频道
		"db.auto.sohu.com/":"type_three", #车型库大全，结尾没有“”
		"db.auto.sohu.com":"type_three", #车型库大全，结尾没有“”
		"db.auto.sohu.com/searchterm.sip":"type_four" #精准选车
		}

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	suv = cols[3]
	whole_url = cols[4] + cols[5]
	refer = cols[8]

	if whole_url in key_value:
		print "pv_uv\t%s\t%d\t%s" %(key_value[whole_url],1,suv)
	
	if refer in key_value:
		print "changenum\t%s\t%s" %(key_value[refer],suv)
