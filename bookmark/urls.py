from django.urls import path
from . import views

urlpatterns = [
    path('bookmark/<int:id>', views.bookmark_view, name='bookmark'),
]
