from django.contrib import admin
from .models import InstaPost, Media, Mention, Story, Tag
# Register your models here.


@admin.register(InstaPost)
class InstaPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'get_tags',
        'media_choice',
        'created_at',
        'updated_at',
        'is_active',
    )
    list_editable = (
        'media_choice',
        'is_active',
    )
    list_display_links = (
        'id',
        'user',
    )
    list_filter = (
        'tags',
        'created_at',
        'updated_at',
        'is_active',
        'media_choice',
    )
    search_fields = (
        'caption',
        'tags',
    )

    def get_tags(self, obj):
        return ", ".join([p.name for p in obj.tags.all()])


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'post',
        'media',
    )
    list_display_links = (
        'id',
    )


@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'post',
        'comment',
        'mentioned_user',
        'created_at',
    )
    list_display_links = (
        'id',
        'mentioned_user'
    )
    list_filter = (
        'created_at',
        'user',
        'mentioned_user',
        'post',
    )


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'context',
        'is_active',
        'created_at',
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'created_at',
        'is_active',
    )
    list_editable = (
        'is_active',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'is_active',
    )
    list_display_links = (
        'id',
        'name',
    )
    list_editable = (
        'is_active',
    )
    search_fields = ('name',)
