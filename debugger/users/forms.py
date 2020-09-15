from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from debugger.models import Users
from wtforms.validators import DataRequired, Length, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose different one')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')