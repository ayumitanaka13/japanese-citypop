from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from flaskr.forms import CommentForm
from flaskr.models import Artist, Comment, User
from flaskr import db

artist_bp = Blueprint('artist', __name__, url_prefix='/artist') 

@artist_bp.route('', methods=['GET', 'POST'])
def artist():
    artists = Artist.query.all()
    comments = Comment.query.all()
    form = CommentForm(request.form)
    user_id = current_user.get_id()
    user = User.select_user_by_id(user_id)

# @artist_bp.route('', methods=['GET', 'POST'])
# @login_required
# def add_comment():
#     form = CommentForm(request.form)
#     user = User.select_user_by_id(id)

#     if request.method == 'POST' and form.validate():
#         new_comment = Comment(current_user.get_id(), id, form.message.data)
#         with db.session.begin(subtransactions=True):
#             new_comment.create_message()
#         db.session.commit()
#         return redirect(url_for('app.message', id=id))

    return render_template('artist/artist.html', artists=artists, comments=comments, form=form, to_artist_id=id, user=user)

