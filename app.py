from flask import Flask
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_mail import Mail, Message
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
