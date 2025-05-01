from ..viewsets.social_viewsets import SocialMediaViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('social-media', SocialMediaViewSet, basename='socialMediaViewsets')