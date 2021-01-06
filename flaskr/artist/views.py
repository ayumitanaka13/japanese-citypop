from flask import Blueprint, request, render_template, flash
from flask_login import login_required, current_user
from flaskr.forms import CommentForm
from flaskr.models import Artist, Comment, User
from flaskr import db

artist_bp = Blueprint('artist', __name__, url_prefix='/artist') 
test_bp = Blueprint('test', __name__, url_prefix='/test') 

@artist_bp.route('', methods=['GET', 'POST'])
def artist():
    artists = Artist.query.all()
    comments = Comment.query.all()

    user_id = current_user.get_id()
    user = User.select_user_by_id(user_id)
    # artist_id = Artist.select_artist_by_id(Artist.id)
    form = CommentForm(request.form)

    if request.method == 'POST' and form.validate():
        new_comment = Comment(user_id, form.to_artist_id.data, user.username, form.comment.data) # user.username
        with db.session.begin(subtransactions=True):
            new_comment.create_comment()
        db.session.commit()
        flash("Your comment has been added!", "success")
    return render_template('artist/artist.html', artists=artists, comments=comments, user=user, form=form)

@test_bp.route('')
def test():
    return render_template('artist/test.html')