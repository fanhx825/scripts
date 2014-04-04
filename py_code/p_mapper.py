#! /usr/bin/env python
#encoding=utf8
"""
@作者	范洪星
@描述	计算日志中有多少无效的pv
@日期	2014年3月21日 星期五 上午
"""
import sys
import re

pattern = re.compile(r"wmh-auto-tab")

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	key = cols[5]
	match = pattern.search(key)

	if match:
		print "%s\t%s" %("yes",1)
	else:
		print "%s\t%s" %("no",1)
