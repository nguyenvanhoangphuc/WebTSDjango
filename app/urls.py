from django.contrib import admin
from django.urls import path, include
from app import views as app
from . import views
from .views import TraSuaList, TraSuaDetail, TraSuaCreate, TraSuaUpdate, TraSuaDelete

urlpatterns = [
    path('', app.login, name = 'login'),
    path('check_login/', app.view_check_login, name='check_login'),
    path('logout/', app.logout, name='logout'),
    path('tra_sua_list/', TraSuaList.as_view(), name='tra_sua_list'),
    # path('mua_tra_sua/<int:pk>/', TraSuaDetail.as_view(), name='mua_tra_sua'),
    path('mua_tra_sua/<int:tra_sua_id>/', app.them_don_hang, name='mua_tra_sua'),
    # path('tra_sua_create/', TraSuaCreate.as_view(), name='tra_sua_create'),
    path('tra_sua_create/', app.them_tra_sua, name='tra_sua_create'),
    # path('tra_sua_update/<int:pk>/', TraSuaUpdate.as_view(), name='tra_sua_update'),
    path('tra_sua_update/<int:tra_sua_id>/', app.cap_nhat_tra_sua , name='tra_sua_update'),
    path('tra_sua_update', app.cap_nhat_tra_sua, name='tra_sua_update'),
    path('tra_sua_delete/<int:pk>/', TraSuaDelete.as_view(), name='tra_sua_delete'),
    path('mua_all_tra_sua/', app.mua_all_tra_sua, name='mua_all_tra_sua'),
    path('don_hang_list/', views.don_hang_list, name='don_hang_list'),
    path('cap_nhat_don_hang/<int:don_hang_id>/', views.cap_nhat_don_hang, name='cap_nhat_don_hang'),
    path('xoa_don_hang/<int:don_hang_id>/', views.xoa_don_hang, name='xoa_don_hang'),
    path('xoa_all_don_hang/', views.xoa_all_don_hang, name='xoa_all_don_hang'),
]