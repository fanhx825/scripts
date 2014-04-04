#! /usr/bin/env python
#encoding=utf8
"""
@作者	范洪星
@描述	统计无效PV数
@日期	2014年3月21日 星期五 上午
"""

import sys

hash_code = {} #stream方式不会形成java的迭代器，故采用此方法

for line in sys.stdin: #一个个yes\t1 形式的
	line = line.strip()
	cols = line.split("\t")
	key = cols[0]

	if key in hash_code:
		hash_code[key] = hash_code.get(key,0) + int(cols[1])
	else:
		hash_code[key] = int(cols[1])

##reducer打印结果
for (k,v) in hash_code.items():
	print "%s\t%s" %(k,v)
