from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('log-out/', views.log_out_view, name='log-out'),
    path('profile/', views.profile_view, name='profile'),
    #로그인한 유저를 삭제하기때문에 id 필요하지 않음
    path('delete-user/', views.delete_user_view, name='delete-user'),
    #로그인한 유저의 프로필을 변경하기때문에 id 필요하지 않음
    path('edit-user/', views.edit_user_view, name='edit-user'),
    ]
