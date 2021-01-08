from flask import Blueprint, request, render_template, redirect, url_for, session
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
        # if form.connect_condition.data == 'connect':
            new_like = LikeAlbum(user_id, form.to_album_id.data)
            with db.session.begin(subtransactions=True):
                new_like.create_new_like()
                # connect.update_status()
            db.session.commit()
        # elif form.connect_condition.data == 'accept':
        #     connect = LikeAlbum.select_by_from_user_id(form.to_album_id.data)
        #     if connect:
        #         with db.session.begin(subtransactions=True):
        #             connect.update_status()
        #         db.session.commit()
    # next_url = session.pop('url', 'app:home')
    # return redirect(url_for(next_url))

    return render_template('history/history.html', albums=albums, artists=artists, like_albums=like_albums, user=user, form=form)

