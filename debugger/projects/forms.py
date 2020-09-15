from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired
from debugger.models import Users

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Text',validators=[DataRequired()])
    user_id = QuerySelectMultipleField('Users',query_factory=lambda: Users.query)
    submit = SubmitField('Submit')