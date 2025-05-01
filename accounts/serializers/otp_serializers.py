from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.core.cache import cache


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User  with this email does not exist.")
        return value

    def send_otp(self, email):
        user = User.objects.get(email=email)
        otp = str(random.randint(100000, 999999))
        # Store OTP in cache for 5 minutes
        cache.set(f'otp_{user.id}', otp, timeout=300)
        send_mail(
            "Password Reset OTP",
            f"Your OTP for password reset is {otp}",
            "sarojkhawas952@gmail.com",
            [user.email],
            fail_silently=False,
        )

class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        user = User.objects.get(email=data["email"])
        stored_otp = cache.get(f'otp_{user.id}')
        if stored_otp != data["otp"]:
            raise serializers.ValidationError("Invalid OTP.")
        return data

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.get(email=data["email"])
        stored_otp = cache.get(f'otp_{user.id}')
        if stored_otp is None:
            raise serializers.ValidationError("OTP verification required.")
        return data

    def save(self):
        user = User.objects.get(email=self.validated_data["email"])
        user.set_password(self.validated_data["new_password"])
        # Clear OTP from cache after successful reset
        cache.delete(f'otp_{user.id}')
        user.save()