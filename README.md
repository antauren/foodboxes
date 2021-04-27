# foodboxes

API-сервис доставки товарных наборов (учебный проект на Python3)

### Установить зависимости

```
pip install -r requirements.txt
```

### Выполните миграцию данных

```
cd foofboxes
python manage.py migrate
```

### Запустите сервер

```
python manage.py runserver
```

### Загрузить тестовые данные

```
python manage.py load_users -u https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json
python manage.py load_items -u https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json
python manage.py load_reviews -u https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json
```

### Откройте тестовый пример

```
http://127.0.0.1:8000/api/v1/items/5/
```
