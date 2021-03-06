# Wargaming.net Task - Сервис рассылки сообщений

## Задание
```
Авторизованный пользователь попадает на страницу с формой, в которой он
вводит email адрес, время отправки и сообщение. В указанное время на
введенный email уходит сообщение в виде html письма. Плюс к этому
прикрутить простенькое API c парой эндпоинтов: информация по списку
юзеров - api/users/ (юзернейм, дата регистрации); информация по
сообщениям - api/messages/ (текст сообщения, статус: ожидает|отправлено).

задание со звездочкой:
•  уметь фильтровать сообщения по статусу (api/messages/?status=waiting) через созданное API
•  Просматривать статус celery тасков в джанговской админке.

Можно подумать, стоит ли использвать кэширование в данном проекте, если
стоит, то где именно. Также проект стоит создавать с использованием
virtualenv
```

## Реализация

Для реализации, по условиям задания, взяты [Django 1.10.3](https://www.djangoproject.com/ "Джанго фреймворк") и [Celery 4.0.0](http://www.celeryproject.org/ "Celery распределенная очередь заданий") на [Python 3.5.2](https://www.python.org/ "Python").
В качестве бекенда для [Celery](http://www.celeryproject.org/ "Celery распределенная очередь заданий") был выбран [Redis](https://redis.io/ "Redis нереляционная высокопроизводительная СУБД").

Отправка сообщений происходит по адресу `/email_send/`, пользователь должен быть авторизован. Ручки API находятся согласно задания.
Email сообщения отправляются в консоль, время отправки сообщений нужно вводить по UTC+0:00

### URL'ы

* `/login/` - авторизация
* `/logout/` - выход
* `/register/` - регистрация нового пользователя
* `/admin/` - Django админка
* `/email_send/` - отправка сообщений


## Запуск решения

1. `apt-get install redis`, `yum install redis`, ... - установка Redis
2. `pip install -e .` - установка проекта
3. `wghw/manage.py collectstatic` - собрка статики
4. `wghw/manage.py migrate` - применение миграций
5. `wghw/manage.py runserver` - запуск WEB сервера
6. `celery -A wghw worker -l info` - запуск Celery

Дополнитльно:
* `wghw/manage.py loaddata demo` - (необязательно) Создается пользователь с логином `test` и паролем `asdasd123`, несколько отправленных и неотправленных сообщений от его имени.
* `wghw/manage.py test` - запуск тестов
