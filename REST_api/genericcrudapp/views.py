from rest_framework import generics,permissions
from genericcrudapp.models import Gen
from genericcrudapp.serializers import GvSerializers


class G_views(generics.ListCreateAPIView):
    queryset = Gen.objects.all()
    serializer_class = GvSerializers
    permission_classes = [permissions.AllowAny]



class Gv_Crud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gen.objects.all()
    serializer_class = GvSerializers
    permission_classes = [permissions.AllowAny]
