# urls.py

from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
]