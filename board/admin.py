from django.contrib import admin
from .models import Board, Comment, Tag
from accounts.models import User


# Register your models here.
@admin.register(Board)
class BoardModelView(admin.ModelAdmin):
  list_display = ('title','writer','tag_list',)

  def tag_list(self, obj):
    return ','.join([t.tag_name for t in obj.tagging.all()])
  

admin.site.register(Comment)
@admin.register(Tag)
class TagModelView(admin.ModelAdmin):
  list_display = ('tag_name',)

admin.site.register(User)