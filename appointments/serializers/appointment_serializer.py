from rest_framework import serializers
from ..models import Appointment
from services.models import Service
import re
from categories.models import Category

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category',]

class ServiceDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['name', 'category', 'price']

class AppointmentWriteSerializer(serializers.ModelSerializer):
    service = ServiceDetailSerializer(many=True, read_only=True)
    category = serializers.CharField(max_length=255, required=False)
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone_number', 'address','gender', 'service', 'category',
                  'appointment_date', 'payment_method', 'message' ]


class AppointmentListSerializer(serializers.ModelSerializer):
    services = ServiceDetailSerializer(many=True, read_only=True)
    category = ServiceDetailSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    appointment_book = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = [
            'id', 'name', 'email', 'phone_number', 'address', 'gender', 'services', 'category',
            'total_price', 'appointment_date', 'payment_method','appointment_book', 'message'
        ]

    def get_total_price(self, obj):
        return sum(service.price for service in obj.services.all())
    
    def get_appointment_book(self, obj):
        if obj.payment_method == 'online':
            return 'online'
        else:
            return 'at clinic'


    def validate_phone_number(self, value):
        pattern =  r'^\+[1-9]\d{1,3}\d{7,12}$'
        
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError("Enter a valid phone number with country code, e.g., +9779801234567.")
            
        return value 