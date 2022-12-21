from django.urls import path
from .views import *

urlpatterns = [

    path("register/", Registerview.as_view()),

    # path("std1/", ListStudentViewset.as_view()),
    # path("std1/<int:pk>", GetStudentViewset.as_view()),

    # path("std/", CreateStudentViewset.as_view()),
    # path("std/<int:pk>", StudentViewset.as_view()),





    # path("signup1/student/", SignupView1.as_view(), name="student_signup"),
    # path("signup1/teacher/", SignupView1.as_view(), name="teacher_signup"),



]
