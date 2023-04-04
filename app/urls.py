from django.contrib import admin
from django.urls import path, include
from app import views as app

urlpatterns = [
    path('', app.login),
    path('check_login/', app.view_check_login, name='check_login'),
]