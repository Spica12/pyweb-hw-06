-- Знайти які курси читає певний викладач.
SELECT t.name, s.subject
FROM subjects as s
JOIN teachers as t ON t.id = s.teacher_id
WHERE t.id = 5
GROUP BY t.name, s.subject
