from django.contrib import admin
from django.urls import path, include

from landing_api import views

urlpatterns = [
    path('', views.LandingAPI.as_view(), name='landing-api'),
    path('index/', views.LandingAPI.as_view(), name='landing-index'),
]