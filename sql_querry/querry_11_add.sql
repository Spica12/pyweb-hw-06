-- Середній бал, який певний викладач ставить певному студентові.

SELECT st.name, t.name, ROUND(AVG(r.rating)) AS avg_rating
FROM ratings AS r
JOIN students AS st ON st.id = r.student_id
JOIN subjects AS su ON su.id = r.subject_id
JOIN teachers AS t ON t.id = su.teacher_id
WHERE st.id = 10 AND t.id = 5
GROUP BY st.name, t.name;
