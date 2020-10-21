from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, login_user, logout_user
from debugger import db
from debugger.models import Users
from debugger.users.forms import RegistrationForm, LoginForm
from debugger import bcrypt

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, password=hashed_password, admin=0, expert=0)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/', methods=['GET', 'POST'])
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash("You've logged in successfully", 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful.Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/manageusers')
def userss():
    users = Users.query.all()
    if current_user.admin == 0:
        return redirect(url_for('main.index'))
    return render_template('users.html', users=users)


@users.route('/promote/<user_id>')
@login_required
def promote(user_id):
    if current_user.admin == 0:
        return redirect(url_for('main.index'))
    user = Users.query.get_or_404(user_id)
    user.expert = 1
    if user.expert == 1:
        user.expert = 0
    db.session.commit()
    return redirect(url_for('main.index'))


@users.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
