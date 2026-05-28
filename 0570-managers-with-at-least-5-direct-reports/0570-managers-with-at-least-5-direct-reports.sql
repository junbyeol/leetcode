# Write your MySQL query statement below
WITH ManagerId AS (
    SELECT managerId
    FROM Employee e
    GROUP BY managerId
    HAVING count(id) >= 5
)
SELECT name
FROM Employee e
JOIN ManagerId m ON m.managerId = e.id