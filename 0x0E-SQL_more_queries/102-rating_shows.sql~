-- 102-rating_shows.sql
-- Lists all shows from hbtn_0d_tvshows_rate by their rating

-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- Select each show's title and the sum of their ratings
SELECT tv_shows.title, SUM(rate) as rating
FROM tv_shows
JOIN tv_shows_ratings ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
