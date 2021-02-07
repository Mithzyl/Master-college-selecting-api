from django.shortcuts import render
from django.utils import timezone

from rest_framework import viewsets, permissions, generics
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

    @action(methods='GET', detail=False)
    def get(self):

        return Response(self.serializer.data)