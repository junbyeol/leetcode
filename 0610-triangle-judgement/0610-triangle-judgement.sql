# Write your MySQL query statement below
SELECT
    x,
    y,
    z,
    IF(x+y<=z or x+z<=y or y+z<=x, 'No', 'Yes') AS triangle
FROM Triangle