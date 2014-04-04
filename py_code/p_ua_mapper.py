#!/usr/bin/env python
#encoding=utf8
"""
@作者：范洪星
@描述：计算全站ua数
@时间：2014年3月24日 星期一 上午
"""

import sys

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")
	key = cols[3]
	print "%s\t%s" % (key,1)
