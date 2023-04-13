from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
        
    blog = models.CharField(max_length=256, default='')
    email = models.CharField(max_length=256, default='')
    imgUrl = models.ImageField(null=True, upload_to="", blank=True)  # 이미지 컬럼 추가
    comment = models.CharField(max_length=256, default='')
    birth = models.DateTimeField(verbose_name="Birth Created", null=True)

    def __str__(self):
        return self.username
