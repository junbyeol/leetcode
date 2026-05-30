# Write your MySQL query statement below
WITH AccWeight AS (
    SELECT
        turn,
        person_id,
        person_name,
        weight,
        SUM(weight) OVER (ORDER BY turn) AS acc
    FROM Queue q
    ORDER BY turn
)
SELECT person_name
FROM AccWeight a
WHERE acc <= 1000
ORDER BY acc DESC
LIMIT 1