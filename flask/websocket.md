## websocket

#### 前言
使用flask-socketio实现websocket通信

>安装

	pip install flask-socketio
	pip install eventlet 


	
>Flask application

	from flask import Flask, render_template
	from flask_socketio import SocketIO
	import eventlet
	
	eventlet.monkey_patch()
	#若不启用这一项，采用polling方式，而不是websocket
	
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secret!'
	socketio = SocketIO(app)
	
	if __name__ == '__main__':
	    socketio.run(app)

>页面-->服务器通信

1.页面发送信息

	<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>

	#采用socket.io.min.js使用接口相同的库

	<script type="text/javascript" charset="utf-8">
		namespace = 'client send';
	    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
	    socket.on('connect', function() {
	        socket.emit('my event', {data: 'I\'m connected!'});
	    });
	</script>

2.服务端接收信息

	@socketio.on('my event', namespace='/client send')
	def handle_my_custom_namespace_event(json):
	    print('received json: ' + str(json))

>服务器-->页面通信

1.服务端发送信息

	socketio.emit('server send',
		{'data': 'test message', 'time': time.ctime()},
		namespace='/websocket/runlog')

2.页面接收信息

  	namespace = '/websocket/runlog';
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('server send', function(msg) {
        $('#log_content').append('<br>' + $('<div/>').text( msg.time + ': ' + msg.data).html());
    });

>同个命名空间，通过回话不同区分websocket

1.前端实例：

	$(function() {
	
	    namespace = '/websocket/runlog';
	    socketresponse = 'logcontent' + Math.floor(Math.random()*10000+1)
	    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
	    socket.on(socketresponse, function(msg) {
	        $('#log_content').append('<br>' + $('<div/>').text( msg.time + ': ' + msg.data).html());
	    });
	
	    $('#deploy').bind('click', function(){
	      $('#log_content').html("");
	      appname = $('select[name="appname"]').val();
	      if (!$.trim(appname)){
	        alert('请选择应用');
	        return false;
	      }
	
	      $.ajax({
	        type: 'post',
	        url:$SCRIPT_ROOT + '/deploy/deploy',
	        dataType: 'json',
	        data:{
	          socketresponse:socketresponse,
		        appname: $('select[name="appname"]').val(),
		        branch: $('input[name="branch"]').val()
	      },
	
	      error: function(xhr, err){
	        alert('请求失败，原因可能是：' + err + '！')
	      },
	
	      success: function(data, textStatus){
	        $('#log_content').prepend( '<h3>' + data.result + '</h3>');
	        }
	    });
	    return false
	  });
	});


2.后端实例：

	socketresponse = request.form['socketresponse']

	p = subprocess.Popen('shellscript', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	while p.poll() == None:
		line = p.stdout.readline()
		print line
		socketio.emit(socketresponse,
			{'data':line, 'time': time.ctime()},
			namespace='/websocket/runlog')

	shellresult = p.wait()
	if shellresult != 0:
		return jsonify(result='shellscript Failed')

	socketio.emit(socketresponse,
		{'data': u'shell done', 'time': time.ctime()},
		namespace='/websocket/runlog')