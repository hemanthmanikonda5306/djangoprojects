from django.urls import path,include
from rest_framework import routers
router = routers.DefaultRouter()
from genericrouterapp.views import Groute_views

router.register(r'gvroute',Groute_views,basename='Genericviewsroutercrud')


urlpatterns = [
    path('',include(router.urls))
]