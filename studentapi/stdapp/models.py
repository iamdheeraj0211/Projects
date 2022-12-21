from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, firstname, password, ** extra_fields):

        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("password must be provided")

        email = self.normalize_email(email)
        user = self.model(email=email,
                          firstname=firstname,
                          **extra_fields
                          )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  email, firstname, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_teacher",   True)

        # extra_fields.setdefault("role", "teacher")
        return self._create_user(email, firstname,  password,  ** extra_fields)

    def create_superuser(self, email, firstname,  password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        # extra_fields.setdefault("role", "admin")
        return self._create_user(email, firstname, password,  **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=250)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    is_staff = models.BooleanField(default=True)  # must for admin interface
    is_active = models.BooleanField(default=True)  # must
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class User(AbstractBaseUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
#     last_login = models.DateTimeField(null=True)


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.id} {self.fname} {self.lname} {self.course}"
