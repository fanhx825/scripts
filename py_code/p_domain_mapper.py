#!/usr/bin/env python
#encoding=utf8
"""
@作者	范洪星
@描述	计算各个频道的流量
@时间	2013年3月21日 星期五 下午
"""

import sys
import re

pattern = re.compile(r"wmh-auto-tab")

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	url = cols[5]
	match = pattern.search(url)
	if match:
		continue
	else:
		key = cols[4]
		print "%s\t%s" %(key,1)	
