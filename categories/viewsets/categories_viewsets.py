from rest_framework import viewsets
from ..serializers.categories_serializer import CategorySerializer, SubCategorySerializer
from ..models import Category
from rest_framework.filters import SearchFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    
    filter_backends = (SearchFilter,)
    search_fields = ['category']