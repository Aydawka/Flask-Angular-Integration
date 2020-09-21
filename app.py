from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app=Flask(__name__)
app.secret_key='fff'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crudi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Data(db.Model):
	_id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100))
	email=db.Column(db.String(100))
	phone=db.Column(db.String(100))
	def __init__(self,name,email,phone):
		self.name=name
		self.email=email
		self.phone=phone





@app.route("/")
def home():
	all_data=Data.query.all()
	return render_template('home.html',employees=all_data)


@app.route("/insert",methods=['POST'])
def insert():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']
		mydata = Data(name, email, phone)
		db.session.add(mydata)
		db.session.commit()
		flash("Employee Inserted Successfully")
		return redirect(url_for('home'))



@app.route("/update",methods=['GET','POST'])
def update():

    if request.method == 'POST':
        mydata = Data.query.get(request.form.get('id'))
 
        mydata.name = request.form['name']
        mydata.email = request.form['email']
        mydata.phone = request.form['phone']
 
        db.session.commit()
        flash("Employee Updated Successfully")
 
        return redirect(url_for('home'))
 



@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    mydata = Data.query.get(id)
    db.session.delete(mydata)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('home'))
 
 





if __name__=='__main__':
	app.run(debug=True)






