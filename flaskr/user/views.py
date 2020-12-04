from flask import Blueprint, render_template
from flask_login import login_required

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('')
@login_required
def user():
    return render_template('user/user.html')