from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,widgets,TextAreaField,SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from debugger.models import Users,Projects


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


"""class MultiCheckboxField(QuerySelectField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()"""

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Text',validators=[DataRequired()])
    user_id = QuerySelectMultipleField('Users',query_factory=lambda: Users.query)
    submit = SubmitField('Submit')



class TicketForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    ticket_text = TextAreaField('Text',validators=[DataRequired()])
    user_id = QuerySelectField('Users',query_factory=lambda: Users.query)
    project = QuerySelectField('Projects',query_factory=lambda: Projects.query)
    status = SelectField('Status',coerce=str,choices=[('Open','Open'),('Pending','Pending'),('Resolved','Resolved'),('Closed','Closed')])
    priority = SelectField('Priority',choices=[('Low','Low'),('Medium','Medium'),('High','High'),('Critical','Critical')])
    submit = SubmitField('Submit')

    def iter_choices(self):
        self.data if self.data is not None else self.coerce(self.default)


class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')
class ReplyForm(FlaskForm):
    reply = StringField('Enter your Reply ', validators=[DataRequired()])
    submit = SubmitField('Submit')