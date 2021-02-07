from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Majors.views import MajorViewSet


router = DefaultRouter()
router.register('majors', MajorViewSet, basename='Majors-list')

app_name = 'Majors'

urlpatterns = [
    path('', include(router.urls)),
]