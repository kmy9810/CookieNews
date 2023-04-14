from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('log-out/', views.log_out_view, name='log-out'),
    path('profile/<int:id>', views.profile_view, name='profile'),
    path('delete-user/', views.delete_user_view, name='delete-user'),

    ]
