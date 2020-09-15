from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,FileField,SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from debugger.models import Users, Projects

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

class AttachForm(FlaskForm):
    file = FileField('Upload file')
    submit = SubmitField('Upload')