from django.contrib import admin
from .models import DirectMessage
# Register your models here.


@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sender',
        'receiver',
        'content_type',
        'content',
        'text_content',
        'created_at',
    )
    list_display_links = (
        'id',
        'sender',
        'receiver',
    )
    list_filter = (
        'sender',
        'receiver',
        'content_type',
        'created_at',
    )
    search_fields = (
        'text_content',
    )
