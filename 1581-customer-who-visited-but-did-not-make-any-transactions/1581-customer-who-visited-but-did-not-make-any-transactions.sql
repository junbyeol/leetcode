# Write your MySQL query statement below
SELECT customer_id, count(customer_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON t.visit_id = v.visit_id
WHERE transaction_id is null
GROUP BY customer_id