from flask import Blueprint, render_template

album_bp = Blueprint('album', __name__, url_prefix='/album')

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

@album_bp.route('')
def album():
    return render_template('album/album.html', album_list=album_list)
