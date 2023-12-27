-- 103-rating_genres.sql
-- Lists all genres in the hbtn_0d_tvshows_rate database by their rating

-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- Select each genre's name and the sum of ratings for all shows in that genre
SELECT tv_genres.name, SUM(tv_show_ratings.rate) as rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
