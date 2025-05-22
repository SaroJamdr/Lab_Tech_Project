from django.urls import path
from .views import team_list, create_team_view, team_edit, team_delete

urlpatterns = [
    path('team/', team_list, name='team_list'),
    path('team/create', create_team_view, name='team_create'),
    path('team/edit/<int:pk>/', team_edit, name='team_edit'),
    path('team/delete/<int:pk>/', team_delete, name='team_delete'),
]
