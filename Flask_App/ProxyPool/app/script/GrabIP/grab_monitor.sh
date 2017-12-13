#!/bin/sh
ps -fe|grep Grab_ip_xundaili.py |grep -v grep
if [ $? -ne 0 ]
then
echo "start process xundaili ....."
nohup /home/software/anaconda3/bin/python /home/Interface/Proxy_pool/app/script/Grab_ip_xundaili.py&
else
echo "still runing....."
fi
