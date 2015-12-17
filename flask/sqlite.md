#sqlite
***

####如何id自增

>定义时声明

	class User(db.Model):
		__tablename__ = 'users'
		__table_args__ = {'sqlite_autoincrement': True}
		uid = db.Column(db.Integer, primary_key = True)
		firstname = db.Column(db.String(100))
		lastname = db.Column(db.String(100))
		email = db.Column(db.String(120), unique=True)
		pwdhash = db.Column(db.String(54))


>建表时不需要声明，因为不支持

	CREATE TABLE users (
		uid INTEGER NOT NULL PRIMARY KEY,
		firstname VARCHAR (100) NOT NULL,
		lastname VARCHAR (100) NOT NULL,
		email VARCHAR (120) NOT NULL UNIQUE,
		pwdhash VARCHAR (100) NOT NULL
	);

	#uid属性为INT无法自增，需改成支持的INTEGER

>参考报错信息(解决方案如上）

	near "AUTO_INCREMENT": syntax error