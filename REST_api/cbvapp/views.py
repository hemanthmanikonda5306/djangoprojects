from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from cbvapp.models import Cbv
from cbvapp.serializers import CbvSerializers


# Create your views here.

class Cbvviews(APIView):
    def get(self, request):
            cbv = Cbv.objects.all()
            cbvser = CbvSerializers(cbv,many=True)
            return Response(cbvser.data, status=status.HTTP_200_OK)
    def post(self,request):
        cbv = CbvSerializers(data=request.data)
        if cbv.is_valid(raise_exception=True):
            cbv.save()
            return Response(cbv.data,status=status.HTTP_201_CREATED)
        return Response(cbv.errors,status=status.HTTP_400_BAD_REQUEST)


class Cbv_Detail(APIView):
    def get_object(self,pk):
        try:
            return Cbv.objects.get(pk=pk)
        except Cbv.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        cbv = self.get_object(pk)
        cbvser = CbvSerializers(cbv)
        return Response(cbvser.data)

    def put(self,request,pk):
        cbv = self.get_object(pk)
        cbvser = CbvSerializers(cbv,data=request.data)
        if cbvser.is_valid(raise_exception=True):
            cbvser.save()
            return Response(cbvser.data,status=status.HTTP_200_OK)
        return Response(cbvser.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        cbv = get_object_or_404(Cbv,pk=pk)
        cbv.delete()
        return Response({'msg':'done'},status=status.HTTP_204_NO_CONTENT)
