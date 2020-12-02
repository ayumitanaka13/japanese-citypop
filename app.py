from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

class AlbumInfo:
    def __init__(self, age, intro, number, year, name, nameJ, title, titleJ, desc, member1, member2, member3, album_pic_path, artist_pic_path):
        self.age = age
        self.intro = intro
        self.number = number
        self.year = year
        self.name = name
        self.nameJ = nameJ
        self.title = title
        self.titleJ = titleJ
        self.desc = desc
        self.member1 = member1
        self.member2 = member2
        self.member3 = member3
        self.album_pic_path = album_pic_path
        self.artist_pic_path = artist_pic_path
    
album_list = [
    AlbumInfo('EARLY 70s',
        'City pop was a popular trend in Japan from the late 70s to 80s. However, it is important to remember that there were already sources of city pop in the early 70s.',
        1, 1970, 'Happy End', 'はっぴいえんど', 'Happy End', 'はっぴいえんど',
        'This is an iconic piece of Japanese rock music history. Happy End is a pioneering band that put Japanese lyrics on the rock sound. ' +
        'In terms of perfection, it is inferior to their second album, "Kaze Machi Roman 風街ろまん", but it has the freshness of a debut album. ' +
        '"Juuni Gatsu No Ame No Hi 12月の雨の日", this classic song is a must listen.',
        'Eiichi Ohtaki', 'Haruomi Hosono', 'Shigeru Suzuki', 'image/1.jpg', 'image/1a.jpg'),
    AlbumInfo('LATE 70s',
        'In the late 70s, city pop started to become popular mainly in Tokyo and evolved further into the 80s. Numerous masterpieces were created during this period.',
        2, 1975, 'Suger Babe', 'シュガーベイブ','Songs', 'ソングス',
        'This masterpiece produced by Eiichi Ohtaki was the starting point for city pop. Sugar Babe is the legendary band that ' + 
        'Tatsuro Yamashita and Taeko Ohnuki were in. "Down Town ダウンタウン" is a famous song that a lot of artists have covered. ' + 
        'I always get excited just listening to this beautiful song. It never gets old.',
        'Tatsuro Yamashita', 'Taeko Ohnuki', 'Ginji Ito', 'image/2.jpg', 'image/2a.jpg'),
    AlbumInfo('EARLY 80s',
        'City pop was at its peak in the 80s. The Japanese economy was booming at the time and many hit songs were born. City pop sound was spreading into the popular music industry.',
        3, 1984, 'Mariya Takeuchi', '竹内まりや', 'Variety', 'ヴァラエティ',
        'This is a city pop classic that needs no explanation. As you know, one of her most popular songs, "Plastic Love プラスティック・ラブ" is on this album. ' +
        'Taeko Ohnuki contributedd background vocals on this song. Mariya wanted to change her image as a pop idol, and her husband Tatsuro did a great job of producing this album.',
        'Mariya Takeuchi', 'Tatsuro Yamashita', 'Taeko Ohnuki', 'image/3.png', 'image/3a.jpg')
]

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

@app.route('/') # main
def main():
    return render_template('main.html')

@app.route('/albumlist') # all albums
def load_album_list():
    return render_template('album_list.html', album_list=album_list)

@app.route('/songlist') # all songs
def load_song_list():
    return render_template('song_list.html', song_list=song_list)

@app.route('/terms') # terms
def terms_of_service():
    return render_template('terms.html')

@app.errorhandler(404) # redirect
def redirect_main_page(error):
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)