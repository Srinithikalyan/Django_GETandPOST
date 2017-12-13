from django.contrib.auth.models import User
from django.http import Http404
from models import Employee
from serializers import EmployeeSerializer, DisplaySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, status

class DisplayView(viewsets.ModelViewSet):
    model = Employee
    serializer_class = DisplaySerializer

    def get_queryset(self):
        return Employee.objects.filter()

class EmployeeView(viewsets.ModelViewSet):
    model = Employee
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter()

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        objects = Employee.objects.get(**filter_kwargs)
        serializer = DisplaySerializer(objects)
	print("ghhhhhhhhhhhhhhhhhhhhhh")
        return Response({'employee_details': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Successfully Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Successfully Updated"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


