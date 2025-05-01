from rest_framework import viewsets
from ..serializers.gallery_serializer import GallerySerializer
from ..models import Gallery

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-id')
    serializer_class = GallerySerializer