# Write your MySQL query statement below
WITH LastDate AS (
    SELECT
        MAX(change_date) AS last_change,
        product_id
    FROM Products
    WHERE change_date < "2019-08-17"
    GROUP BY product_id
),
Updated AS (
    SELECT p.product_id, p.new_price AS price
    FROM Products p
    LEFT JOIN LastDate l ON l.product_id = p.product_id AND l.last_change = p.change_date
    WHERE last_change IS NOT NULL
)
(SELECT * FROM Updated) UNION (
    SELECT 
        p.product_id,
        10 AS price
    FROM Products p
    LEFT JOIN Updated u ON p.product_id = u.product_id
    WHERE u.product_id IS NULL
    GROUP BY p.product_id
)

