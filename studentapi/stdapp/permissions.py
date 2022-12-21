from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_student and request.user.is_active


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_teacher and request.user.is_active


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser and request.user.is_active
