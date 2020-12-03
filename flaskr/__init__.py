from flask import Flask

def create_app():
    app = Flask(__name__)
    from flaskr.album.views import album_bp
    from flaskr.song.views import song_bp

    app.register_blueprint(album_bp)
    app.register_blueprint(song_bp)
    return app