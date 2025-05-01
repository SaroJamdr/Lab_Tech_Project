from rest_framework import viewsets
from ..serializers.branches_serializer import BranchSerializer
from ..models import Branch
from rest_framework.permissions import IsAdminUser

class BranchViewSet(viewsets.ModelViewSet):
    queryset= Branch.objects.all().order_by('-id')
    serializer_class = BranchSerializer
    permission_classes= [IsAdminUser]

    