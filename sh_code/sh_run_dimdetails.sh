#!/bin/sh

#作者：范洪星
#描述：运行pub_dimdetails.sh脚本
#时间：2014年3月31日 星期一 下午

#参数必须是两个
if [[ $# != 2 ]]
then
	echo "please input 2 args, first is start date,second is end date"
	exit
fi

start=$1
end=$2
current=$start
#echo '$start' #测试参数

sh_dir="/opt/pd/datacenter/shells/modelindex/prepare"
sh_file="pub_dimdetails.sh"
#cd $sh_dir #测试时注释掉

#while运行
while [[ $current < $end ]]
do
	echo $current
	#sh $sh_file $current #测试时注释掉
	current=`date -d "$current 1 day" "+%Y%m%d"` #注意单引号和双引号的区别
done
