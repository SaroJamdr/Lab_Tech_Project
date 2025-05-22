from django.urls import path
from .viewsets.otp_viewsets import PasswordResetAPIView, PasswordResetRequestAPIView, OTPVerificationAPIView

urlpatterns = [
    path('account/password-reset-request/', PasswordResetRequestAPIView.as_view(), name='password-reset-request'),
    path('account/otp-verify/', OTPVerificationAPIView.as_view(), name='otp-verify'),
    path('account/password-reset/', PasswordResetAPIView.as_view(), name='password-reset'),
]