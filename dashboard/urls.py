from django.urls import path
from .viewsets.revenue_viewsets import RevenueChartAPIView

urlpatterns = [
    path('revenue', RevenueChartAPIView.as_view(), name='revenue-chart'),
]