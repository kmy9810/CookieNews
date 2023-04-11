from django.db import models

# Create your models here.
class PostingModel(models.Model):
    class Meta:
        db_table = "my_board"

    posting_id = models.IntegerField(max_length=10)
    posting_author = models.IntegerField(max_length=10)   # UserModel을 참조하는 외래키
    posting_category = models.CharField(max_length=10)
    posting_title = models.CharField(max_length=20)
    posting_content = models.TextField()
    posting_created = models.DateTimeField(auto_now_add=True)
