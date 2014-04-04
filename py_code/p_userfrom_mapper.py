#!/usr/bin/env python
#encoding=utf8
"""
@作者：范洪星
@描述：统计一个用户是从哪个渠道来的
@时间：2014年3月24日 星期一 下午
"""

import sys
import re

pattern = re.compile(r"wmh-auto-tab")

for line in sys.stdin:
	line = line.strip()
	
	cols = line.split("\t")

	s_time = cols[0]
	s_ua = cols[3]
	s_url = cols[5]
	s_from = cols[8]

	match = pattern.search(s_url)

	if match:
		continue
	key = s_ua + "\t" + s_from + "\t" + s_time
	print "%s\t%s" %(key,1)
