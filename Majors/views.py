from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action

from Majors.models import Majors
from Majors.serializers import MajorsSerializer


class MajorViewSet(viewsets.ModelViewSet):
    """
    Manage majors in the dataset
    """
    serializer_class = MajorsSerializer
    authentication_classes = ()
    permission_classes = (permissions.AllowAny, )
    queryset = Majors.objects.all()

    @action(methods=['GET'], detail=False)
    def get_queryset(self):
        queryset = self.queryset
        classes = self.request.query_params.get('classes')
        if classes:
            queryset = self.queryset.filter(classes__contains=classes)

        return queryset
