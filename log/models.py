from django.db import models
from django.contrib.auth import get_user_model

from post.models import InstaPost, Story
from user.models import Profile
# Create your models here.

User = get_user_model()


class PostViewLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='log_postview')
    post = models.ForeignKey(InstaPost, on_delete=models.CASCADE, related_name="log_post")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} seen post {self.post.id} from {self.post.user.username}"

    class Meta:
        ordering = ("-created_at",)


class StoryViewLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='log_storyview')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="log_story")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} seen story {self.story.id} from {self.story.user.username}"

    class Meta:
        ordering = ("-created_at",)


class ProfileViewLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='log_profileview')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="log_profile")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} seen profile {self.profile.user.username}"

    class Meta:
        ordering = ("-created_at",)
