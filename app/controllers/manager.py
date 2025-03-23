from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask_login import current_user
from extensions import db  # ✅ Import db first
from models.application import Application
from models.forms import CreateAccountForm
from models.users import User
from models.cca import InterestGroup, CompetitiveGroup

manager_bp = Blueprint('manager', __name__)

@manager_bp.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateAccountForm()

    if request.method == 'POST':
        if form.validate():
            user = User.getUser(form.email.data)
            if user:
                flash("Account already exists.", 'warning')
            else:
                # ✅ MongoEngine handles persistence, no need for db.session
                User.createUser(form.email.data, form.name.data, "12345", form.account_type.data)
                flash(f"Student account {form.name.data}, {form.email.data} created successfully.", 'primary')
                return redirect(url_for('manager.create'))

    return render_template('create.html', form=form, panel="create student account")

@manager_bp.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == "GET":
        if current_user.role == "admin":
            user_type = "admin"
            applications = Application.getApplications()
        elif current_user.role == "CCA admin":
            user_type = "CCA"
            cca = InterestGroup.objects(name=current_user.name).first() or CompetitiveGroup.objects(name=current_user.name).first()
            applications = Application.getApplications(group=cca)
        else:
            user_type = "student"
            student = User.getUser(current_user.email)
            applications = Application.objects(student=student)

        app_list = [{
            "type": "Interest" if isinstance(application.group, InterestGroup) else "Competitive",
            "name": application.group.name,
            "email": application.student.email,
            "date": application.date.strftime('%a, %d %b %Y'),
            "status": application.status,
            "id": application.id
        } for application in applications]

        return render_template('process.html', panel="process application", applications=app_list, user_type=user_type)
    else:
        action = request.form.get('action')
        app_id = request.form.get('app_id')
        application = Application.getApplication(app_id)

        if application:
            user = application.student
            cca = application.group

        if action == "updatestatus":
            status = request.form.get('status')
            if Application.updateApplication(status, app_id):
                flash(f"Updated status for student {user.name} for CCA group {cca.name} to {status}", 'primary')
                return redirect(url_for('manager.process'))
        else:
            Application.deleteApplication(app_id)
            flash(f"Application for {cca.name} has been removed", 'primary')
            return redirect(url_for('manager.process'))
