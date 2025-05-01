from ..viewsets.categories_viewsets import CategoryViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('categories', CategoryViewSet, basename='categoriesViewsets')