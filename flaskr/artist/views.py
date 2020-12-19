from flask import Blueprint, render_template

artist_bp = Blueprint('artist', __name__, url_prefix='/artist') 

@artist_bp.route('')
def artist():
    return render_template('artist/artist.html')
  