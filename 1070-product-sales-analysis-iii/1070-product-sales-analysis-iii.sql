# Write your MySQL query statement below

WITH FirstYear AS (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) 
SELECT
    s.product_id,
    f.first_year,
    quantity,
    price
FROM FirstYear f
    JOIN Sales s
    ON s.product_id = f.product_id
    AND s.year = f.first_year