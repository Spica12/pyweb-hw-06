-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT t.name, su.subject, ROUND(AVG(r.rating), 2) as avg_rating
FROM ratings as r
JOIN subjects AS su ON su.id = r.subject_id
JOIN teachers AS t ON t.id = su.teacher_id
WHERE t.id = 5
GROUP BY t.name, su.subject;
