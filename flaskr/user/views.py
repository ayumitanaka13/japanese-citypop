from datetime import datetime

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from flaskr.models import User, LikeAlbum, Album
from flaskr.forms import UserForm
from flaskr import db

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('', methods=['GET', 'POST'])
@login_required
def user():
    like_albums = LikeAlbum.query.all()
    albums = Album.query.all()

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
                user.picture_path = 'image_user/' + file_name
        db.session.commit()
        flash('User info update completed.')
    return render_template('user/user.html', like_albums=like_albums, albums=albums, form=form)