#!/usr/bin/env python
#encoding=utf8
"""
@作者：范洪星
@描述：统计全站ua值，reducer部分
@时间：2014年3月24日 星期一 下午
"""

import sys

hash_ua = {}

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	key = cols[0]
	value = int(cols[1])
	if key in hash_ua:
		hash_ua[key] = hash_ua.get(key,0) + value
	else:
		hash_ua[key] = value

for (k,v) in hash_ua.items():
	print "%s\t%s" %(k,v)
