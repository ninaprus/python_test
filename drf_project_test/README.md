# python_test

**Встановлення**
```python
pip install -r requirements.txt
python manage.py migrate
python manage.py import_products_csv 
python manage.py import_reviews_csv 
```

**Запуск сервера**

```python
python manage.py runserver
```

**URLconf**
```console
admin/
products/ products/<int:pk>/
reviews/ create_review/<int:product_id>/
```