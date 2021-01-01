from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user
from flaskr.forms import LoginForm
from flaskr.models import User

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.select_user_by_email(form.email.data)
        if user and user.is_active and user.validate_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next:
                next = url_for('app.home')
            return redirect(next)
        elif not user:
            flash('This user does not exist.')
        elif not user.is_active:
            flash('Please reset your password.')
        elif not user.validate_password(form.password.data):
            flash('Your email address or password is not correct.')
    return render_template('login/login.html', form=form)