# project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from mini.views import ProductListView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
