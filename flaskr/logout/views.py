from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, logout_user

logout_bp = Blueprint('logout', __name__, url_prefix='/logout')

@logout_bp.route('/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.home'))