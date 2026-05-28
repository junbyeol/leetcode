# Write your MySQL query statement below
-- SELECT s.student_id, s.student_name, j.subject_name
SELECT s.student_id, s.student_name, j.subject_name, COUNT(e.student_id) as attended_exams
FROM Students s
    CROSS JOIN Subjects j
    LEFT JOIN Examinations e ON e.student_id = s.student_id AND j.subject_name = e.subject_name
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name