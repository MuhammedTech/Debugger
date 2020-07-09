
from flask_login import UserMixin
from debugger import login_manager,db
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    expert = db.Column(db.Boolean, nullable=False)
    projects = db.relationship('Projects', backref='author', lazy=True)
    tickets = db.relationship('Tickets',backref='author',lazy=True)

    def __repr__(self):
        return f"{self.username}"

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    created_by_id = db.Column(db.Integer, nullable = False)
    expert_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tickets = db.relationship('Tickets', backref='projector', lazy=True)

    def __repr__(self):
        return f"{self.title}"


class Tickets(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    #question text
    title = db.Column(db.String(100),nullable=False)
    ticket_text = db.Column(db.Text,nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    answer_text = db.Column(db.Text) #delete this
    #status = #open (default), closed (only expert) , resolved ( only developer)
    #priority = low,medium,high
    #comment =
    #attachment =
    created_by_id = db.Column(db.Integer, nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'),nullable=False)
    projects = db.relationship('Projects', backref='ticketso', lazy=True)

    def __repr__(self):
        return f"Tickets('{self.title}','{self.date_posted}')"
