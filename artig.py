app.permanent_session_lifetime=timedelta(seconds=30)


#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Falsedb=SQLAlchemy(app)


class Users(db.Model):
	_id=db.Column("id",db.Integer,primary_key=True)
	name=db.Column(db.String(100))
	email=db.Column(db.String(100))

	def __init__(self,name,email):
		self.name=name
		self.email=email

