from flask import Flask,render_template,flash,redirect,url_for
from forms import RegistrationForm,LoginForm,TicketForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,UserMixin,login_user,current_user,logout_user



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

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
        return f"User('{self.username}')"

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    created_by_id = db.Column(db.Integer, nullable = False)
    expert_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tickets = db.relationship('Tickets', backref='projector', lazy=True)



class Tickets(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    #question text
    title = db.Column(db.String(100),nullable=False)
    ticket_text = db.Column(db.Text,nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    answer_text = db.Column(db.Text)
    created_by_id = db.Column(db.Integer, nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'),nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"




@app.route('/')
def index():
    return render_template('home.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data,password=hashed_password,admin=0,expert=0)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember = form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful.Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/question')
def question():
    return render_template('question.html')
@app.route('/createTicket',methods=['GET','POST'])
def createTicket():
    users = Users.query.all()
    form = TicketForm()
    if form.validate_on_submit():
       ticket = Tickets(title=form.title.data,ticket_text=form.ticketText.data,created_by_id=current_user.username)
       db.session.add(ticket)
       db.session.commit()
       flash('You ticket has been created', 'success')
       return redirect(url_for('home'))
    return render_template('createTicket.html',title='Create a Ticket',form=form, users=users)

@app.route('/ask')
def ask():
    return render_template('ask.html')

@app.route('/unanswered')
def unanswered():
    return render_template('unanswered.html')
@app.route('/users')
def users():
    users = Users.query.all()
    return render_template('users.html',users=users)

@app.route('/promote/<user_id>')
def promote(user_id):
    user = Users.query.get_or_404(user_id)
    user.expert = 1
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
