# Write your MySQL query statement below
(
    SELECT employee_id, department_id
    FROM Employee e
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1
) UNION (
    SELECT employee_id, department_id
    FROM Employee e
    WHERE primary_flag = 'Y'
)