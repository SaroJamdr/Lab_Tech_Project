from rest_framework import serializers
from ..models import Branch
import re

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'  # Include all fields from the Branch model

    phone = serializers.CharField()
    def validate_phone_number(self, value):
        pattern =  r'^\+[1-9]\d{1,3}\d{7,12}$'
        
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError("Enter a valid phone number with country code, e.g., +9779801234567.")
            
        return value

    def validate_gps_location(self, value):
        try:
            latitude_str, longitude_str = value.split(',')
            latitude = float(latitude_str)
            longitude = float(longitude_str)
        except ValueError:
            raise serializers.ValidationError("GPS location must be in the format 'latitude,longitude'.")

        # Validate latitude
        if latitude < -90 or latitude > 90:
            raise serializers.ValidationError("Latitude must be between -90 and 90 degrees.")

        # Validate longitude
        if longitude < -180 or longitude > 180:
            raise serializers.ValidationError("Longitude must be between -180 and 180 degrees.")

        return value