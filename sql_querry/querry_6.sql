-- Знайти список студентів у певній групі.

SELECT g.name_group, s.name
FROM students AS s
JOIN groups AS g ON g.id = s.group_id
WHERE g.id = 1
GROUP BY g.name_group, s.name;
