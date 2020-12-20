from flask import Blueprint, render_template
from flaskr.models import Age, Album, Artist

history_bp = Blueprint('history', __name__, url_prefix='/history')

@history_bp.route('')
def history():
    albums = Album.query.join(Age, Age.id==Album.from_age_id).add_columns(
        Age.age, Age.info.label('age_info'), Album.id, Album.year,
        Album.name, Album.name_j, Album.title, Album.title_j, Album.info,
        Album.album_picture_path, Album.artist_picture_path).all()
    # artists = Artist.query.all()
    return render_template('history/history.html', albums=albums, artists=artists)

