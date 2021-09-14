
from django.contrib import admin
from django.urls import path

from product import views

urlpatterns = [
    path('', views.product_list),
    path('details/<int:pk>/', views.product_detail),
    path('create/', views.product_create),
    path('edit/<int:pk>/', views.product_edit),
    path('delete/<int:pk>/', views.product_delete),
]
