# Пример проекта на Fastapi
## Подготовка
*Рекомендуется* создать виртуальную перед использованием
```bash
python -m venv venv
source venv/bin/activate
```
Установите библиотеки
```bash
pip install - r requirements.txt
```
## Использование
Запустите сервер с помощью
```
fastapi dev server.py
```
По умолчанию сервер запустится на http://127.0.0.1:8000
Чтобы послать на него запрос можно воспользоваться браузером или утилитой ```client.py```
```bash
python client.py --request-method post add_new_user --parameter "Alice&AAA&Bob"
```
Команда выше создаст нового юзера в БД. В аргументе ```--parameter``` указаны "параметры" к запросу. В данном случае мы пошлем POST запрос на адрес ```http://127.0.0.1:8000/add_new_user/Alice&AAA&Bob```. Запрос имеет 3 параметра отделенные друг от друга знаком ```&```. Они вписываются в столбцы БД ```pp```, ```administrant``` и ```defendant``` соответственно.

Всего реализовано 3 запроса:
#### Создать пользователя
```bash
python client.py --request-method post add_new_user --parameter "Alice&AAA&Bob"
```
#### Получить всех пользователей
```bash
python client.py get_all_users
```
#### Получить пользователя по id
```bash
python client.py get_user 0
```
