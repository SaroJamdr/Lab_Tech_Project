from rest_framework import viewsets
from ..serializers.appointment_serializer import AppointmentListSerializer, AppointmentWriteSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from ..models import Appointment
from ..utilities.permissions import AppointmentPermission

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset= Appointment.objects.all().order_by('-id')
    serializer_class = AppointmentListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes= [AppointmentPermission,]
    search_fields= ['name','email' ]
    ordering_fields = '__all__'
    
    def get_queryset(self):
        return super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create']:
            return AppointmentWriteSerializer
        return super().get_serializer_class()