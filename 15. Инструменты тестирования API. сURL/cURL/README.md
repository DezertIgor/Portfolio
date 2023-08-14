# Объект тестирования:

[ToDo List](https://sky-todo-list.herokuapp.com/)

![](./Задание%202%20Демо.png)

## Задача:

Отправить cURL-запросы для всех составленных тест-кейсов через терминал.

1. Операция: Получение списка задач.

Curl-запрос:

```bash
curl https://todo-app-sky.herokuapp.com/ -H 'Content-Type: application/json' | json_pp
```

Результат выполнения команды в GitBash:

```bash
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
100 81 100 81 0 0 159 0 --:--:-- --:--:-- --:--:-- 159
[
{
"completed" : false,
"id" : 70269,
"order" : null,
"title" : "фывфв",
"url" : "/70269"
}
]
```

2. Операция: Создание новой задачи.

Curl-запрос:

```bash
curl https://todo-app-sky.herokuapp.com/ -X POST -H 'Content-Type: application/json' -d '{"title":"Zadacha"}' | json_pp
```

Результат выполнения команды в GitBash:

```bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    95  100    76  100    19    187     46 --:--:-- --:--:-- --:--:--   235
{
   "completed" : false,
   "id" : 91686,
   "order" : null,
   "title" : "Zadacha",
}
```

3. Операция: Отметка о выполнении задачи.

Curl-запрос:

```bash
curl https://todo-app-sky.herokuapp.com/70282 -X PATCH -H 'Content-Type: application/json' -d '{"completed":"true"}' | json_pp
```

Результат выполнения команды в GitBash:

```bash
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    95  100    75  100    20    162     43 --:--:-- --:--:-- --:--:--   206
{
   "completed" : true,
   "id" : 70282,
   "order" : null,
   "title" : "Zadacha",
   "url" : "/70282"
}
```

4. Операция: Удаление задачи.

Curl-запрос:

```bash
curl https://todo-app-sky.herokuapp.com/70282 -X DELETE -H 'Content-Type: application/json' | json_pp
```

Результат выполнения команды в GitBash:

```bash
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
0 0 0 0 0 0 0 0 --:--:-- --:--:-- --:--:-- 0
malformed JSON string, neither array, object, number, string or atom, at character offset 0 (before "(end of string)") at /usr/bin/core_perl/json_pp line 59.
```
