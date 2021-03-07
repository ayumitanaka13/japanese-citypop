-- SQLite

DELETE FROM comments;

INSERT INTO comments (id, from_user_id, to_artist_id, comment, create_at, update_at, username, picture_path)
VALUES (1, 1, 1, "It is very good that many people begin to know Eiichi Ohtaki by Kakushigoto anime, he is one of the best City Pop singers in Japan.", "2020-12-20 15:53:04.943453", "2020-12-20 15:53:04.943453", "Amy", "image_user/1_1609734421.jpg");

INSERT INTO comments (id, from_user_id, to_artist_id, comment, create_at, update_at, username, picture_path)
VALUES (2, 2, 1, "I love his works so much! 'Kimi wa Tennen Shoku' sounds like the breeze in the summer and a little sadness inside.", "2020-12-21 15:53:04.943453", "2020-12-21 15:53:04.943453", "John", "image_user/2_1609734344.jpg");

INSERT INTO comments (id, from_user_id, to_artist_id, comment, create_at, update_at, username, picture_path)
VALUES (3, 2, 2, "I do not care how people found this man, just glad that he gets even more popular as the years go by.", "2020-12-22 15:53:04.943453", "2020-12-22 15:53:04.943453", "John", "image_user/2_1609734344.jpg");