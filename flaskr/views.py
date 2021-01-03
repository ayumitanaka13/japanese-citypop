from flask import Blueprint, render_template, redirect, url_for,request
from flaskr.forms import SearchForm

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

# @bp.route('/search', methods=['GET'])
# def search():
#     form = SearchForm(request.form)
#     session['url'] = 'app.search'
#     keywords = None
#     keyword = request.args.get('keyword', None, type=str)
#     next_url = prev_url = None
#     if keyword:
#         page = request.args.get('page', 1, type=int)
#     return render_template('base.html', form=form)

@bp.route('/comingsoon')
def comingsoon():
    return render_template('comingsoon.html')

@bp.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('app.home'))

@bp.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500