-- 101-not_a_comedy.sql
-- Lists all shows without the genre Comedy in hbtn_0d_tvshows

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    -- Select show IDs with the genre Comedy
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
