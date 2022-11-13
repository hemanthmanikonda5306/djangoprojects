from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from simplejwt.views import home,Simpleviews
router = routers.DefaultRouter()

router.register(r'simplejwt',Simpleviews,basename='SIMPLEJWT')

urlpatterns = [
    path('simple/',home),
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]