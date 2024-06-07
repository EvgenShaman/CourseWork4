from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import message, conversation, User_conv

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fielsd = ('id', 'email', 'name', 'password')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'

class convSerializer(serializers.ModelSerializer):
    class Meta:
        model = conversation
        fields = '__all__'

class connectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_conv
        fields = '__all__'