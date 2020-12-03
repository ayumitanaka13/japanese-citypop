from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from flaskr.forms import LoginForm, RegisterForm
from flaskr.models import User

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.home'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.select_by_email(form.email.data)
        if user and user.validate_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next:
                next = url_for('app.home')
            return redirect(next)
    return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data
        )
        user.add_user()
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)

@bp.route('/user')
@login_required
def user():
    return render_template('user.html')