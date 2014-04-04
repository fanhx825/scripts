#!/usr/bin/env python
#encoding=utf8
"""
@作者：范洪星
@描述：统计用户从哪个渠道过来的
@时间：2014年3月24日 星期一 下午
"""

import sys

hash_from = {}

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")

	s_ua = cols[0]
	s_from = cols[1]
	s_time = int(cols[2])
	s_count = int(cols[3])

	key = s_ua

	if key in hash_from:
		
		pre_value = hash_from.get(key)

		pre_cols = pre_value.split("\t")

		pre_from = pre_cols[0]

		pre_time = int(pre_cols[1])

		pre_count = int(pre_cols[2])

		end_value = s_count + pre_count
		
		if pre_time < s_time:
			hash_from[key] = pre_from + "\t" + str(pre_time) + "\t" + str(end_value)
			continue
		else:
			hash_from[key] = s_from + "\t" + str(s_time) + "\t" + str(end_value)
	else:
		hash_from[key] = s_from + "\t" + str(s_time) + "\t"  + str(s_count)

for (k,v) in hash_from.items():
	print "%s\t%s" %(k,v)
