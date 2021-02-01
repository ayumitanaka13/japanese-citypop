from flask import Blueprint, render_template, redirect, url_for,request
from flaskr.forms import SearchForm
from flaskr.models import Album

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

# @bp.route('/searchbar', methods=['GET', 'POST'])
# def searchbar():
#     albums = Album.query.all()
#     form = SearchForm(request.form)

#     if request.method == 'POST' and form.validate():
#         name = form.name.data
#         return redirect(url_for('result.result'))
#     return render_template(
#         'searchbar.html', albums=albums, form=form)

@bp.route('/comingsoon')
def comingsoon():
    return render_template('comingsoon.html')

@bp.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('app.home'))

@bp.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500