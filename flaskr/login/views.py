from flask import Blueprint, request, render_template, redirect, url_for, flash, current_app
from flask_login import login_user
from flaskr.forms import LoginForm
from flaskr.models import User

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('', methods=['GET', 'POST'])
def login():
    current_app.logger.info('%s 0')
    form = LoginForm(request.form)
    current_app.logger.info('%s 1')
    if request.method == 'POST' and form.validate():
        current_app.logger.info('%s 2')
        user = User.select_user_by_email(form.email.data)
        current_app.logger.info('%s 3')
        if user and user.is_active and user.validate_password(form.password.data):
            current_app.logger.info('%s 4')
            login_user(user, remember=True)
            current_app.logger.info('%s 5')
            next = request.args.get('next')
            current_app.logger.info('%s 6')
            if not next:
                current_app.logger.info('%s 7')
                next = url_for('app.home')
                current_app.logger.info('%s 8')
            return redirect(next)
            current_app.logger.info('%s 9')
        elif not user:
            current_app.logger.info('%s 10')
            flash('This user does not exist.')
            current_app.logger.info('%s 11')
        elif not user.is_active:
            current_app.logger.info('%s 12')
            flash('Please reset your password.')
            current_app.logger.info('%s 13')
        elif not user.validate_password(form.password.data):
            current_app.logger.info('%s 14')
            flash('Your email address or password is not correct.')
            current_app.logger.info('%s 15')
    return render_template('login/login.html', form=form)