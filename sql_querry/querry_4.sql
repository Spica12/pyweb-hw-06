-- Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings as r;
