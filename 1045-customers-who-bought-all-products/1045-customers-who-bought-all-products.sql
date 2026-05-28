# Write your MySQL query statement below
SELECT customer_id
FROM
(SELECT customer_id, product_key FROM Customer GROUP BY customer_id, product_key) u
GROUP BY customer_id
HAVING COUNT(product_key) = (SELECT COUNT(*) FROM Product)