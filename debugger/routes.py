from flask import render_template,flash,redirect,url_for,request
from debugger import app,db
from debugger.forms import RegistrationForm,LoginForm,TicketForm,ProjectForm
from debugger.models import Users,Projects,Tickets
from flask_login import current_user,logout_user,login_user
from debugger import bcrypt

@app.route('/')
def index():
    projects = Projects.query.all()
    tickets = Tickets.query.all()
    return render_template('home.html', projects = projects , tickets = tickets)
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
            flash("You've logged in successfully", 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful.Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/project/<project_id>')
def project(project_id):
    project = Projects.query.get_or_404(project_id)
    return render_template('project.html', title=project.title, project=project)

@app.route('/ticket/<ticket_id>')
def ticket(ticket_id):
    ticket = Tickets.query.get_or_404(ticket_id)
    return render_template('ticket.html', title=ticket.title, ticket=ticket)


@app.route('/createTicket',methods=['GET','POST'])
def createTicket():
    users = Users.query.all()
    form = TicketForm()
    if form.validate_on_submit():
       ticket = Tickets(title=form.title.data,ticket_text=form.ticket_text.data,created_by_id=current_user.username,expert_id= str(form.user_id.data),project_id= str(form.project.data),status=form.status.data,priority=form.priority.data)
       db.session.add(ticket)
       db.session.commit()
       flash('Your ticket has been created', 'success')
       return redirect(url_for('index'))
    return render_template('createTicket.html',title='Create a Ticket',form=form, users=users)

@app.route('/createProject',methods=['GET','POST'])
def createProject():
    users = Users.query.all()
    form = ProjectForm()
    if form.validate_on_submit():
        project = Projects(title = form.title.data, description = form.description.data, created_by_id = current_user.username, expert_id = str(form.user_id.data))
        db.session.add(project)
        db.session.commit()
        flash('You project has been created', 'success')
        return redirect(url_for('index'))
    return render_template('createProject.html',form = form, users = users)


@app.route('/editTicket/<ticket_id>/edit',methods=['GET','POST'])
def editTicket(ticket_id):
    ticket = Tickets.query.get_or_404(ticket_id)
    form = TicketForm()
    if form.validate_on_submit():
        ticket.title = form.title.data
        ticket.ticket_text = form.ticket_text.data
        ticket.expert_id = str(form.user_id.data)
        ticket.created_by_id = current_user.username
        ticket.project_id = ticket.project_id
        ticket.status = form.status.data
        ticket.priority = form.priority.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('index', ticket_id=ticket.id))
    elif request.method == "GET":
        form.title.data = ticket.title
        form.ticket_text.data = ticket.ticket_text
        form.user_id.data = ticket.expert_id
    return render_template('editTicket.html',form=form, title='Edit Ticket')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ask')
def ask():
    return render_template('ask.html')

@app.route('/unanswered')
def unanswered():
    return render_template('unanswered.html')

@app.route('/answer')
def answer():
    return render_template('answer.html')


@app.route('/question')
def question():
    return render_template('question.html')

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
    return redirect(url_for('login'))
