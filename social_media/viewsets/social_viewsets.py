from rest_framework import viewsets
from ..serializers.social_serializer import (
    SocialMediaListSerializer, SocialMediaRetriveSerializer, SocialMediaWriteSerializer

)
from ..models import Social_media
from rest_framework.permissions import IsAdminUser

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset= Social_media.objects.all().order_by('-id')
    serializer_class = SocialMediaListSerializer
    permission_classes= [IsAdminUser]

    
    def get_queryset(self):
        return super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SocialMediaWriteSerializer
        elif self.action == 'retrive':
            return SocialMediaRetriveSerializer
        return super().get_serializer_class()