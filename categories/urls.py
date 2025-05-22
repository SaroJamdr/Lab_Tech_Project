
from django.urls import path
from .views import category_list, create_category_view, category_edit, category_delete

urlpatterns = [
    path('categories/', category_list, name='categories_list'),
    path('categories/create', create_category_view, name='categories_create'),
    path('categories/edit/<int:pk>/', category_edit, name='categories_edit'),
    path('categories/delete/<int:pk>/', category_delete, name='categories_delete'),
    
]
