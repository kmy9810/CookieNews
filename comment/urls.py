from django.urls import path
from comment import views


urlpatterns = [
    path('delete-comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('edit-comment/<int:id>', views.edit_comment, name='edit_comment'),
]