from flask import Blueprint, render_template

song_bp = Blueprint('song', __name__, url_prefix='/song')

class SongInfo:
    def __init__(self, year, nameF, nameL, nameJ, title, titleJ, words, music, desc, singer_desc, youtube, band, icon_pic_path, song_pic_path, singer_pic_path):
        self.year = year
        self.nameF = nameF
        self.nameL = nameL
        self.nameJ = nameJ
        self.title = title
        self.titleJ = titleJ
        self.words = words
        self.music = music
        self.desc = desc
        self.singer_desc = singer_desc
        self.youtube = youtube
        self.band = band
        self.icon_pic_path = icon_pic_path
        self.song_pic_path = song_pic_path
        self.singer_pic_path = singer_pic_path
    
song_list = [
    SongInfo(1982, 'Eiichi', 'Ohtaki', '大瀧 詠一', 'Kimi wa Tennen Shoku', '君は天然色', 'Takashi Matsumoto', 'Eiichi Ohtaki',
        'The best of Japanese pop song! This one of the Ohtaki\'s most popular song is included on the album "A long vacation". ' +
        'Lyricist Takashi Matsumoto said everything he saw had lost its color after losing his sister. ' +
        'The lyrics reflect his feelings for her. Amazingly, the sound is a one-shot recording like Phil Spector did.',
        'Eiichi Ohtaki (July 28, 1948 – December 30, 2013) was a Japanese musician, songwriter and record producer.' +
        'He first became known as a member of the rock band Happy End, but was better known for his solo work which began in 1972.',
        'https://www.youtube.com/embed/dH9yLGoIxBw', 'Happy End', 'image/icon1.jpg', 'image/s1.jpg', 'image/p-ohtaki.jpg'),
    SongInfo(1980, 'Tatsuro', 'Yamashita', '山下 達郎', 'Ride On Time', 'ライド・オン・タイム', 'Tatsuro Yamashita', 'Tatsuro Yamashita',
        'Tatsuro\'s first big hit, a very popular and iconic city pop song! You can feel the uplifting feeling from the start of the song.' +
        'Not only Tatsuro\'s voice, but also Minako Yoshida\'s chorus is wonderful. And do not miss the soul-style slow number on the B-side, "Rainy Walk".',
        'Yamashita Tatsuro (February 4, 1953) is a Japanese singer-songwriter and record producer' +
        'who helped pioneer the style of Japanese adult-oriented rock/soft rock dubbed "city pop". He has also collaborated with his wife Mariya Takeuchi.',
        'https://www.youtube.com/embed/1rdlHKioR6A', 'Suger Babe', 'image/icon2.jpg', 'image/s2.jpg', 'image/p-yamashita.jpg')
]

@song_bp.route('/')
def song():
    return render_template('song/song.html', song_list=song_list)
  