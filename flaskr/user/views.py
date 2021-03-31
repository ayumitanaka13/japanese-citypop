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
                file_name = user_id + '.jpg'
                # file_name = user_id + '_' + \
                #     str(int(datetime.now().timestamp())) + '.jpg'
                picture_path = 'flaskr/static/image_user/' + file_name
                open(picture_path, 'wb').write(file)
                # upload
                storage.child("test/test.txt").put("flask.txt")
                # storage.child(f"image_user/{file_name}").put(picture_path)
                # storage.child(f"image_user/{file_name}").put("flaskr/static/image_user/2.jpg")
                # Download
                user.picture_path=storage.child("test/test.txt").get_url("flask.txt")
                # user.picture_path = storage.child(f"image_user/{file_name}").get_url("2.jpg")
                print(storage.child("test/test.txt").get_url("flask.txt"))
                # print(user.picture_path)
        db.session.commit()
        return redirect(url_for('user.user'))
        flash('User info update completed.')
    return render_template('user/user.html', like_albums=like_albums, like_songs=like_songs, albums=albums, artists=artists, form=form)


# ok
# https://firebasestorage.googleapis.com/v0/b/japanese-city-pop.appspot.com/o/image_user%2F2.jpg?alt=media&token=55bcae10-abc1-433b-9086-0960ff78c581
# db
# https://firebasestorage.googleapis.com/v0/b/japanese-city-pop.appspot.com/o/image_user%252F2.jpg%3Falt%3Dmedia%26token%3D2_1609734344.jpg