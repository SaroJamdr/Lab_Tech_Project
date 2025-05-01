from rest_framework import viewsets
from ..serializers.service_serializer import ServiceSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from ..utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAdminUser

from ..models import Service
from categories.serializers.categories_serializer import CategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset= Service.objects.all().order_by('-id')
    serializer_class = ServiceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class= MyPageNumberPagination
    search_fields= ['name',]
    ordering_fields = '__all__'
    permission_classes= [IsAdminUser,]


# def get_queryset(self):
#         queryset = super().get_queryset()
#         category_filter = self.request.query_params.get('category', None)
#         subcategory_filter = self.request.query_params.get('sub_category', None)

#         if category_filter:
#             queryset = queryset.filter(category_id=category_filter)

#         if subcategory_filter:
#             queryset = queryset.filter(sub_category_id=subcategory_filter)

#         return queryset

