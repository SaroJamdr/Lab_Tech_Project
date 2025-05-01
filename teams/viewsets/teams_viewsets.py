from rest_framework import viewsets
from ..serializers.teams_serializer import TeamsSerializer
from ..models import Team
from ..utilities.pagination import MyPageNumberPagination
from rest_framework.permissions import IsAdminUser

class TeamViewSet(viewsets.ModelViewSet):
    queryset= Team.objects.all().order_by('-id')
    serializer_class = TeamsSerializer
    permission_classes= [IsAdminUser,]
    pagination_class= [MyPageNumberPagination]
    