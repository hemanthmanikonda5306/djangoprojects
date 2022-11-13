from django.urls import path,include
from rest_framework import routers
router = routers.DefaultRouter()
from viewsetcrudapp.views import View_views
router.register(r'Viewsets',View_views,basename='viewsetscrud')

urlpatterns = [
    path('',include(router.urls))
]