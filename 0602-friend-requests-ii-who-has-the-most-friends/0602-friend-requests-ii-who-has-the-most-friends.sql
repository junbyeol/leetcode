# Write your MySQL query statement below
WITH Friends AS (
    SELECT
        requester_id AS id,
        COUNT(accepter_id) AS friends
    FROM RequestAccepted
    GROUP BY requester_id UNION ALL
    SELECT
        accepter_id AS id,
        COUNT(requester_id) AS friends
    FROM RequestAccepted
    GROUP BY accepter_id
)
SELECT id, SUM(friends) AS num
FROM Friends
GROUP BY id
ORDER BY num DESC
LIMIT 1