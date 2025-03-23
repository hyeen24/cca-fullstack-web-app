from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Email, Length, InputRequired

class LoginForm(FlaskForm):
    email = StringField('Email',  validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])
    name = StringField('Name')


class ChangePassForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[InputRequired(), Length(min=5, max=20)])
    new_password = PasswordField('New Password', validators=[InputRequired(), Length(min=5, max=20)])
    retype_password = PasswordField('Retype Password', validators=[InputRequired(), Length(min=5, max=20)])

class CreateAccountForm(FlaskForm):
    email = StringField('Email',  validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    name = StringField('Name', validators=[InputRequired(), Length(max=30)])
    account_type = SelectField('Choose account type:',choices=['Student', 'CCA Admin'])
