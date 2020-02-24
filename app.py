from flask import Flask
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_mail import Mail, Message

app = Flask(__name__)


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/travelplanner"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'asdjf23kja'


mail = Mail(app)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route('/registe', methods=["POST", "GET"])
def registe():
    print(request.method)
    if request.method == "POST":
        print("11post")
        username = request.form["username"]
        print(username)
        email = request.form["email"]
        password = request.form["password"]
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("registe.html")


class User(db.Model):
    __tablename__ = "tbl_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))


if __name__ == '__main__':
    app.run()
