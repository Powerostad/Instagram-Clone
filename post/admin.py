from django.contrib import admin
from .models import InstaPost, Media, Mention, Story, Tag
# Register your models here.
admin.site.register(InstaPost)
admin.site.register(Media)
admin.site.register(Mention)
admin.site.register(Story)
admin.site.register(Tag)