from ..viewsets.appointments_viewsets import AppointmentViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointmentsViewsets')