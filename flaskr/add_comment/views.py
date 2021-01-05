from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from flaskr.forms import CommentForm
from flaskr.models import Artist, Comment, User
from flaskr import db

add_comment_bp = Blueprint('add_comment', __name__, url_prefix='/add_comment') 

@add_comment_bp.route('', methods=['GET', 'POST'])
@login_required
def add_comment():
    user_id = current_user.get_id()
    user = User.select_user_by_id(user_id)
    form = CommentForm(request.form)

    if request.method == 'POST' and form.validate():
        new_comment = Comment(current_user.get_id(), id, form.comment.data)
        with db.session.begin(subtransactions=True):
            new_comment.create_comment()
        db.session.commit()
    return render_template('add_comment/add_comment.html', form=form, user=user, to_artist_id=id)

