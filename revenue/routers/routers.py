
from rest_framework.routers import DefaultRouter
from ..viewsets.revenue_viewsets import RevenueViewSet

router = DefaultRouter()
router.register('revenue', RevenueViewSet, basename='revenue')