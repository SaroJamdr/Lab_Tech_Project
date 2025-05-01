from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework import serializers
from django.core.mail import send_mail

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user with this email found.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        token = get_random_string(length=32)  # Generate a token
        # Here you would save the token to the database or send it via email
        send_mail(
            'Password Reset Request',
            f'Use this token to reset your password: {token}',
            'from@example.com',
            [email],
            fail_silently=False,
        )

class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate_token(self, value):
        # Validate the token (check if it exists and is valid)
        return value

    def save(self):
        token = self.validated_data['token']
        new_password = self.validated_data['new_password']
        # Here you would find the user by the token and reset the password
        user = User.objects.get(...)  # Find user by token
        user.set_password(new_password)
        user.save()