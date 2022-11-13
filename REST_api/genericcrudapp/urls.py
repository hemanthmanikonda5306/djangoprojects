from django.urls import path
from genericcrudapp.views import G_views,Gv_Crud


urlpatterns = [
    path('gviews/',G_views.as_view()),
    path('gviews/<int:pk>',Gv_Crud.as_view())
]