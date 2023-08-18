В данном проекте реализован API, хранящий информацию о перевалах.


Модели:

Users (содержит информацию о пользователе: email, телефон, имя, отчество, фамилию).

Coords (содержит информацию о координатах перевала: ширину, долготу, высоту).

Photo (содержит информацию о фото).

Pereval_added (содержит информацию о перевале: название, описание, время добавления, уровень сложности; ссылку на пользователя, добавившего этот перевал; координаты; фото).


Методы:

`Pereval_addedAPICreate`

POST /`submitData`/ - добавление перевала 

GET`/submitData/?user__email=<email>` - получение списка перевалов с фильтром по email’у


`PerevalOne`

GET `/submitData/<id>` -  информация о перевале по id

PATCH `/submitData/<id>` - изменение информации о перевале (менять данные пользователя нельзя) 


Принимает JSON:
{
    "photos": [
        {
        "data": "https://altaitg.ru/upload/medialibrary/f87/f87987866560658cad63c54eda6160db.jpg",
        "title": "на закате"
    },
        {
        "data": "https://altaitg.ru/upload/medialibrary/f87/f87987866560658cad63c54eda6160db.jpg",
        "title": "начало"
    }
    ],
    "user": {
        "email": "email@gmail.com",
        "phone": 123123123,
        "name": "Иван",
        "patronimic": "Иванович",
        "last_name": "Иванов"
    },
    "coords": {
        "latitude": 23.23,
        "longitude": 23.23,
        "height": 2323
    },
    "beauty_title": "перевал",
    "title": "Даван",
    "other_titles": "Дабаан",
    "connect": "какой-нибудь текст",
    "winter_level": "1a",
    "autumn_level": "1a",
    "spring_level": "1a",
    "summer_level": "1a",
    "status": "new"
}


Установка

1) клонировать проект 

git clone https://github.com/IrinaKolner/DRF_pass.git

2) создать и активировать виртуальное окружение 

`python -m venv venv`

`source venv/bin/activate`

3) установить: 

`pip install django`

`pip install djangorestframework`

`pip install psycopg2-binary`

`pip install drf-writable-nested`

`pip install django-filter`

`pip install python-dotenv`

4) создать и применить миграции

`python manage.py makemigrations`

`python manage.py migrate`