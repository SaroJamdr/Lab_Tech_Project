from rest_framework import serializers
from ..models import Social_media

class SocialMediaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields= '__all__'

class SocialMediaRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = '__all__'

class SocialMediaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = ('title', 'link', 'image')