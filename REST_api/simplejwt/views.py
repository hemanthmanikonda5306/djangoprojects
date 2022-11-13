from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from simplejwt.models import Simple
from simplejwt.serializers import Simple_Serializers


# Create your views here.
def home(request):
    return HttpResponse('<h1>ANNAA EYYYYYYYYY</h1>')

class Simpleviews(viewsets.ModelViewSet):
    queryset = Simple.objects.all()
    serializer_class = Simple_Serializers
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            name = request.query_params.get('name',None)
            salary = request.query_params.get('salary',None)
            age = request.query_params.get('age',None)
            if name:
                queryset = queryset.filter(name = name)
            if salary:
                queryset = queryset.filter(salary__gte = salary)
            if age:
                queryset = queryset.filter(age__gte = age)

            serializers_data = self.get_serializer(queryset,many=True).data
            return Response(
                data={
                    'msg':'details displayed succesfully',
                    'details':serializers_data,
                    'success':True
                }
            )
        except Exception as error:
            return Response({
                'msg':str(error)},status=status.HTTP_400_BAD_REQUEST

            )



    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            with transaction.atomic():

                name = data.get('name',None)
                if name and Simple.objects.filter(name = name).exists():
                    raise Exception('Already Exists Take another name')

                name_records = Simple.objects.create(
                    name = name,
                    age = data.get('age',None),
                    role = data.get('role',None),
                    company = data.get('company',None),
                    salary = data.get('salary',None)
                )
                serializer_data = self.get_serializer(name_records).data
                return Response(
                    data={
                        'message':'details added successfully',
                        'details':serializer_data,
                        'success':True
                    }
                )


        except  Exception as error:
            return Response(
                {'message':str(error)},status=status.HTTP_400_BAD_REQUEST)



    def destroy(self, request, *args, **kwargs):
        data = request.data
        try:
            with transaction.atomic():
                name = self.get_object()
                if name:
                    name.delete()
                serializer_data = self.get_serializer(name).data

                return Response(
                    data={
                         'message':'details deleted successfully',
                         'details':serializer_data,              
                        'success':True   },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as error:
            return Response ( {'message':str(error)},status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, *args, **kwargs):
        data = request.data
        try:
            with transaction.atomic():
                name = self.get_object()
                if name:
                    name.name = data.get('name'),
                    name.age = data.get('age'),
                    name.role = data.get('role'),
                    name.company = data.get('company'),
                    name.salary = data.get('salary')

                serializer_data = self.get_serializer(name).data
                return Response(
                       data={
                            'message':'details updated successfully',
                            'details':serializer_data,
                           'success':True   },
                       status=status.HTTP_200_OK
                )
        except Exception as error:
            return Response ({'message':str(error)},status=status.HTTP_400_BAD_REQUEST)


