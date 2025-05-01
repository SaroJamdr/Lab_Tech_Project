from rest_framework import viewsets
from ..serializers.inquiries_serializer import InquirySerializer
from ..models import Inquiry
from rest_framework.filters import SearchFilter

class InquiryViewSet(viewsets.ModelViewSet):
    queryset= Inquiry.objects.all().order_by('-id')
    serializer_class = InquirySerializer
    filter_backends = (SearchFilter,)
    search_fields = ['name', 'email', 'phone',]
    