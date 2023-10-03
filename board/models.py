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

    tag_common = models.ManyToManyField("Common_Tag", related_name="tag_common")
    tag_travel = models.ManyToManyField("Travel_Tag", related_name="tag_travel")
    tag_res = models.ManyToManyField("Res_Tag", related_name="tag_res")
    tag_cafe = models.ManyToManyField("Cafe_Tag", related_name="tag_cafe")

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Board", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Common_Tag(models.Model):
    common_tag = models.CharField(max_length=10, verbose_name="공통_태그")

    def __str__(self):
        return self.common_tag


class Travel_Tag(models.Model):
    travel_tag = models.CharField(max_length=10, verbose_name="여행지_태그")

    def __str__(self):
        return self.travel_tag


class Res_tag(models.Model):
    res_tag = models.CharField(max_length=10, verbose_name="식당_태그")

    def __str__(self):
        return self.res_tag


class Cafe_tag(models.Model):
    cafe_tag = models.CharField(max_length=10, verbose_name="카페_태그")

    def __str__(self):
        return self.cafe_tag
