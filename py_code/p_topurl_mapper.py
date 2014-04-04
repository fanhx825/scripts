#!/usr/bin/env python
#encoding=utf8
"""
@作者：范洪星
@描述：计算topurl
@时间：2014年3月24日 星期一 上午
"""

import sys
import re

pattern = re.compile(r"wmh-auto-tab")

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	key_1 = cols[4] #domain
	key_2 = cols[5] #url
	match = pattern.search(key_2)
	if match:
		continue
	print "%s%s\t%s" %(key_1,key_2,1)
