from django.shortcuts import render
from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer,SignupSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class SnippetViewset(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SignUpAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer