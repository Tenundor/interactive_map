# Куда пойти - Москва глазами Артёма

Интерактивная карта Москвы, на которой указаны различные виды активного отдыха
с подробными описаниями и комментариями. [Ссылка на работающий сайт для тестирования](https://tenundor2.pythonanywhere.com/)

<img width="70%" alt="screenshot" src="screenshots/ezgif.com-gif-maker_4nWhtfQ.gif">

## Установка

Для запуска у вас уже должен быть установлен Python 3.

- Скачайте код из репозитория GitHub
- Установите зависимости:

`pip install -r requirements.txt`

- Создайте файл базы данных SQLite:

`python3 manage.py migrate`

- Настройте переменные окружения в файле `.env` (см. ниже)
- Запустите разработческий сервер:

`python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта на локальном компьютере эти настройки не требуются**, значения уже проставлены по-умолчанию.

Доступны следующие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — список хостов/доменов, которые может обслуживать этот сайт. Перечисляются через запятую:

`ALLOWED_HOSTS=example1.com,example2.com`

## Наполнение БД тестовыми данными

Тестовые данные можно загрузить в БД из репозитория  [where-to-go-places](https://github.com/devmanorg/where-to-go-places) следующим образом:

- Перейдите в директорию [places](https://github.com/devmanorg/where-to-go-places/tree/master/places) репозитория
- Выберете файл, откройте его на отдельной странице и нажмите кнопку Raw. Так вы получите ссылку на исходный код файла. Скопируйте ссылку.
- В консоли выполните команду для загрузки данных, в качестве параметра передав ссылку на выбранный файл:

`python3 manage.py load_place http://адрес_файла`

## Доступ к панели администратора сайта

- Создайте суперпользователя:

`python3 manage.py createsuperuser`

- Убедитесь, что сервер запущен
- Перейдите по ссылке `http://127.0.0.1:8000/admin/`
- Введите логин и пароль пользователя

## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
