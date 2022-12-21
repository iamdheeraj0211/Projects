from django.shortcuts import render
from .serializers import StudentSerializer, RegisterSerializer
from rest_framework import viewsets, generics, views, response, status
from .models import Student
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .permissions import IsStudent, IsTeacher, IsSuperUser
from rest_framework_simplejwt.views import TokenObtainPairView
# from django.contrib.auth.models import User

from .models import User

from django.contrib.auth import get_user_model


User = get_user_model()


class Registerview(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class StudentViewset1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTeacher | IsSuperUser | IsStudent]

# class ListStudentViewset(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsStudent | IsSuperUser | IsTeacher]


# class GetStudentViewset(generics.RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsSuperUser | IsStudent | IsTeacher]


# class CreateStudentViewset(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsSuperUser]


# class StudentViewset(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsTeacher | IsSuperUser]
