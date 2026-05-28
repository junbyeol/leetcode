# Write your MySQL query statement below
SELECT p.product_id, IFNULL(ROUND(SUM(price * units) / SUM(units), 2), 0) as average_price
FROM Prices p
LEFT JOIN UnitsSold u on u.purchase_date BETWEEN p.start_date AND p.end_date AND p.product_id = u.product_id
GROUP BY product_id