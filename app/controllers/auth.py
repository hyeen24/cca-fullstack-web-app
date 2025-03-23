from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Import models
from models.forms import LoginForm, ChangePassForm
from models.users import User

# Import login_manager from extensions (not app)
from extensions import login_manager

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate():
        check_user = User.objects(email=form.email.data).first()
        if check_user:
            if check_password_hash(check_user.password, form.password.data):
                login_user(check_user)
                return redirect(url_for('home'))
            else:
                form.password.errors.append("Incorrect Password")
        else:
            form.email.errors.append("User not found")

    return render_template('login.html', form=form, panel="Login")

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Load user from database
@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()
