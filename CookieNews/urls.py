from django.contrib import admin
from django.urls import path, include

from posting import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('save-posting', views.save_posting, name='save-posting'),
]
