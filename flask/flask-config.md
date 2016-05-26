##flask-config

###前言
抽取静态配置，统一管理，是个管理程序的好方法


###添加配置文件

>目录架构

	flaskapp/
		└── Stoy/
		        ├── app/
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

>config.py文件模式

	USER = 'YOURUSER'

>包\_\_init\_\_.py中申明

	from flask import Flask
	app = Flask(__name__)
	app.config.from_object('config')

>test.pys使用

    user = app.config['USER']
