# coding=utf-8
from flask_wtf import  FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField,RadioField
from wtforms.validators import  Required,NumberRange


class UserForm(FlaskForm):

    name = StringField(label="What is your name?")
    password = PasswordField("Input your password")
    age = IntegerField("Input your age")
    submit = SubmitField("Submit")