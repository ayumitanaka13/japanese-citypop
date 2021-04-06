from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from flaskr.models import User, LikeAlbum, LikeSong, Album, Artist
from flaskr.forms import UserForm
from flaskr import db

from config import storage

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('', methods=['GET', 'POST'])
@login_required
def user():
    like_albums = LikeAlbum.query.all()
    like_songs = LikeSong.query.all()
    
    albums = Album.query.all()
    artists = Artist.query.all() 

    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user_id = current_user.get_id()
        user = User.select_user_by_id(user_id)
        with db.session.begin(subtransactions=True):
            file = request.files[form.picture_path.name].read()
            if file:
                file_name = user_id + '_' + \
                    str(int(datetime.now().timestamp())) + '.jpg'
                picture_path = 'flaskr/static/image_user/' + file_name
                open(picture_path, 'wb').write(file)
                # Upload
                storage.child(f"image_user/{file_name}").put(f"flaskr/static/image_user/{file_name}")
                # Download
                user.picture_path = storage.child(f"image_user/{file_name}").get_url(f"flaskr/static/image_user/{file_name}")
                print("---------------")
                print(user.picture_path)
        db.session.commit()
        return redirect(url_for('user.user'))
        flash('User info update completed.')
    return render_template('user/user.html', like_albums=like_albums, like_songs=like_songs, albums=albums, artists=artists, form=form)
