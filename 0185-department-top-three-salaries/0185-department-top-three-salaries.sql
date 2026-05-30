# Write your MySQL query statement below
WITH SalaryRank AS
(
    SELECT
        id,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as salary_rank
    FROM Employee
)
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN SalaryRank s ON s.id = e.id
JOIN Department d ON d.id = e.departmentId
WHERE s.salary_rank <= 3