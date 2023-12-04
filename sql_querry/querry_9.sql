-- Знайти список курсів, які відвідує студент.

SELECT st.name, su.subject
FROM ratings as r
JOIN students AS st ON st.id = r.student_id
JOIN subjects AS su ON su.id = r.subject_id
WHERE st.id = 10
GROUP BY st.name, su.subject;
