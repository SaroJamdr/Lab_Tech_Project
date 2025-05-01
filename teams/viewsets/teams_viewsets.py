from rest_framework import viewsets
from ..serializers.teams_serializer import TeamsSerializer
from ..models import Team

class TeamViewSet(viewsets.ModelViewSet):
    queryset= Team.objects.all().order_by('-id')
    serializer_class = TeamsSerializer
    