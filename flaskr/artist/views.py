from flask import Blueprint, request, render_template
from flask_login import login_required
from flaskr.forms import CommentForm
from flaskr.models import Artist, Comment, User

artist_bp = Blueprint('artist', __name__, url_prefix='/artist') 

@artist_bp.route('')
def artist():
    artists = Artist.query.join(Comment, Artist.id==Comment.to_artist_id).add_columns(
        Artist.id, Artist.year, Artist.year, Artist.name, Artist.name_j,
        Artist.title, Artist.title_j, Artist.youtube, Artist.song_info, Artist.artist_info,
        Artist.song_picture_path, Artist.artist_picture_path,
        Comment.from_user_id, Comment.to_artist_id, Comment.comment
    ).all()
    return render_template('artist/artist.html', artists=artists)

# @login_required
# def add_comment():