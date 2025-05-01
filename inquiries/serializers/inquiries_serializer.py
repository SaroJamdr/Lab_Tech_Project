from rest_framework import serializers
from ..models import Inquiry
import re

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ('id', 'name', 'email', 'message', 'phone')

    phone = serializers.CharField()
    def validate_phone(self, value):
        pattern =  r'^\+[1-9]\d{1,3}\d{7,12}$'
        
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError("Enter a valid phone number with country code, e.g., +9779801234567.")
            
        return value