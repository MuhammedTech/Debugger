import os
from flask import Blueprint, render_template, abort ,redirect, url_for, flash, request, send_from_directory, current_app
from flask_login import current_user,login_required
from debugger import db
from debugger.models import Tickets,Users,Comment,Attachment
from debugger.tickets.forms import TicketForm,CommentForm,AttachForm
from debugger.tickets.utils import save_file

tickets = Blueprint('tickets',__name__)

@tickets.route('/ticket/<int:ticket_id>',methods=['GET','POST'])
@login_required
def ticket(ticket_id):
    ticket = Tickets.query.get_or_404(ticket_id)
    com = Comment.query.filter_by(ticket_id=ticket.id).first()
    form = CommentForm()
    attachform = AttachForm()
    if form.validate_on_submit() and form.body.data:
        comment = Comment(body=form.body.data,ticket_id=ticket_id,author = current_user.username)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been published.')
        return redirect(url_for('tickets.ticket', ticket_id=ticket_id))
    if attachform.validate_on_submit():
        if attachform.file.data:
            picture_file = save_file(attachform.file.data)
            attachment = Attachment(file=picture_file,ticket_id=ticket_id)
            db.session.add(attachment)
        db.session.commit()
        flash('Your file has been published.')
        return redirect(url_for('tickets.ticket', ticket_id=ticket_id))
    return render_template('ticket.html', title=ticket.title,ticket=ticket,form=form,comment=com,attachform=attachform)



@tickets.route('/createTicket',methods=['GET','POST'])
@login_required
def createTicket():
    if current_user.expert == 0:
        return redirect(url_for('main.index'))
    users = Users.query.all()
    form = TicketForm()
    if form.validate_on_submit():
       ticket = Tickets(title=form.title.data,ticket_text=form.ticket_text.data,created_by_id=current_user.username,expert_id= str(form.user_id.data),project_id = str(form.project.data),status=form.status.data,priority=form.priority.data)
       db.session.add(ticket)
       db.session.commit()
       flash('Your ticket has been created', 'success')
       return redirect(url_for('main.index'))
    return render_template('createTicket.html',title='Create a Ticket',form=form, users=users)



@tickets.route('/editTicket/<ticket_id>/edit',methods=['GET','POST'])
@login_required
def editTicket(ticket_id):
    if current_user.expert == 0:
        return redirect(url_for('main.index'))
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
        flash('Your ticket has been updated!', 'success')
        return redirect(url_for('main.index', ticket_id=ticket.id))
    elif request.method == "GET":
        form.status.default = ticket.status
        form.priority.default = ticket.priority
        form.user_id.default = ticket.expert_id
        form.project.default = ticket.project_id
        form.process()
        form.title.data = ticket.title
        form.ticket_text.data = ticket.ticket_text
    return render_template('editTicket.html',form=form, title='Edit Ticket')

@tickets.route('/deleteTicket/<int:ticket_id>/delete',methods=['POST'])
@login_required
def delete_ticket(ticket_id):
    ticket = Tickets.query.get_or_404(ticket_id)
    if ticket.created_by_id != current_user:
        abort(403)
    db.session.delete(ticket)
    db.session.commit()
    flash('Ticket has been deleted!', 'success')
    return redirect(url_for('main.index'))



@tickets.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, mimetype='zip', filename=filename, as_attachment=True)