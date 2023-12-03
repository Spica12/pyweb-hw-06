

Створити контейнер **pyweb_hw_06** з postgres DB:
```
docker run --name pyweb_hw_06 -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres
```

Увійти в контейнер **pyweb_hw_06**
```
docker exec -it pyweb_hw_06 bash
```

Зайти під користувачем postgres
```
psql-U postgres
```
