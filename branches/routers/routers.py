from ..viewsets.branch_viewsets import BranchViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('branches', BranchViewSet, basename='branchesVisewsets')