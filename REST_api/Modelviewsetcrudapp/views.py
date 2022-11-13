from django.shortcuts import render
from Modelviewsetcrudapp.models import Model_crud
from Modelviewsetcrudapp.serializers import Model_serializers
from rest_framework import permissions,viewsets
# Create your views here.



class Model_Views(viewsets.ModelViewSet):
    queryset = Model_crud.objects.all()
    serializer_class = Model_serializers
    permission_classes = [permissions.AllowAny]