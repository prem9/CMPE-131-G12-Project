from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

# Create a form for composing an email
class ComposeForm(FlaskForm):
    recipient = StringField('To', validators=[DataRequired(message='Recipient(s)'), Email()])
    subject = StringField('Subject', validators=[DataRequired(message='Please enter the subject'), Length(min=1, max=255)])
    body = TextAreaField('Body', validators=[DataRequired(message='Please enter the body'), Length(min=1, max=10000)])
    submit = SubmitField('Send')