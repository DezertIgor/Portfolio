# Объект тестирования:

[Хост для нагрузки](https://httpbin.org/post)

## Задача:
Написать нагрузочный тест, используя JMeter, для метода запроса POST и тела запроса 
```
{ "user": "jmeter", "ver": 2 }
```

## Требования:

Тест необходимо запускать через командную строку без использования графического интерфейса JMeter.
Параметры количества потоков (vu), задержки между потоками (ramp-up) и количества повторений (loop)
должны передаваться через командную строку.
Отчёт по нагрузочному тестированию должен формироваться автоматически и сохраняться в папку "web".
Для ответов от сервера применяются проверки статус-кода и наличия в теле ответа ключа "json.user" со значением
"jmeter".

![](./Демо%201%20JMeter.png)
![](./Демо%202%20JMeter.png)
![](./Демо%203%20JMeter.png)


Запуск теста (non-GUI):
```
jmeter.bat -n -t Nagruzka.jmx -l otchet.log -e -o web -Jvu=15 -Jloop=5 -Jramp-up=10
```
![](./Демо%204%20Запуск%20non-UI.png)

[Нагрузочный тест](./Nagruzka.jmx)
![](./Демо%205%20Отчёт%20о%20нагрузочном%20тестировании.png)

[Отчет о нагрузочном тестировании](./index.html)
![](./Демо%206%20Логи.png)