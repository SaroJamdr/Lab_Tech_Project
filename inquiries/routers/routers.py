from ..viewsets.inquiries_viewsets import InquiryViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('inquiries', InquiryViewSet, basename='inquiriesViewsets')