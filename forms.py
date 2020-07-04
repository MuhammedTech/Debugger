from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError,TextAreaField,SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import  DataRequired,Length


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    """def validate_username(self,username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose different one')"""

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class TicketForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    ticketText = TextAreaField('Text',validators=[DataRequired()])
    user_id = QuerySelectField('Users',query_factory=lambda: Users.query.all())
    submit = SubmitField('Create')
