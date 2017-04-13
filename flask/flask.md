## flask_run

### 前言
flask有很多启动方式，根据需要选择。

### 参考项目组织架构

	Dtoy/
		└── app/
		        ├── Dtoy/
		        │      ├── __init__.py
		        │      ├── static/
		        │      ├── templates/
		        │      ├── forms.py
		        │      ├── routes.py
				│      ├── models.py
				│      ├── test.py
		        ├── runserver.py     
 				├── config.py      
		        └── README.md


### 使用tornado

>runserver.py

	#coding=utf-8
	#!/usr/bin/python
	
	from tornado.wsgi import WSGIContainer
	from tornado.httpserver import HTTPServer
	from tornado.ioloop import IOLoop
	from Doty import app
	
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(5000)  #flask默认的端口
	IOLoop.instance().start()

### websocket启动方式


>\_\_init\_\_.py

	from flask import Flask

	from flask_socketio import SocketIO
	import eventlet
	
	eventlet.monkey_patch()
	socketio = SocketIO(app, async_mode='eventlet')

>runserver.py

	from Dtoy import app,socketio

	if __name__ == '__main__':
		# app.run(debug=True,host='0.0.0.0',port=15000)
	    socketio.run(app, debug=True,host='0.0.0.0',port=15001)

	
