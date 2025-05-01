from rest_framework import viewsets
from ..serializers.banners_serializer import BannerSerializer
from ..models import Banner
from rest_framework.permissions import IsAdminUser

class BannerViewSet(viewsets.ModelViewSet):
    permission_classes= [IsAdminUser,]
    queryset= Banner.objects.all().order_by('-id')
    serializer_class = BannerSerializer

    def create(self, request, *args, **kwargs):
        old_banner = Banner.objects.first()
        if old_banner:
            old_banner.delete()

        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        Banner.objects.exclude(pk=kwargs['pk']).delete()
        return super().update(request, *args, **kwargs)

    