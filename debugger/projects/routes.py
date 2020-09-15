from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import current_user,login_required
from debugger import db
from debugger.models import Projects,Users
from debugger.projects.forms import ProjectForm

projects = Blueprint('projects',__name__)


@projects.route('/project/<project_id>')
@login_required
def project(project_id):
    project = Projects.query.get_or_404(project_id)
    return render_template('project.html', title=project.title, project=project)

@projects.route('/createProject',methods=['GET','POST'])
@login_required
def createProject():
    if current_user.expert == 0:
        return redirect(url_for('main.index'))
    users = Users.query.all()
    form = ProjectForm()
    if form.validate_on_submit():
        project = Projects(title = form.title.data, description = form.description.data, created_by_id = current_user.username, expert_id = str(form.user_id.data))
        db.session.add(project)
        db.session.commit()
        flash('You project has been created', 'success')
        return redirect(url_for('main.index'))
    return render_template('createProject.html',form = form, users = users)