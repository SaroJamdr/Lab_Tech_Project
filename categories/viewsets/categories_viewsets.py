from rest_framework import viewsets
from ..serializers.categories_serializer import CategorySerializer, SubCategorySerializer
from ..models import Category
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes= [IsAdminUser,]
    queryset = Category.objects.filter(parent__isnull=True).order_by('-id')
    
    filter_backends = (SearchFilter,)
    search_fields = ['category']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset