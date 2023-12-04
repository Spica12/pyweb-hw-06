-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.name student, ROUND(AVG(r.rating), 2) avg_rating
FROM ratings as r
LEFT JOIN students as s ON r.student_id = s.id
GROUP BY s.name
ORDER BY avg_rating DESC
LIMIT 5;
