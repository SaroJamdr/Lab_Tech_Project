from django.urls import path
from .views import branch_list, create_branch_view, branch_edit, branch_delete

urlpatterns = [
    path('branch/', branch_list, name='branch_list'),
    path('branch/create', create_branch_view, name='branch_create'),
    path('branch/edit/<int:pk>/', branch_edit, name='branch_edit'),
    path('branch/delete/<int:pk>/', branch_delete, name='branch_delete'),
]
