from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Colleges.models import Colleges
from Colleges.serializers import CollegesSerializer


class CollegesView(viewsets.ModelViewSet):
    serializer_class = CollegesSerializer
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    queryset = Colleges.objects.all()

