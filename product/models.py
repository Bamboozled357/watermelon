from django.db import models

# Создать модель Product c полями: title, description, price и зарегистрировать его в админ панели.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)

# Создать записи в БД
# После создания таблицы с полями, нужно в терминале сделать миграции. Это и будет процесс создания записей в БД.
# python3 manage.py makemigrations и python3 manage.py migrate
