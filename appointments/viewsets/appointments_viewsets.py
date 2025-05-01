from rest_framework import viewsets
from ..serializers.appointment_serializer import  AppointmentSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from ..models import Appointment

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset= Appointment.objects.all().order_by('-id')
    serializer_class = AppointmentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields= ['name','email' ]
    ordering_fields = '__all__'
    
 
