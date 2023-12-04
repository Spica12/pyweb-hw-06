## Python WEB Homework-06 "Work with SQL Database"

1) В Docker завантажити образ **postgres**

```
docker pull postgres
```

2) В Docker створити контейнер **pyweb_hw_06** з postgres DB:

```
docker run --name pyweb_hw_06 -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres
```

3) Увійти в контейнер **pyweb_hw_06**

```
docker exec -it pyweb_hw_06 bash
```

4) Зайти під користувачем postgres

```
psql-U postgres
```

5) Створити пусту базу даних **pyhomedb**

```
CREATE DATABASE pyhomedb;
```

6) Створити таблиці в базі даних, для цього треба запустити файл **create_tables.py**

```
cd pyweb_hw_06
py create_tables.py
```

7) Заповнити базу даних фейковивими даними для тестування, для цього треба запустити файл **fill_data.py**

```
py fill_data.py
```
