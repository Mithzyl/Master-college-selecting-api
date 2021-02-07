from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Users.views import CreateUserView, UserDetailView, UserUpdateInfoView

router = DefaultRouter()
# router.register(r'users/token', CreateTokenView, basename="create_token")
# router.register(r'users/token', obtain_jwt_token, basename="create_token")
router.register(r'create', CreateUserView, basename="users_create")
router.register(r'user/info', UserDetailView, basename="user_info")
router.register(r'update-info', UserUpdateInfoView, basename="update_user_info")

app_name = 'Users'

urlpatterns = [
    path('', include(router.urls)),
]