from django.urls import path
from .viewsets.dashboard_viewsets import DashboardView
from .views import dashboard_view

urlpatterns = [
    # path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard_admin'),
]
