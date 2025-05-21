-- Добавляем жанры

INSERT into music_genre  (name)
VALUES ('Rock'), ('Jazz'), ('Pop'), ('Blues');

-- Добавляем исполнителей

INSERT into singer  (nickname)
VALUES ('Victor Tsoy'), ('Louis Armstrong'), ('B B King'), ('Madonna'), ('X');

-- Cоздаем и добавляем  связки Жанр - Исполнитель

INSERT into genres_singers (singer_id, genre_id)
select s.singer_id, m.genre_id  from singer s
join music_genre m on m.name = 'Rock'
where nickname = 'Victor Tsoy';

INSERT into genres_singers (singer_id, genre_id)
select s.singer_id, m.genre_id  from singer s
join music_genre m on m.name = 'Jazz'
where nickname = 'Louis Armstrong';

INSERT into genres_singers (singer_id, genre_id)
select s.singer_id, m.genre_id  from singer s
join music_genre m on m.name = 'Blues'
where nickname = 'B B King';

INSERT into genres_singers (singer_id, genre_id)
select s.singer_id, m.genre_id  from singer s
join music_genre m on m.name = 'Pop'
where nickname = 'Madonna';

INSERT into genres_singers (singer_id, genre_id)
select s.singer_id, m.genre_id  from singer s
join music_genre m on m.name = 'Pop'
where nickname = 'Victor Tsoy';

INSERT into genres_singers (singer_id, genre_id)
select s.singer_id, m.genre_id  from singer s
join music_genre m on m.name = 'Pop'
where nickname = 'X';

-- Создаем и добавляем альбомы

INSERT into album (name, year)
VALUES ('Erotica',1992), ('Black Album',1991), ('Night', 2022), ('My Jazz', 2012), ('Bad Blues', 2020), ('My music', 2018);

-- создаем связки Альбом-Исполнитель

INSERT into albums_singers (singer_id, album_id)
select s.singer_id, a.album_id  from singer s
join album a on a.name = 'Black Album'
where nickname = 'Victor Tsoy';

INSERT into albums_singers (singer_id, album_id)
select s.singer_id, a.album_id  from singer s
join album a on a.name = 'Erotica'
where nickname = 'Madonna';

INSERT into albums_singers (singer_id, album_id)
select s.singer_id, a.album_id  from singer s
join album a on a.name = 'Night'
where nickname in ('Madonna', 'Victor Tsoy');

INSERT into albums_singers (singer_id, album_id)
select s.singer_id, a.album_id  from singer s
join album a on a.name = 'My Jazz'
where nickname = 'Louis Armstrong';

INSERT into albums_singers (singer_id, album_id)
select s.singer_id, a.album_id  from singer s
join album a on a.name = 'Bad Blues'
where nickname = 'B B King';

INSERT into albums_singers (singer_id, album_id)
select s.singer_id, a.album_id  from singer s
join album a on a.name = 'My music'
where nickname = 'X';

-- Заполненяем таблицу с треками

INSERT into track (name, duration, album_id)
select 'Star', 268, a.album_id from album a
where a.name = 'Black Album';

INSERT into track (name, duration, album_id)
select 'Cuckoo', 400, a.album_id from album a
where a.name = 'Black Album';

INSERT into track (name, duration, album_id)
select 'Anthill', 318, a.album_id from album a
where a.name = 'Black Album';

INSERT into track (name, duration, album_id)
select 'War tomorrow', 35, a.album_id from album a
where a.name = 'Black Album';

INSERT into track (name, duration, album_id)
select 'Fever', 300, a.album_id from album a
where a.name = 'Erotica';

INSERT into track (name, duration, album_id)
select 'Rain', 324, a.album_id from album a
where a.name = 'Erotica';

INSERT into track (name, duration, album_id)
select 'War', 312, a.album_id from album a
where a.name = 'Night';

INSERT into track (name, duration, album_id)
select 'Tears', 305, a.album_id from album a
where a.name = 'Night';

INSERT into track (name, duration, album_id)
select 'Cabaret', 189, a.album_id from album a
where a.name = 'My Jazz';

INSERT into track (name, duration, album_id)
select 'Mop Mop', 124, a.album_id from album a
where a.name = 'My Jazz';

INSERT into track (name, duration, album_id)
select 'Past Day', 197, a.album_id from album a
where a.name = 'Bad Blues';

INSERT into track (name, duration, album_id)
select 'My song', 180, a.album_id from album a
where a.name = 'My music';

INSERT into track (name, duration, album_id)
select 'мой день', 120, a.album_id from album a
where a.name = 'My music';

INSERT into track (name, duration, album_id)
select 'The my track', 122, a.album_id from album a
where a.name = 'My music';

-- Создаем сборники

INSERT into collection  (name, year)
VALUES ('Best',2020), ('Top-5',2023), ('Hi load', 2024), ('Relax',2001);

-- Наполняем сборники треками

INSERT into tracks_collections (collection_id, track_id)
select c.collection_id, t.track_id from track t
join collection c on c.name = 'Best'
join album a on a.year  < c."year"
where t.album_id = a.album_id;

INSERT into tracks_collections (collection_id, track_id)
select c.collection_id, t.track_id from track t
join collection c on c.name = 'Top-5'
order by t.duration
limit 5;

INSERT into tracks_collections (collection_id, track_id)
select c.collection_id, t.track_id from track t
join collection c on c.name = 'Relax'
join album a on a.album_id = (select album_id 
                              from albums_singers 
                              where singer_id = 
                                               (select singer_id 
                                               from singer 
                                               where nickname = 'Louis Armstrong'
                                               )
                              )
where t.album_id = a.album_id;

INSERT into tracks_collections (collection_id, track_id)
select c.collection_id, t.track_id from track t
join collection c on c.name = 'Hi load'
where t.track_id % 2 = 0;

