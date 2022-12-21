from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import Student
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from .models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# def get_user_model():
#     return User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('email', 'firstname', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            firstname=validated_data['firstname'],

        )

        user.set_password(validated_data['password'])
        user.save()

        return user


# User serializer


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
