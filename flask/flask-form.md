##flask-form


####注册实例

>目录架构

	flaskapp/
		└── app/
		        ├── form_to_flask/
		        │      ├── __init__.py
		        │      ├── static/
		        │      ├── templates/
		        │      ├── forms.py
		        │      ├── routes.py
				│	   ├── models.py
		        ├── runserver.py        
		        └── README.md


>基础启动（runserver.py）

	from intro_to_flask import app
	app.run(debug=True)



>数据库路径定义（\_\_init\_\_.py)

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

	from models import db
	db.init_app(app)

>建表sql

	CREATE TABLE users (
		uid INT NOT NULL PRIMARY KEY,
		firstname VARCHAR(100) NOT NULL,
		lastname VARCHAR(100) NOT NULL,
		email VARCHAR(120) NOT NULL UNIQUE,
		pwdhash VARCHAR(100) NOT NULL
	);


>数据定义（modeles.py) 

	from flask.ext.sqlalchemy import SQLAlchemy
	from werkzeug import generate_password_hash, check_password_hash
	
	db = SQLAlchemy()
	
	class User(db.Model):
	  __tablename__ = 'users'
	  __table_args__ = {'sqlite_autoincrement': True}
	  uid = db.Column(db.Integer, primary_key = True)
	  firstname = db.Column(db.String(100))
	  lastname = db.Column(db.String(100))
	  email = db.Column(db.String(120), unique=True)
	  pwdhash = db.Column(db.String(54))
	  
	  def __init__(self, firstname, lastname, email, password):
	    self.firstname = firstname.title()
	    self.lastname = lastname.title()
	    self.email = email.lower()
	    self.set_password(password)
	
	    
	  def set_password(self, password):
	    self.pwdhash = generate_password_hash(password)
	  
	  def check_password(self, password):
	    return check_password_hash(self.pwdhash, password)

>表单定义项目（form.py)

	from flask.ext.wtf import Form
	from wtforms import IntegerField,TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
	from models import db, User

	class SignupForm(Form):
		firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
		lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
		email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
		password = PasswordField('Password', [validators.Required("Please enter a password.")])
		submit = SubmitField("Create account")
		
		def __init__(self, *args, **kwargs):
			Form.__init__(self, *args, **kwargs)
		
		def validate(self):
			if not Form.validate(self):
	  			return False
		
			user = User.query.filter_by(email = self.email.data.lower()).first()
			if user:
		  		self.email.errors.append("That email is already taken")
		  		return False
			else:
			  return True


>页面(signup.html)


	{% block content %}
	  <h2>Sign up</h2>
	
	  {% for message in form.firstname.errors %}
	    <div class="flash">{{ message }}</div>
	  {% endfor %}
	  
	  {% for message in form.lastname.errors %}
	    <div class="flash">{{ message }}</div>
	  {% endfor %}
	  
	  {% for message in form.email.errors %}
	    <div class="flash">{{ message }}</div>
	  {% endfor %}
	  
	  {% for message in form.password.errors %}
	    <div class="flash">{{ message }}</div>
	  {% endfor %}
	  
	  <form action="{{ url_for('signup') }}" method=post>
	    {{ form.hidden_tag() }}
	    
	
	    {{ form.firstname.label }}
	    {{ form.firstname }}
	    
	    {{ form.lastname.label }}
	    {{ form.lastname }}
	    
	    {{ form.email.label }}
	    {{ form.email }}
	    
	    {{ form.password.label }}
	    {{ form.password }}
	
	    {{ form.submit }}
	  </form>
	    
	{% endblock %}


>试图定义(routes.py)

	from intro_to_flask import app
	from flask import render_template, request, flash, session, url_for, redirect
	from forms import SignupForm
	from flask.ext.mail import Message, Mail
	from models import db, User


	@app.route('/signup', methods=['GET', 'POST'])
	def signup():
	  form = SignupForm()
	
	  if 'email' in session:
	    return redirect(url_for('profile')) 
	  
	  if request.method == 'POST':
	    if form.validate() == False:
	      return render_template('signup.html', form=form)
	    else:
	      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
	      db.session.add(newuser)
	      db.session.commit()
	      
	      session['email'] = newuser.email
	      return redirect(url_for('profile'))
	  
	  elif request.method == 'GET':
	    return render_template('signup.html', form=form)