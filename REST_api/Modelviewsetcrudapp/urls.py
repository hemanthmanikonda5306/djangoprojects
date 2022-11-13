from django.urls import path,include
from rest_framework import routers
router = routers.DefaultRouter()
from Modelviewsetcrudapp.views import Model_Views
router.register(r'Mvsc',Model_Views,basename='Modelviewsetcrud')


urlpatterns = [
    path('',include(router.urls))
]