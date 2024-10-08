## **Задача:**

### **Стабилизируйте автотесты из Практикума № 9 «Библиотека Requests» на методы:**

- [GET] /employee
- [POST] /employee
- [GET] /employee/{id}
- [PATCH] /employee/{id}

Добавьте в тесты методы работы с БД, которые создают, удаляют, редактируют и вычитывают записи из БД.

**Строка подключения к БД:** 

postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0

**Таблица из БД:** "employee"


**Требования:**

1. Тесты должны работать с библиотекой `pytest`.
2. Тесты должны использовать библиотеку `Requests`.
3. Тесты должны использовать библиотеку `SQLAlchemy`.
    - Дополнительно установите библиотеку `psycopg2-binary`.
4. Тесты должны предварительно создавать себе тестовые данные через обращение к БД.
5. Тесты должны удалять за собой созданные данные через обращение к БД.
6. Тесты должны быть стабильны:
    - их не нужно редактировать перед каждым запуском;
    - повторный запуск теста приводит к тому же статусу.

Если сервис не получает запросы 30 минут, он выключается. Первое обращение к сервису потребует больше времени (около 2 минут), т. к. сервис запускается заново. Учитывайте это при работе.

**Swagger:** https://x-clients-be.onrender.com/docs/

**URL приложения:** https://x-clients-be.onrender.com
