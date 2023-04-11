from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
        
    blog = models.CharField(max_length=256, default='')
    email = models.CharField(max_length=256, default='')
    birth = models.DateTimeField(default='datetime.datetime.now')
    imgUrl = models.CharField(max_length=256, default='')
    comment = models.CharField(max_length=256, default='')

