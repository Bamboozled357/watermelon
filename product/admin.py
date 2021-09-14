from django.contrib import admin

# Создать модель Product c полями: title, description, price и зарегистрировать его в админ панели.
from product.models import Product

admin.site.register(Product)
