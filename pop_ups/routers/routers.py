from ..viewsets.pop_up_viewsets import PopUpViewSet, PopUpDataViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('pop-ups', PopUpViewSet, basename='popUpViewsets')
router.register('pop-ups/data', PopUpDataViewSet, basename='popUpDataViewsets')