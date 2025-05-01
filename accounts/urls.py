from django.urls import path
from .viewsets.otp_viewsets import PasswordResetAPIView, PasswordResetRequestAPIView, OTPVerificationAPIView

urlpatterns = [
    path('password-reset-request/', PasswordResetRequestAPIView.as_view(), name='password-reset-request'),
    path('otp-verify/', OTPVerificationAPIView.as_view(), name='otp-verify'),
    path('password-reset/', PasswordResetAPIView.as_view(), name='password-reset'),
]