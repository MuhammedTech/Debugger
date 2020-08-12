
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
    tickets = db.relationship('Tickets',backref='ticketso',lazy=True)

    def __repr__(self):
        return f"{self.title}"


class Tickets(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    ticket_text = db.Column(db.Text,nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    status = db.Column(db.String(30), nullable=False)
    priority = db.Column(db.String(30), nullable=False)
    #attachment =
    #make user - tickets many to many relationship
    created_by_id = db.Column(db.Integer, nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'),nullable=False)
    comment = db.relationship('Comment', backref='title', lazy='dynamic')
    #projects = db.relationship('Projects', backref=db.backref('ticketso', uselist=False), lazy=True)


    def __repr__(self):
        return f"Tickets('{self.title}','{self.date_posted}')"

class Comment(db.Model):
    _N = 6

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    author = db.Column(db.Integer,nullable=True)
    path = db.Column(db.Text, index=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'),nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'),nullable=False)
    replies = db.relationship(
        'Comment', backref=db.backref('parent', remote_side=[id]),
        lazy='dynamic')

    def __repr__(self):
        return '<Post %r>' % (self.body)

    def save(self):
        db.session.add(self)
        db.session.commit()
        prefix = self.parent.path + '.' if self.parent else ''
        self.path = prefix + '{:0{}d}'.format(self.id, self._N)
        db.session.commit()

    def level(self):
        return len(self.path)

