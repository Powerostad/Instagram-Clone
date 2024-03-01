from django.contrib import admin
from .models import PostViewLog, StoryViewLog, ProfileViewLog
# Register your models here.


@admin.register(PostViewLog)
class PostViewLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'post',
        'created_at',
    )
    list_display_links = (
        'id',
        'user',
        'post',
    )
    list_filter = (
        'user',
        'post',
        'created_at',
    )


@admin.register(StoryViewLog)
class StoryViewLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'story',
        'created_at',
    )
    list_display_links = (
        'id',
        'user',
        'story',
    )
    list_filter = (
        'user',
        'story',
        'created_at',
    )


@admin.register(ProfileViewLog)
class ProfileViewLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'profile',
        'created_at',
    )
    list_display_links = (
        'id',
        'user',
        'profile',
    )
    list_filter = (
        'user',
        'profile',
        'created_at',
    )
