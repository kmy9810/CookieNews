from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
        
    blog = models.CharField(max_length=256, default='', null=True, blank=True)
    email = models.CharField(max_length=256, default='', null=True, blank=True)
    imgUrl = models.ImageField(null=True, upload_to="", blank=True)  # 이미지 컬럼 추가
    comment = models.CharField(max_length=256, default='', null=True, blank=True)
    birth = models.DateTimeField(verbose_name="Birth Created")

    def __str__(self):
        return self.username
