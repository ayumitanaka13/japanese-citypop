from flask import Blueprint, request, render_template, redirect, url_for
from flaskr.forms import RegisterForm
from flaskr.models import User
from flaskr import db

signup_bp = Blueprint('signup', __name__, url_prefix='/signup')

@signup_bp.route('', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            email = form.email.data,
            username = form.username.data,
        )
        with db.session.begin(subtransactions=True):
            user.create_new_user()
        db.session.commit()
        return redirect(url_for('login.login'))
    return render_template('signup/signup.html', form=form)