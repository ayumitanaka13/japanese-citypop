-- SQLite
DELETE FROM albums;

INSERT INTO albums (id, from_age_id, year, name, name_j, title, title_j, info, album_picture_path, artist_picture_path)
VALUES (1, 1, 1970, "Happy End", "はっぴいえんど", "Happy End", "はっぴいえんど",
        "This is an iconic piece of Japanese rock music history. Happy End is a pioneering band that put Japanese lyrics on the rock sound.
         In terms of perfection, it is inferior to their second album, 'Kaze Machi Roman 風街ろまん', but it has the freshness of a debut album.
         'Juuni Gatsu No Ame No Hi 12月の雨の日', this classic song is a must listen.",
        "image/1.jpg", "image/1a.jpg");

INSERT INTO albums (id, from_age_id, year, name, name_j, title, title_j, info, album_picture_path, artist_picture_path)
VALUES (2, 2, 1975, "Sugar Babe", "シュガーベイブ","Songs", "ソングス",
        "This masterpiece produced by Eiichi Ohtaki was the starting point for city pop. Sugar Babe is the legendary band that
         Tatsuro Yamashita and Taeko Ohnuki were in. 'Down Town ダウンタウン' is a famous song that a lot of artists have covered.
         I always get excited just listening to this beautiful song. It never gets old.",
        "image/2.jpg", "image/2a.jpg");

INSERT INTO albums (id, from_age_id, year, name, name_j, title, title_j, info, album_picture_path, artist_picture_path)
VALUES (3, 3, 1984, "Mariya Takeuchi", "竹内まりや", "Variety", "ヴァラエティ",
        "This is a city pop classic that needs no explanation. As you know, one of her most popular songs, 'Plastic Love プラスティック・ラブ' is on this album.
         Taeko Ohnuki contributedd background vocals on this song. Mariya wanted to change her image as a pop idol, and her husband Tatsuro did a great job of producing this album.",
        "image/3.png", "image/3a.jpg");
