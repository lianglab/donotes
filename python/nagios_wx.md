##微信开发之nagios报警

***

###前言

nagios是个入手很快的监控平台，默认采用email通知。微信开发顺便之余，将nagios报警方式修改成微信。经测试，微信公众号群发功能限制100条，虽然可以直接调用组发送，但是条目太少。采用模板单日可用10W，虽然每个人遍历发送，起码满足量上的需求。

###python代码

>人员获取

	目前采用拉取所有，遍历每个openid，通过判定组id进行比对，是否符合条件
	

>申请模板，或者直接调用微信模板，比如：

	{{first.DATA}}
	服务器：{{keyword1.DATA}}
	监控类型：{{keyword2.DATA}}
	监控点：{{keyword3.DATA}}
	异常发生时间：{{keyword4.DATA}}
	异常信息：{{keyword5.DATA}}
	{{remark.DATA}}

>代码可见 [wxapi.py](./code/wxapi.md)

	复合代码，根据需求选择对应功能

###nagios调用修改

>根据微信模板，添加微信报警调用入口

	
	vim /usr/local/nagios/etc/monitor/conmmands.cfg

	# 'notify-host-by-weixin' command definition
	define command{
		command_name	notify-host-by-weixin
		command_line	/usr/bin/python /usr/local/nagios/python/wxapi.py "hf.21tb.com#.#$HOSTNAME$#.#$NOTIFICATIONTYPE$#.#$HOSTSTATE$#.#$LONGDATETIME$#.#$HOSTOUTPUT$#.#$HOSTADDRESS$"
		}


	# 'notify-service-by-weixin' command definition
	define command{
		command_name	notify-service-by-weixin
		command_line	/usr/bin/python /usr/local/nagios/python/wxapi.py "hf.21tb.com#.#$HOSTALIAS$#.#$NOTIFICATIONTYPE$#.#$SERVICEDESC$#.#$LONGDATETIME$#.#$SERVICEOUTPUT$#.#$HOSTADDRESS$"
		}

>报警触发启动

	#查找对应调用，修改为上述定义的 weixin 命令
	vim  templates.cfg 

    service_notification_commands   notify-service-by-weixin	; send service notifications via email
    host_notification_commands      notify-host-by-weixin	; send host notifications via email

>检测reload

	/etc/init.d/nagios checkconfig
	
	/etc/init.d/nagios reload


	
	

