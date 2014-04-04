#!/bin/sh

#作者：范洪星
#描述：用于判断pub_dimdetails.sh脚本执行的结果情况，包括日期，文件大小
#时间：2013年3月31日 星期一 下午
#总结：1.echo输出变量内容，echo ""是有换行符的。cat输出文件内容 
#	   2.注意awk使用

#只要2个参数
if [[ $# != 2 ]]
then
	echo "please input 2 args ,first is start date,second is end date"
	exit
fi

path_pre="/user/autolog/autodc_index/pub_data/pub_dimdetails" #结果路径前缀

start=$1
end=$2
current=$start

compare_model_index="compare_model/part"
dealer_order_index="dealer_order/part"
pvlog_model_index="pvlog_model/part"

while [[ $current < $end ]]
do
	echo $current
	content=`hadoop dfs -ls "$path_pre/$current/*/part*"`
	#echo "$content" #加上""后显示结果换行
	echo "$content" | awk 'BEGIN{FS=" ";OFS="\t"} {
							if($8 ~ /compare_model/) {
								count["compare_model_time"] = $6" "$7
								count["compare_model_size"] += $5
							} else if($8 ~ /dealer_order/) {
								count["dealer_order_time"] = $6" "$7
								count["dealer_order_size"] += $5
							} else if($8 ~ /pvlog_model/) {
								count["pvlog_model_time"] = $6" "$7
								count["pvlog_model_size"] += $5
							}
						}
						END{
							for(item in count) {
								print item,count[item]
							}
						}'
							
	
	current=`date -d "$current 1 day" "+%Y%m%d"`
done
