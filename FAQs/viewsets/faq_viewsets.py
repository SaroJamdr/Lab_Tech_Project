from rest_framework import viewsets
from ..serializers.faq_serializer import (FAQSerializer
    # FAQListSerializer, FAQRetriveSerializer, FAQWriteSerializer

)
from ..models import FAQ
from rest_framework.permissions import IsAdminUser

class FAQViewSet(viewsets.ModelViewSet):
    queryset= FAQ.objects.all().order_by('-id')
    serializer_class = FAQSerializer
    permission_classes = [IsAdminUser]
    
    # def get_queryset(self):
    #     return super().get_queryset()
    #     return queryset
    
    # def get_serializer_class(self):
    #     if self.action in ['create', 'update', 'partial_update']:
    #         return FAQWriteSerializer
    #     elif self.action == 'retrive':
    #         return FAQRetriveSerializer
    #     return super().get_serializer_class()