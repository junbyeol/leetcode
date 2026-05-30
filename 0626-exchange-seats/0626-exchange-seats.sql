# Write your MySQL query statement below
SELECT
    id,
    IF(id % 2 = 1,
        LEAD(student, 1, student) OVER (ORDER BY id ),
        LAG(student, 1) OVER (ORDER BY id)
    ) AS student
FROM Seat