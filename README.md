# Кинобиблиотека на Esmerald

## Инструменты
- Python 3.12
- Esmerald
- Edgy
- Postgres
- Alembic
- Docker


### Запустить сборку
```shell
docker-compose up --build
```

## Alembic создание migrations
Не выключая контейнеры выполнить команду
```shell
docker exec -it movie-api edgy migrate
```

### Перейти по адресу
```
http:\\127.0.0.1:8000\docs\swagger
```
