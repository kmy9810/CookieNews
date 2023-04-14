from django.urls import path
from posting import views

urlpatterns = [
    path('save-posting/', views.save_posting, name='save-posting'),
    path('detail-posting/<int:id>', views.detail_posting, name='detail-posting'),
    path('posting-list/<str:id>', views.posting_list_view, name='posting-list'),
    path('delete-posting/<str:id>', views.delete_posting, name='delete-posting'),
    path('edit-posting/<str:id>', views.edit_posting, name='edit-posting'),
]