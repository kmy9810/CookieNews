from django.contrib import admin
from .models import PostingModel
from embed_video.admin import AdminVideoMixin

class PostingAdmin(AdminVideoMixin, admin.ModelAdmin):
    #list_display = ('posting_title', 'posting_video')
    pass

admin.site.register(PostingModel, PostingAdmin)
