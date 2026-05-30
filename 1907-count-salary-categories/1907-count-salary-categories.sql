# Write your MySQL query statement below
WITH Categorized AS (
    SELECT
        account_id,
        income,
        CASE WHEN income < 20000 THEN 'Low Salary'
            WHEN 20000 <= income AND income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary' END AS category
    FROM Accounts A
),
Labels AS(
    SELECT 'Low Salary' AS category UNION
    SELECT 'Average Salary' AS category UNION
    SELECT 'High Salary' AS category
)
SELECT l.category, COUNT(account_id) AS accounts_count
FROM Categorized c 
RIGHT JOIN Labels l ON l.category = c.category
GROUP BY l.category