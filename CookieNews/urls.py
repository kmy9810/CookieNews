from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import user.views
from posting import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('posting.urls')),
    path('', include('bookmark.urls')),
    path('', include('comment.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 경로 추가
