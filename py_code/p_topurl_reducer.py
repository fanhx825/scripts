#!/usr/bin/env python
#encoding=utf8
"""
@作者：范洪星
@描述：计算topurl
@时间：2014年3月24日 星期一 上午
"""

import sys

hash_url = {}

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	key = cols[0]
	value = cols[1]

	if key in hash_url:
		hash_url[key] = hash_url.get(key,0) + int(value)
	else:
		hash_url[key] = int(value)

for (k,v) in hash_url.items():
	print "%s\t%s" %(k,v)
