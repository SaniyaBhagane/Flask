from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
with app.app_context():
    db.create_all()

with app.app_context():
    user = User(name= 'ABC', email= "abc@gmail.com")
    db.session.add(user)
    db.session.commit()

@app.route('/')
def hello_worls():
    return '<p>Hello World !!</p>'

@app.route('/hello')
def hello():
    return render_template('hello.html', context={'name': 'User', 'age': 22})

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('form.html', context={'users': users})

if __name__ == '__main__':
    app.run()
