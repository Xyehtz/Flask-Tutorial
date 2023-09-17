from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
  username = StringField(label="Enter your Username:")
  email_address = StringField(label="Enter your Email Address:")
  password1 = PasswordField(label="Enter your Password:")
  password2 = PasswordField(label="Confirm your Password:")
  submit = SubmitField(label="Crate account")
