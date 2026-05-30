# Write your MySQL query statement below
WITH MostRates AS (SELECT
    u.name AS user_name
FROM MovieRating mr
JOIN Users u ON u.user_id = mr.user_id
GROUP BY u.user_id
ORDER BY COUNT(mr.movie_id) DESC, user_name ASC
LIMIT 1),
BestFeb AS (
    SELECT m.title AS title
    FROM movieRating mr
    JOIN Movies m ON m.movie_id = mr.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mr.movie_id
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
)
SELECT user_name AS results FROM MostRates UNION ALL
SELECT title AS results FROM BestFeb