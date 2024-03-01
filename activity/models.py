from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    # Generic relation
    limit = models.Q(app_label='post', model='story') | models.Q(app_label='post',
                    model='instapost') | models.Q(app_label='activity', model='comment')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.user.username} liked {self.post}'

    class Meta:
        unique_together = ['user', 'content_type', 'object_id']


class Comment(models.Model):
    post = models.ForeignKey("post.InstaPost", on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like, related_query_name='comment')

    def __str__(self):
        if len(self.content) > 100:
            return f'{self.content[:100]} ...'
        return self.content
