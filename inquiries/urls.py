
from django.urls import path
from .views import inquiry_view, create_inquiry_view

urlpatterns = [
    path('inquiries/', inquiry_view, name='inquiries'),
    path('inquiry/', create_inquiry_view, name='inquiry'),
    
]
