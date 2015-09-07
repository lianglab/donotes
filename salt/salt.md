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

####节点分组

对目标服务器分组有以下七种方式，这七种方式的标示符分别为：

1. G -- 针对 Grains 做单个匹配，例如：G@os:Ubuntu
2. E -- 针对 minion 针对正则表达式做匹配，例如：E@web\d+.(dev|qa|prod).loc
3. P -- 针对 Grains 做正则表达式匹配，例如：P@os:(RedHat|Fedora|CentOS)
4. L -- 针对 minion 做列表匹配，例如：L@minion1.example.com,minion3.domain.com or bl*.domain.com
5. I -- 针对 Pillar 做单个匹配，例如：I@pdata:foobar
6. S -- 针对子网或是 IP 做匹配，例如：S@192.168.1.0/24 or S@192.168.1.100
7. R -- 针对客户端范围做匹配，例如： R@%foo.bar
	

>列表组，采用L前缀标示

	nodegroups:
	  rs: 'L@rs1,rs2'

>正则表达式，采用E前缀标示

	nodegroups:
	  test: 'E@rs[0-9]'

>混合，测试结论为 or 后可以正则，and 则失败
	
	nodegroups:
	  rs: 'L@rs1,rs2 or app21[0-9]'
	
>遇到故障及处理

	1.Minion did not return. [Not connected]
	修改客户端 /etc/salt/minion_id   内容等于minion中注册id

	2.No minions matched the target. No command was sent, no jid was assigned.
	分组表达式错误


