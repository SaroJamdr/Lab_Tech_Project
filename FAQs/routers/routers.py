from ..viewsets.faq_viewsets import FAQViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('faqs', FAQViewSet, basename='faqsViewsets')