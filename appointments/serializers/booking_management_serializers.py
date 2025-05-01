from rest_framework import serializers
from ..models import Appointment
from services.serializers.service_serializer import ServiceSerializer

class BookingListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Appointment
        fieds= '__all__'
