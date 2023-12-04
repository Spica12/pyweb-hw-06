-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT p.subject, s.name, ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings as r
JOIN students as s ON r.student_id = s.id
JOIN subjects as p ON r.subject_id = p.id
WHERE p.id = 2
GROUP BY p.subject, s.name
ORDER BY avg_rating DESC
LIMIT 1;
