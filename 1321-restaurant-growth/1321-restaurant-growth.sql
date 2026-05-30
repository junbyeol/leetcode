# Write your MySQL query statement below
WITH DailyAmount AS (
    SELECT
        visited_on,
        SUM(amount) AS tot,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS visit_rank
    FROM Customer
    GROUP BY visited_on
),
AllOutput AS (SELECT
    visited_on,
    SUM(tot) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount,
    ROUND(AVG(tot) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) as average_amount,
    visit_rank
FROM DailyAmount
ORDER BY visited_on ASC
)
SELECT visited_on, amount, average_amount FROM AllOutput WHERE visit_rank >= 7
