from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, EmployeeSerializer
from .models import Employee


class CreateUserView(generics.CreateAPIView):
    '''Create a new User. This user might be used as for employee profile as for restaurant's admin too.'''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class CreateEmployeeView(generics.CreateAPIView):
    '''Create a new employee profile bonded with logged in user.'''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        request.data.update({"user": request.user})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
