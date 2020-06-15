"""Serializers for user models."""

from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for codeWOF users."""

    class Meta:
        """Meta settings for serializer."""

        model = User
        fields = (
            'pk',
            'email',
            'first_name',
            'last_name',
            'user_type',
        )
