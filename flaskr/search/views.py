from flask import Blueprint, render_template, request, redirect, url_for, session
from flaskr.models import Album
from flaskr.forms import SearchForm

search_bp = Blueprint('search', __name__, url_prefix='/search')

@search_bp.route('', methods=['GET', 'POST'])
def search():
    # albums = Album.query.all()
    form = SearchForm(request.form)

    # session['url'] = 'search.search'
    # albums = None
    if request.method == 'POST' and form.validate():
        name = form.name.data
        albums = Album.search_by_name(name)

    # name = request.args.get('name', None, type=str)
    # next_url = prev_url = None
    # if name:
    #     page = request.args.get('page', 1, type=int)
    #     posts = Album.search_by_name(name, page)
    #     next_url = url_for('search.search', page=posts.next_num, name=name) if posts.has_next else None
    #     prev_url = url_for('search.search', page=posts.prev_num, name=name) if posts.has_prev else None
    #     albums = posts.items
        # return redirect(url_for('result.result'))
    return render_template('search/search.html', albums=albums, form=form)