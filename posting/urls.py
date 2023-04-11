from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('save-posting/', views.save_posting, name='save-posting'),
    # path('posting-list/<str:id>', views.posting_list, name='posting-list'),
]