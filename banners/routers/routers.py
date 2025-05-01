from ..viewsets.banner_viewsets import BannerViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('banners', BannerViewSet, basename='bannersViewsets')