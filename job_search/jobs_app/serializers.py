from rest_framework import serializers
from .models import Application, Post
from auth_app.serializers import SignupSerializer


class PostSerializer(serializers.ModelSerializer):

    user = SignupSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'post_text', 'created_at', 'user']


class ApplicationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Application
        fields = "__all__"