from django.contrib import admin
from .models import Board
from accounts.models import User

# Register your models here.
admin.site.register(Board)
admin.site.register(User)
