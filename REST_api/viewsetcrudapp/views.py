from django.shortcuts import render
from rest_framework import status,permissions,viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from viewsetcrudapp.models import View_crud
from viewsetcrudapp.serializers import View_serializers

# Create your views here.
class View_views(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self,request):
        view = View_crud.objects.all()
        view_seria = View_serializers(view,many=True)
        return Response(view_seria.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):
        view = get_object_or_404(View_crud,pk=pk)
        view_seria = View_serializers(view)
        return Response(view_seria.data,status=status.HTTP_200_OK)
    def create(self,request):
        view_seria = View_serializers(data=request.data)
        if view_seria.is_valid(raise_exception=True):
            view_seria.save()
            return Response(view_seria.data,status=status.HTTP_201_CREATED)
        return Response(view_seria.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk):
        view = get_object_or_404(View_crud,pk=pk)
        view_seria = View_serializers(view,data=request.data)
        if view_seria.is_valid(raise_exception=True):
            view_seria.save()
            return Response(view_seria.data,status=status.HTTP_200_OK)
    def delete(self,request,pk):
        view = get_object_or_404(View_crud,pk=pk)
        view.delete()
        return Response({'msg':'done'},status=status.HTTP_204_NO_CONTENT)
