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


@app.route('/testpage', methods=["POST", "GET"])
def testpage():
    destination = request.form.get('destination')
    Airline_start = request.form.get('startplace')
    Airline_end = request.form.get('endplace')
    startday = request.form.get('startday')
    endday = request.form.get('endday')
    interest = request.form.getlist('interest')



    return render_template("testPage.html", destination=destination,
                           startplace=Airline_start, endplace=Airline_end,
                           startday=startday, endday=endday,
                           interest=interest)


if __name__ == '__main__':
    app.run()
