from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"

class SignupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')


        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
