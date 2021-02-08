from django.shortcuts import render
from django.utils import timezone

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Favorites.serializers import FavoriteCollegesSerializer, FavoriteMajorsSerializer
from Favorites.models import FavoriteMajors, FavoriteColleges


class FavoriteCollegesView(viewsets.ModelViewSet):
    """
    Manage favorite colleges in database
    """

    serializer_class = FavoriteCollegesSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    # return current user only
    def get_object(self):
        return self.request.user

    def get_queryset(self):
        queryset = FavoriteColleges.objects.filter(user=self.request.user.id)

        return queryset

    def create(self, request, *args, **kwargs):

        return super().create(request, args, kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = FavoriteColleges.objects.filter(user=self.request.user.id, base=kwargs['pk'])

        self.perform_destroy(instance)

        return Response({'detail': '删除成功'}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)


class FavoriteMajorsView(viewsets.ModelViewSet):
    """
    Manage favorite majors in dataset
    """

    serializer_class = FavoriteMajorsSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    # return current user only
    def get_object(self):
        return self.request.user

    def get_queryset(self):
        queryset = FavoriteMajors.objects.filter(user=self.request.user.id)

        return queryset


