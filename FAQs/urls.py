from django.urls import path
from .views import faq_list, create_faq_view, faq_edit, faq_delete

urlpatterns = [
    path('faqs/', faq_list, name='faq_list'),
    path('faqs/create', create_faq_view, name='faq_create'),
    path('faqs/edit/<int:pk>/', faq_edit, name='faq_edit'),
    path('faqs/delete/<int:pk>/', faq_delete, name='faq_delete'),
]
