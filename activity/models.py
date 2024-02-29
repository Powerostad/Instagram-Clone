from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Like(models.Model):
    post = models.ForeignKey("post.InstaPost", on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.username} liked {self.post}'

    def clean(self):
        already_liked = Like.objects.filter(post=self.post, user=self.user).exists()
        if already_liked:
            raise ValidationError(f'{self.user} have already liked {self.post}')


class Comment(models.Model):
    post = models.ForeignKey("post.InstaPost", on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey("post.InstaPost", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.content) > 100:
            return f'{self.content[:100]} ...'
        return self.content
