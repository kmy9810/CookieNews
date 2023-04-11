from django.db import models
from user.models import UserModel


# Create your models here.
class PostingModel(models.Model):
    class Meta:
        db_table = "my_board"

    posting_author = models.ForeignKey(UserModel, on_delete=models.CASCADE)   # UserModel을 참조하는 외래키
    posting_category = models.CharField(max_length=10)
    posting_title = models.CharField(max_length=20)
    posting_content = models.TextField()
    posting_created = models.DateTimeField(blank=True, null=True, verbose_name="Posting Created", auto_now_add=True)
    # posting_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)


def __str__(self):
    return self.posting_created
