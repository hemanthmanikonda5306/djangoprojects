
from django.shortcuts import render
from rest_framework import status,permissions,viewsets,generics
from rest_framework.permissions import IsAuthenticated

from genericrouterapp.models import Groute
from genericrouterapp.serializers import Gr_serializers

# Create your views here.
class Groute_views(viewsets.ViewSetMixin,generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Groute.objects.all()
    serializer_class = Gr_serializers
    permission_classes = [permissions.AllowAny]