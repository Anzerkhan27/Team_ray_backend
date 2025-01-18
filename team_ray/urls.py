"""
URL configuration for team_ray project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from core.views import ProjectViewSet
from django.http import HttpResponse
from django.contrib.auth.models import User


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

from django.http import HttpResponse
from django.contrib.auth.models import User

def check_superuser(request):
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse("Superuser exists!")
    return HttpResponse("No superuser found.")





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('check-superuser/', check_superuser),
]
