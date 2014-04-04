#! /usr/bin/python
#encoding=utf-8
'''
 描述:用于支持12530周数据的报表
 作者:范红星
 时间:2013-11-20 星期三 早上
 总结:1.注意编码问题 2.熟练字典的使用 3.发送邮件写法
'''
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
from email.Header import Header
import smtplib 
import os
import time
import datetime

#-装载文件到字典中-#
def fill(code_file_path):
	code_map = {}; #声明字典
	#使用python的try except finally 结构
	try:
		code_file_handler = open(code_file_path,"r");
		for line in code_file_handler.readlines():
			line = line.strip("\n");
			k_v = line.split("\t");
			code_map[k_v[1]] = k_v[0]; #字典赋值
		return code_map;
	except IOError:
		print("Read code file error");
	finally:
		code_file_handler.close();

#-查询数据库-#
def query(sql):
	try:
		conn = MySQLdb.connect(host="221.204.212.80", user="dba", passwd="dba", db="dw",port=5029);
		cursor = conn.cursor();
		cursor.execute("set NAMES utf8"); #编码问题
		cursor.execute(sql);
		result = cursor.fetchall();
		return result;
	except MySQLdb.Error as e:
		print("MySQL Error %d: %s" %(e.args[0],e.args[1]));
	finally:
		cursor.close();
		conn.close();

#-从字典中转化结果 写入文件中-#
def write(attach_path,result,task_key_value):
	f = open(attach_path,'w');
	f.write("URL" + "\t" + "省份" + "\t" + "运营商" + "\t" + "速度" + "\n");
	for (task,pro,isp,speed) in result:
		f.write(task_key_value[task] + "\t" + pro + "\t" + isp + "\t" + str(speed)+ "\n");
	f.close();

#-发送邮件-#
def sendMail(_from,to,cc,attach_path):
	msg = MIMEMultipart();
	assert type(to) == list; #多人发送的问题弄了很久 要注意
	assert type(cc) == list;
	msg['To'] = COMMASPACE.join(to);
	msg['Cc'] = COMMASPACE.join(cc);
	msg['From'] = _from;
	msg['Subject'] = Header(' 12530 周数据 ','utf-8');
	att = MIMEText(open(attach_path, 'rb').read(), 'base64', 'utf-8');
	att["Content-Type"] = 'application/octet-stream';
	att["Content-Disposition"] = 'attachment; filename="12530.txt"';
	msg.attach(att);

	server = smtplib.SMTP('corp.chinacache.com');
	server.sendmail(_from, to, msg.as_string());
	server.close;
if(__name__ == "__main__"):
	Monday = str(datetime.date.today() - datetime.timedelta(days=7)).replace("-","");
	Tuesday = str(datetime.date.today() - datetime.timedelta(days=6)).replace("-","");
	Wednesday = str(datetime.date.today() - datetime.timedelta(days=5)).replace("-","");
	Thursday = str(datetime.date.today() - datetime.timedelta(days=4)).replace("-","");
	Friday = str(datetime.date.today() - datetime.timedelta(days=3)).replace("-","");
	Saturday = str(datetime.date.today() - datetime.timedelta(days=2)).replace("-","");
	Sunday = str(datetime.date.today() - datetime.timedelta(days=1)).replace("-","");
	
	code_file_path = "./code.ip.20130609.data";
	
	sql = "SELECT task,pro,isp,SUM(speed * 1024 / 8)/SUM(weight) FROM ( \
			SELECT task,pro,isp,SUM(speed) AS speed,SUM(weight) AS weight FROM \
			speed_" + str(Monday) \
			+ " WHERE task='[migupage]' OR task='[miguclient]' OR task='[cailing]' \
				GROUP BY task,pro,isp \
			UNION ALL \
			SELECT task,pro,isp,SUM(speed) AS speed,SUM(weight) AS weight FROM \
			speed_" + str(Tuesday) \
			+ " WHERE task='[migupage]' OR task='[miguclient]' OR task='[cailing]' \
				GROUP BY task,pro,isp \
			UNION ALL \
			SELECT task,pro,isp,SUM(speed) AS speed,SUM(weight) AS weight FROM \
			speed_" + str(Wednesday) \
			+ " WHERE task='[migupage]' OR task='[miguclient]' OR task='[cailing]' \
				GROUP BY task,pro,isp \
			UNION ALL \
			SELECT task,pro,isp,SUM(speed) AS speed,SUM(weight) AS weight FROM \
			speed_" + str(Thursday) \
			+ " WHERE task='[migupage]' OR task='[miguclient]' OR task='[cailing]' \
				GROUP BY task,pro,isp \
			UNION ALL \
			SELECT task,pro,isp,SUM(speed) AS speed,SUM(weight) AS weight FROM \
			speed_" + str(Friday) \
			+ " WHERE task='[migupage]' OR task='[miguclient]' OR task='[cailing]' \
				GROUP BY task,pro,isp \
			UNION ALL \
			SELECT task,pro,isp,SUM(speed) AS speed,SUM(weight) AS weight FROM \
			speed_" + str(Saturday) \
			+ " WHERE task='[migupage]' OR task='[miguclient]' OR task='[cailing]' \
				GROUP BY task,pro,isp \
			UNION ALL \
			SELECT task,pro,isp,SUM(speed) AS speed,SUM(weight) AS weight FROM \
			speed_" + str(Sunday) \
			+ " WHERE task='[migupage]' OR task='[miguclient]' OR task='[cailing]' \
				GROUP BY task,pro,isp \
			)a GROUP BY task,pro,isp";

	attach_path = "/home/fanhx/tmp.txt";
	task_key_value = {
						"[migupage]":"http://img01.12530.com",
						"[miguclient]":"http://wlanwm.12530.com",
						"[cailing]":"http://open.migu.cn"
					};
	#code_map = fill(code_file_path);
	result = query(sql);
	write(attach_path,result,task_key_value);
	_from = "lili.fu@chinacache.com";
	to = ["dingyuan.liu@chinacache.com"];
	#to = ["qi.wang@chinacache.com","hongxing.fan@chinacache.com"];
	#cc = ["shan.liang@chinacache.com","dingyuan.liu@chinacache.com"];
	sendMail(_from,to,cc,attach_path);
else:
	print("out of main");

