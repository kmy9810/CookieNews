from django.db import models
from user.models import UserModel
from posting.models import PostingModel


# Create your models here.
class BookmarkModel(models.Model):
    class Meta:
        db_table = "my_bookmark"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)   # UserModel을 참조하는 외래키
    posting = models.ForeignKey(PostingModel, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, verbose_name="Posting Created", auto_now_add=True)


def __str__(self):
    return self.created
