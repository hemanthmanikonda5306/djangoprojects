from django.urls import path
from fbvapp.views import fbv_crud,fbv_getpost

urlpatterns=[
    path('fbv/',fbv_getpost),
    path('fbv/<int:pk>',fbv_crud)
]