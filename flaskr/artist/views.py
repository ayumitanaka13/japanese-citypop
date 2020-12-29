from flask import Blueprint, request, render_template
from flask_login import login_required
from flaskr.forms import CommentForm
from flaskr.models import Artist, Comment, User

artist_bp = Blueprint('artist', __name__, url_prefix='/artist') 

@artist_bp.route('')
def artist():
    artists = Artist.query.all()
    comments = Comment.query.all()
    return render_template('artist/artist.html', artists=artists, comments=comments)

# @login_required
# def add_comment():