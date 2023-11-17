# project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from mini.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='product-list'),
]
