from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,widgets,TextAreaField,SelectMultipleField
from wtforms.ext.sqlalchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms.validators import  DataRequired,Length
from debugger.models import Users,Projects


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


"""class MultiCheckboxField(QuerySelectField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()"""

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Text',validators=[DataRequired()])
    user_id = QuerySelectMultipleField('Users',query_factory=lambda: Users.query)
    submit = SubmitField('Create')

class TicketForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    ticketText = TextAreaField('Text',validators=[DataRequired()])
    user_id = QuerySelectField('Users',query_factory=lambda: Users.query)
    project = QuerySelectField('Projects',query_factory=lambda: Projects.query)
    submit = SubmitField('Create')


