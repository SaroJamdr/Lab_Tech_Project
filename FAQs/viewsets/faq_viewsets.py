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
    