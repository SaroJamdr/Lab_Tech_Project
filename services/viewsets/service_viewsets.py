from rest_framework import viewsets
from ..serializers.service_serializer import ServiceSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models import Service
from categories.serializers.categories_serializer import CategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset= Service.objects.all().order_by('-id')
    serializer_class = ServiceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields= ['name',]
    ordering_fields = '__all__'
    

