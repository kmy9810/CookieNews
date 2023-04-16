from django.db import models
from user.models import UserModel


# Create your models here.
class PostingModel(models.Model):
    class Meta:
        db_table = "my_board"

    posting_author = models.ForeignKey(UserModel, on_delete=models.CASCADE)   # UserModel을 참조하는 외래키
    categorys = (
        ('뉴스피드', '뉴스피드'),
        ('자유게시판', '자유게시판'),
    )
    posting_category = models.CharField(choices=categorys, max_length=10)
    posting_title = models.CharField(max_length=20)
    posting_content = models.TextField()
    posting_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    posting_img = models.ImageField(null=True, upload_to="", blank=True)  # 이미지 컬럼 추가
    posting_video = models.URLField(null=True, blank=True)
    posting_views = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.posting_title

