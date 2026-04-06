# api_final
# API Yatube

Социальная сеть для публикации постов с возможностью комментирования и подписки на авторов.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yandex-praktikum/api-final-yatube-ad
cd api-final-yatube-ad
```
2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```
3.Установите зависимости:
```bash
pip install -r requirements.txt
```
4.Выполните миграции:
```bash
python manage.py migrate
```
5.Запустите сервер:
```bash
python manage.py runserver
```
