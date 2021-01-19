from flask import Blueprint, render_template, redirect, url_for,request
from flaskr.forms import SearchForm
from flaskr.models import Album

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/search', methods=['GET'])
def name_search():
    albums = Album.query.all()

    form = SearchForm(request.form)
    # session['url'] = 'app.user_search'
    # users = None
    name = request.args.get('name', None, type=str)
    next_url = prev_url = None
    if name:
        page = request.args.get('page', 1, type=int)
        posts = albums.search_by_name(name, page)
        # next_url = url_for('app.user_search', page=posts.next_num, username=user_name) if posts.has_next else None
        # prev_url = url_for('app.user_search', page=posts.prev_num, username=user_name) if posts.has_prev else None
        # users = posts.items
    return render_template(
        'base.html', albums=albums, form=form, next_url=next_url, prev_url=prev_url
    )

@bp.route('/comingsoon')
def comingsoon():
    return render_template('comingsoon.html')

@bp.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('app.home'))

@bp.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500