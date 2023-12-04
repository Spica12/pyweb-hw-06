-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

-- SELECT MAX(r.date_of) as last_date, g.name_group, st.name, su.subject, r.rating
-- FROM ratings as r
-- JOIN students AS st ON st.id = r.student_id
-- JOIN subjects AS su ON su.id = r.subject_id
-- JOIN groups AS g ON g.id = st.group_id
-- WHERE g.id = 1 AND su.id = 3
-- GROUP BY g.name_group, st.name, su.subject, r.rating

SELECT MAX(r.date_of) as last_date, g.name_group, st.name, su.subject, r.rating
FROM ratings as r
JOIN students AS st ON st.id = r.student_id
JOIN subjects AS su ON su.id = r.subject_id
JOIN groups AS g ON g.id = st.group_id
WHERE g.id = 2 and r.subject_id = 3
GROUP BY g.name_group, su.subject, st.name, r.rating;
