from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Favorites.views import FavoriteCollegesView

app_name = 'Favorites'

router = DefaultRouter()
router.register('colleges', FavoriteCollegesView, basename='colleges-list')

urlpatterns = [
    path('', include(router.urls))
]