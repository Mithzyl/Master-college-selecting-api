from rest_framework import viewsets, mixins, authentication, status, permissions
from rest_framework.response import Response

from Users.serializers import RegisterUserSerializer, UserDetailSerializer

from Users.models import User


class CreateUserView(viewsets.GenericViewSet,
                     mixins.CreateModelMixin):
    serializer_class = RegisterUserSerializer
    # authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

