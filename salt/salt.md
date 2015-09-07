##salt

###前言###

Salt是：
一个配置管理系统，能够维护预定义状态的远程节点(比如，确保指定的报被安装，指定的服务在运行);
一个分布式远程执行系统，用来在远程节点（可以是单个节点，也可以是任意规则挑选出来的节点）上执行命令和查询数据。


***
####简单搭建

>初始化yum源

	rpm -ivh http://mirrors.sohu.com/fedora-epel/6/x86_64/epel-release-6-8.noarch.rpm

>服务端安装

	yum  -y install salt-master

>服务端配置
	
	vi /etc/salt/master
	interface: 192.168.6.170
	auto_accept: False              //False:服务器端手工验证，True:自动验证</code>

>客户端安装

	yum -y install salt-minion

>客户端配置

	vi /etc/salt/minion
	master: 192.168.100.80 //指向master端的ip
	id: salt_minion-1 //客户端标识
	schedule: //客户端每隔30s去服务端进行同步更新
	  highstate:
	    function: state.highstate
	    seconds: 30

>防火墙设置

	vi /etc/sysconfig/iptables
	-A input -P tcp -m tcp --dport 4505 -j ACCEPT
	-A output -P tcp -m tcp --sport 4505 -j ACCEPT
	-A input -P tcp -m tcp --dport 4506 -j ACCEPT
	-A output -P tcp -m tcp --sport 4506 -j ACCEPT

>启动服务

	service salt-server start
	service salt-minion start

>收工验证方式

	salt-key -L
	salt-key -a [minion-key-n]

>测试验收

	salt '*' test.ping



