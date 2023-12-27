-- 14-my_genres.sql
-- Lists all genres of the show Dexter from hbtn_0d_tvshows

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select genre names for the show Dexter
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
