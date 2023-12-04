-- Список курсів, які певному студенту читає певний викладач.

SELECT t.name, st.name, su.subject
FROM ratings as r
JOIN students AS st ON st.id = r.student_id
JOIN subjects AS su ON su.id = r.subject_id
JOIN teachers AS t ON t.id = su.teacher_id
WHERE t.id = 3 AND st.id = 5
GROUP BY t.name, st.name, su.subject;
