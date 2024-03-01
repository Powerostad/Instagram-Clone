from django.contrib import admin
from .models import Comment, Like
# Register your models here.

admin.site.register(Like)
admin.site.register(Comment)
