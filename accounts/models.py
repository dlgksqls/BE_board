from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("이메일은 필수 값입니다.")

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # 비밀번호는 나만 알아야함.. 데이터베이스에 해싱해서 들어감
        user.save()

    def create_user(self, username, email=None, password=None, **extra_fields):  # 일반 유저
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):  # 슈퍼 유저
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name="이름", max_length=20)
    nickname = models.CharField(verbose_name="닉네임", max_length=50)
    password = models.CharField(verbose_name="비밀번호", max_length=50)
    email = models.EmailField(verbose_name="이메일", unique=True)

    objects = UserManager()

    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
