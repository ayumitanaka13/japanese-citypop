from flask import Blueprint, request, render_template, flash
from flask_login import login_required, current_user
from flaskr.forms import CommentForm, LikeSongForm
from flaskr.models import Artist, Comment, LikeSong, User
from flaskr import db

artist_bp = Blueprint('artist', __name__, url_prefix='/artist') 

@artist_bp.route('', methods=['GET', 'POST'])
def artist():
    artists = Artist.query.all()
    comments = Comment.query.all()
    like_songs = LikeSong.query.all()
    users = User.query.all()

    user_id = current_user.get_id()
    user = User.select_user_by_id(user_id)

    form = LikeSongForm(request.form)
    form_c = CommentForm(request.form)


    if request.method == 'POST' and form.validate():
        new_like = LikeSong(user_id, form.to_artist_id.data)
        with db.session.begin(subtransactions=True):
            if new_like.is_liked(form.to_artist_id.data) == False:
                new_like.add_like()
            else:
                liked_items = LikeSong.query.filter_by(
                    from_user_id = user_id,
                    to_artist_id = form.to_artist_id.data
                ).all()
                for liked_item in liked_items:
                    liked_item.delete_like()
        db.session.commit()

    if request.method == 'POST' and form_c.validate():
        new_comment = Comment(user_id, form_c.to_artist_id.data, form_c.comment.data)
        with db.session.begin(subtransactions=True):
            new_comment.create_comment()
        db.session.commit()
        flash("Your comment has been added!", "success")

    return render_template('artist/artist.html', artists=artists, comments=comments, like_songs=like_songs, users=users, user=user, form=form, form_c=form_c)