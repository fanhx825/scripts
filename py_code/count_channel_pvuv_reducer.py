#!/usr/bin/env python
#encoding=utf8
"""
作者：范洪星
描述：统计的reduce
时间：2014年4月3日 星期四 下午
总结：
"""

import sys

hash_pv = {} #value是int类型的pv值
hash_uv = {} #value是list类型的suv值
hash_change = {} #value是list类型的suv 转化率

for line in sys.stdin:
	line = line.strip()
	cols = line.split("\t")

	length = len(cols)

	if length == 4: #统计pv uv
		pv = int(cols[2])
		suv = cols[3]
		key = "\t".join(cols[0:2])
		
		hash_pv[key] = hash_pv.get(key,0) + pv #pv值
		
		if key in hash_uv:
			if suv not in hash_uv[key]:
				hash_uv[key].append(suv)
		else:
			hash_uv[key] = [suv]
	elif length == 3: #统计转化率
		suv = cols[2]
		key = "\t".join(cols[0:2])
		if key in hash_change:
			if suv not in hash_change[key]:
				hash_change[key].append(suv)
		else:
			hash_change[key] = [suv]

for (k,v) in hash_pv.items():
	print "pv\t%s\t%d" %(k,v)

for (k,v) in hash_uv.items():
	print "uv\t%s\t%d" %(k,len(v))

for (k,v) in hash_change.items():
	print "change\t%s\t%d" %(k,len(v))

