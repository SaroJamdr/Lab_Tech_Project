from django.urls import path
from .viewsets.dashboard_viewsets import DashboardView

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
]