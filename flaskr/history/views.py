from flask import Blueprint, request, render_template, session, redirect, url_for
from flask_login import current_user
from flaskr.forms import LikeAlbumForm
from flaskr.models import Age, Album, Artist, User, LikeAlbum
from flaskr import db

history_bp = Blueprint('history', __name__, url_prefix='/history')

@history_bp.route('', methods=['GET', 'POST'])
def history():
    albums = Album.query.join(Age, Age.id==Album.from_age_id).add_columns(
        Age.age, Age.info.label('age_info'),
        Album.id, Album.year, Album.name, Album.name_j, Album.title, Album.title_j,
        Album.info, Album.album_picture_path, Album.artist_picture_path
    ).all()
    artists = Artist.query.all()
    like_albums = LikeAlbum.query.all()

    user_id = current_user.get_id()
    user = User.select_user_by_id(user_id)

    form = LikeAlbumForm(request.form)

    if request.method == 'POST' and form.validate():
        new_like = LikeAlbum(user_id, form.to_album_id.data)
        with db.session.begin(subtransactions=True):
            if new_like.is_liked(form.to_album_id.data) == False:
                new_like.add_like()
            else:
                liked_items = LikeAlbum.query.filter_by(
                    from_user_id = user_id,
                    to_album_id = form.to_album_id.data
                ).all()
                for liked_item in liked_items:
                    liked_item.delete_like()
        db.session.commit()
        return redirect(url_for('history.history'))
    return render_template('history/history.html', albums=albums, artists=artists, like_albums=like_albums, user=user, form=form)