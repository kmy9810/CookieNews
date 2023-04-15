from django.db import models
from user.models import UserModel
from posting.models import PostingModel


# Create your models here.
class CommentModel(models.Model):
    class Meta:
<<<<<<< HEAD
        db_table = "my_comment"
=======
        db_table = "my_comment"  # 테이블 이름을 정해준다!
>>>>>>> 89d52a665f21893691e84ac15bb5b92e5cc35cbf

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)   # UserModel을 참조하는 외래키
    posting = models.ForeignKey(PostingModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=20)

<<<<<<< HEAD
def __str__(self):
    return self.comment


=======
    def __str__(self):
        return self.comment
>>>>>>> 89d52a665f21893691e84ac15bb5b92e5cc35cbf
