from django.urls import path
from cbvapp.views import Cbvviews,Cbv_Detail


urlpatterns = [
    path('cbv/',Cbvviews.as_view()),
    path('cbv/<int:pk>',Cbv_Detail.as_view())

]