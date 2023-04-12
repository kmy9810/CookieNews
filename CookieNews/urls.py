from django.contrib import admin
from django.urls import path, include

import user.views
from posting import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('save-posting', views.save_posting, name='save-posting'),
    path('', include('bookmark.urls')),
]
