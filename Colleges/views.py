from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Colleges.models import Colleges
from Colleges.serializers import CollegesSerializer


class CollegesView(viewsets.ModelViewSet):
    queryset = Colleges.objects.all()
    serializer_class = CollegesSerializer(queryset, many=True)
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)


