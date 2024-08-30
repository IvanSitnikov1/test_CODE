#### Тестовое задание CODE

#### Описание проекта:
Реализовано REST API на фреймворке FastAPI.  
Для передачи данных используется формат JSON.  
Созданы эндпоинты регистрации, логина и логаута пользователя, добавления заметок, вывода списка заметок конкретного пользователя.  
Данные хранятся в базе данных PostgreSQL.  
При сохранении заметок орфографические ошибки валидируются при помощи сервиса Яндекс.Спеллер. Ошибочные слова автоматически исправляются и в базу данных добавляется исправленный вариант.  
Сервис подготовлен для запуска в докер контейнерах.  

#### Протестировать сервис можно на странице документации
http://127.0.0.1:9999/docs

### Запуск проекта:
docker compose up --build