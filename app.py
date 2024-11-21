from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']= 'sqlite:///members.db'

db = SQLAlchemy(app)

class members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
name= db.Column(db String(200), nullable=False)
data_created=db.Column(db.DateTime, default=)

def __repr__(self):
    return.'<Name.%r'

members=[]

@app.route("/")
def members():
    title="About members"
    names=["Lufuno, Tondani, Thanyani"]
    return render_template("members.html", title=title, names=names)

    