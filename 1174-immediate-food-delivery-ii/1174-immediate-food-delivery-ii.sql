# Write your MySQL query statement below
WITH FirstOrder AS (
    SELECT
        customer_id,
        min(order_date) AS first_order
    FROM Delivery
    GROUP BY customer_id
)
SELECT
    ROUND(AVG(IF(d.order_date = d.customer_pref_delivery_date, 1, 0)) * 100, 2) AS immediate_percentage
FROM Delivery d
JOIN FirstOrder f ON f.first_order = d.order_date AND f.customer_id = d.customer_id