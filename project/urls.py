"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country_data', views.country_data.as_view()),
    path('country_data1', views.country_data1.as_view()),
    path('person_data', views.person_data.as_view()),
    path('person_data1', views.person_data1.as_view()),
    path('pet_data', views.pet_data.as_view()),
    path('pet_data1', views.pet_data1.as_view()),
    path('vehicle_data', views.vehicle_data.as_view()),
    path('vehicle_data1', views.vehicle_data1.as_view()),
]
