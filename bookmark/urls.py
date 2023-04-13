from django.urls import path
from . import views

urlpatterns = [
    path('save-bookmark/<int:id>', views.save_bookmark_view, name='save-bookmark'),
    path('bookmark/<int:id>', views.bookmark_view, name='bookmark'),
]
