from django.contrib import admin
from .models import Profile, CustomUser
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'phone_number',
        'birthday',
        'gender',
        'account_type',
        'followers_count',
        'following_count',
        'post_count',
        'is_private',
        'is_deactivated',
    )
    list_editable = (
        'gender',
        'account_type',
        'is_private',
        'is_deactivated',
    )
    list_display_links = (
        'id',
        'user',
    )
    list_filter = (
        'birthday',
        'gender',
        'account_type',
        'is_private',
        'is_deactivated',
    )


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'full_name',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_display_links = (
        'id',
        'username',
        'email',
    )
    search_fields = (
        'username',
        'email',
    )
    list_editable = (
        'is_staff',
        'is_active',
    )
