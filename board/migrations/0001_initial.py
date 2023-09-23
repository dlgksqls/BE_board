# Generated by Django 4.2.3 on 2023-09-23 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('images', models.ImageField(blank=True, upload_to='', verbose_name='사진')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
