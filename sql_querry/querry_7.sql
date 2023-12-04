-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT su.subject, g.name_group, st.name, r.rating
FROM ratings as r
JOIN subjects AS su ON su.id = r.subject_id
JOIN students AS st ON st.id = r.student_id
JOIN groups AS g ON g.id = st.group_id
WHERE g.id = 1 AND su.id = 2
GROUP BY su.subject, g.name_group, st.name, r.rating
