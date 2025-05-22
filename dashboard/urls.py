from django.urls import path
# from .viewsets.dashboard_viewsets import DashboardView
from .views import dashboard_view, appointment_view, group_list
from .viewsets.services_viewsets import service_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard_admin'),
    path('appointments/', appointment_view, name='appointments'),
    path('services/', service_view, name='services'),
    path('groups/', group_list, name='group_list'),
]
