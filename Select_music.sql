-- Задание 2
--
-- Название и продолжительность самого длительного трека.

select name as "Наименование трека", duration / 60 as "Длительность, мин.,", duration % 60 as "сек."  from track
order by duration desc
limit 1;

--Название треков, продолжительность которых не менее 3,5 минут.

select name as "Наименование трека", duration / 60 as "Длительность, мин.,", duration % 60 as "сек."  from track
where duration >= 210
order by duration desc;

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.

select name as "Наименование сборника", year as "Год выхода сборника" from collection
where year > 2018 and year <= 2020
order by year;

-- Исполнители, чьё имя состоит из одного слова.

select nickname as "Исполнитель" from singer
where LENGTH(nickname) = 1;


-- Название треков, которые содержат слово «мой» или «my».

select name as "Наименование трека" from track
where name like '%my%' or name like '%мой%';

-- Задание 3
--
-- Количество исполнителей в каждом жанре

select name "Жанр", count(gs.singer_id) "Число исполнителей" from music_genre mg
join genres_singers gs on gs.genre_id = mg.genre_id
group by name;

--Количество треков, вошедших в альбомы 2019–2020 годов.

select count(t.track_id) "Число треков" from track t
join album a on t.album_id = a.album_id
where a.year between 2019 and 2020;

-- Средняя продолжительность треков по каждому альбому.

select a.name as "Альбом", AVG(t.duration ) "Ср. длительность треков, сек." from track t
join album a on t.album_id = a.album_id
group by a."name";

--Все исполнители, которые не выпустили альбомы в 2020 году.

select nickname from singer s 
join albums_singers as2 on as2.singer_id = s.singer_id
join album a on as2.album_id = a.album_id
where a."year" != 2020
group by nickname;


--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).

select c.name from collection c
join tracks_collections tc on tc.collection_id = c.collection_id
join track t on t.track_id = tc.track_id
join album a on t.album_id = a.album_id
join albums_singers as2 on as2.album_id = a.album_id
where as2.singer_id = (select singer_id from singer where nickname = 'Louis Armstrong')
group by c.name;


 