from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from .permissions import IsAuthenticatedUserOrReadOnly
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [
        IsAuthenticatedUserOrReadOnly,
    ]
















