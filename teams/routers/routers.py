from ..viewsets.teams_viewsets import TeamViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('teams', TeamViewSet, basename='teamsViewsets')