from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from fbvapp.models import Fbv
from fbvapp.serializers import FbvSerializers

# Create your views here.
@api_view(['GET','POST'])
def fbv_getpost(request):
    if request.method == 'GET':
        fbv = Fbv.objects.all()
        fbvser = FbvSerializers(fbv,many=True)
        return Response(fbvser.data,status=status.HTTP_200_OK)
    else:
        fbvser = FbvSerializers(data=request.data)
        if fbvser.is_valid():
            fbvser.save()
            return Response()
@api_view(['GET','PUT','DELETE'])
def fbv_crud(request,pk):
    try:
        fbv = Fbv.objects.get(pk=pk)
    except Fbv.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        fbvser = FbvSerializers(fbv)
        return Response(fbvser.data)
    elif request.method == 'PUT':
        fbvser = FbvSerializers(fbv,data=request.data)
        if fbvser.is_valid():
            fbvser.save()
            return Response(fbvser.data)
        return Response(fbvser.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fbv.delete()
        return Response({'msg':'done'},status=status.HTTP_204_NO_CONTENT)


