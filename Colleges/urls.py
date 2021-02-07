from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Colleges.views import CollegesView

router = DefaultRouter()
router.register(r'Colleges', CollegesView, basename='Colleges-list')

app_name = 'Colleges'

urlpatterns = [
    path('', include(router.urls))
]
