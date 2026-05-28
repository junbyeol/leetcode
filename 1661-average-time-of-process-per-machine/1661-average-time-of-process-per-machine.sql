# Write your MySQL query statement below
WITH StartActivity AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'start'
),
EndActivity AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'end'
)

SELECT s.machine_id, ROUND(AVG(e.timestamp - s.timestamp), 3) as processing_time
FROM StartActivity s
    JOIN EndActivity e
    ON s.machine_id = e.machine_id
    AND s.process_id = e.process_id
GROUP BY s.machine_id