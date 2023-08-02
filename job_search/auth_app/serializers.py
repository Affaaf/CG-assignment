from rest_framework import serializers
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'full_name', 'first_name', 'last_name']


class SigninSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
