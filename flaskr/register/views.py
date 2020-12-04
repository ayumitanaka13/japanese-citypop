from flask import Blueprint, request, render_template, redirect, url_for
from flaskr.forms import RegisterForm
from flaskr.models import User

register_bp = Blueprint('register', __name__, url_prefix='/register')

@register_bp.route('', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data
        )
        user.add_user()
        return redirect(url_for('login.login'))
    return render_template('register/register.html', form=form)