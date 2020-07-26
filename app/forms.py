from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import IntegerField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class Signup(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class Publication(FlaskForm):
    Purpose = StringField('Purpose', validators=[DataRequired()])
    Amount = IntegerField('Amount', validators=[DataRequired()])
    Months = IntegerField('Months', validators=[DataRequired()])
    Description = TextAreaField('Description', validators=[DataRequired()])
    Submit = SubmitField('Submit')
