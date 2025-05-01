from ..viewsets.gallery_viewsets import GalleryViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router= DefaultRouter()
router.register('gallery', GalleryViewSet, basename='galleryViewsets')
