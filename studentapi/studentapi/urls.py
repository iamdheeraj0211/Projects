"""studentapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from stdapp.views import StudentViewset1
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register("stdapi", StudentViewset1)

# router1 = routers.DefaultRouter()
# router1.register("su", SignupView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("stdapp.urls")),
    # path("", include(router1.urls)),

    path("access_token/", TokenObtainPairView.as_view()),
    path("refresh_token/", TokenRefreshView.as_view()),
    path("verify_token/", TokenVerifyView.as_view()),


]
urlpatterns += router.urls
