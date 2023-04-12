from django.contrib import admin
from django.urls import path, include

import user.views
from posting import views

urlpatterns = [
    path('save-posting/', views.save_posting, name='save-posting'),
    path('detail-posting/<int:id>', views.detail_posting, name='detail-posting'),
    path('posting-list/<str:id>', views.posting_list_view, name='posting-list'),
]