from ..viewsets.service_viewsets import ServiceViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('services', ServiceViewSet, basename='services')