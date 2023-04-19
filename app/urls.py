from django.contrib import admin
from django.urls import path, include
from app import views as app
from . import views
from .views import TraSuaList, TraSuaDetail

urlpatterns = [
    path('', app.login),
    path('check_login/', app.view_check_login, name='check_login'),
    path('tra_sua_list/', TraSuaList.as_view(), name='tra_sua_list'),
    path('tra_sua/<int:pk>/', TraSuaDetail.as_view, name='tra_sua'),
]