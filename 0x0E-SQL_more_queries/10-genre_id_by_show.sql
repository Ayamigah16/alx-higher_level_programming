-- 10-genre_id_by_show.sql
-- Lists all shows with at least one genre linked in the hbtn_0d_tvshows database

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
