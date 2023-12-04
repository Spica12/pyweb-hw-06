-- Знайти середній бал у групах з певного предмета.
SELECT p.subject, g.name_group, ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings as r
JOIN students as s ON r.student_id = s.id
JOIN groups as g ON s.group_id = g.id
JOIN subjects as p ON r.subject_id = p.id
WHERE p.id = 3
GROUP BY p.subject, g.name_group
ORDER BY avg_rating DESC;
