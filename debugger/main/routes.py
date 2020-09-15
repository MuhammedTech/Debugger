from flask import Blueprint,render_template
from debugger.models import Projects,Tickets
from flask_login import current_user,login_required


main = Blueprint('main',__name__)

@main.route('/dashboard')
@login_required
def index():
    projects = Projects.query.all()
    if current_user.expert != 1:
        tickets = Tickets.query.filter(Tickets.expert_id == current_user.username).all()
    else:
        tickets = Tickets.query.all()
    return render_template('home.html', projects = projects , tickets = tickets)


@main.route('/about')
@login_required
def about():
    return render_template('about.html')