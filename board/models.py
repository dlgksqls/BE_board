from django.db import models
from accounts.models import User


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    images = models.ImageField(verbose_name="사진", blank=True)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    writer = models.ForeignKey(
        "accounts.User", verbose_name="작성자", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Board", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
