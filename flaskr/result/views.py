from flask import Blueprint, render_template

result_bp = Blueprint('result', __name__, url_prefix='/result')

@result_bp.route('')
def result():
    return render_template('result/result.html')