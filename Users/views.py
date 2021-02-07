from rest_framework import viewsets, mixins, authentication, status, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Users.serializers import UserRegisterSerializer, UserDetailSerializer

from Users.models import User


class CreateUserView(viewsets.GenericViewSet,
                     mixins.CreateModelMixin):
    serializer_class = UserRegisterSerializer
    # authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Manage user detail
    """
    serializer_class = UserDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()

    @action(methods=['GET'], detail=True)
    def get_object(self):
        return self.request.user


class UserUpdateInfoView(viewsets.ModelViewSet, generics.UpdateAPIView):
    serializer_class = UserDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        user_instance = self.get_object()
        serializer = UserDetailSerializer(instance=user_instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        results = serializer.save()

        return Response(UserDetailSerializer(results).data)



