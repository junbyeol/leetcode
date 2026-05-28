# Write your MySQL query statement below
WITH TotalPlayer AS (
    SELECT COUNT(*) FROM (SELECT COUNT(*) FROM Activity GROUP BY player_id) t
),
FirstLogin AS (
    SELECT MIN(event_date) AS first_login, player_id FROM Activity GROUP BY player_id
)

SELECT ROUND(
    COUNT(*) / (SELECT * FROM TotalPlayer)
    ,2) AS fraction
FROM (
    SELECT
        a.player_id
    FROM FirstLogin f
    JOIN Activity a
        ON DATE_ADD(f.first_login, INTERVAL 1 DAY) = a.event_date
        AND f.player_id = a.player_id
    WHERE a.event_date IS NOT NULL
    GROUP BY f.player_id
) x
