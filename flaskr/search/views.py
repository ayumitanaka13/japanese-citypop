from flask import Blueprint, render_template, request, redirect, url_for, session
from flaskr.models import Album
from flaskr.forms import SearchForm

search_bp = Blueprint('search', __name__, url_prefix='/search')

@search_bp.route('', methods=['GET', 'POST'])
def search():
    albums = Album.query.all()
    form = SearchForm(request.form)

    if request.method == 'POST' and form.validate():
        keyword = form.keyword.data
    return render_template('search/search.html', albums=albums, form=form)