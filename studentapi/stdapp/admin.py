from django.contrib import admin
from .models import Student, User
# Register your models here.


@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    class Meta:
        model = Student
        list_display = "__all__"


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    class Meta:
        model = User
        list_display = "__all__"
