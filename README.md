# Трекер задач

Данное Django приложение предоставляет api для управления задачами.

### API

Пример данных

{"name": "Task1",
 "project": "Project1",
 "status": "Created",
 "performer": "User1",
 "author": "User1",
 "description": \["Description1", "Description2"\]}

PUT /tasks/create - создание задачи;
GET /tasks/info/{task_id} - получение информации о задаче;
POST /tasks/update - обновление задачи;
DELETE /tasks/delete - удаление задачи;
GET /tasks/filter - фильтрация задачи;

PUT /comments/create - создание комментария;
GET /tasks/info/{task_id} - получение информации о задаче;
POST /tasks/update - обновление задачи;
DELETE /tasks/delete - удаление задачи;
GET /tasks/filter - фильтрация задачи;

### Запуск приложения

`$ docker-compose build web`

`$ docker-compose run web`

После этого приложение будет запущено на 0.0.0.0:8000

Либо можно запустить с помощью

`$ python manager.py runserver 0.0.0.0:8000`

### Другие версии Python

Чтобы изменить версию питона, надо просто в Dockerfile в первой строке изменить версию питона на желаемую
