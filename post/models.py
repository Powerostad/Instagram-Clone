import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.exceptions import ValidationError
# Create your models here.

User = get_user_model()


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField(unique=True, null=False, default=uuid.uuid1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Post(models.Model):
    MEDIA_CHOICES = (
        (1, '1 media'),
        (10, 'Up to 10 media')
    )
    title = models.CharField(max_length=100,)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    tags = models.ManyToManyField(Tag, related_name='tags')
    media_choice = models.IntegerField(choices=MEDIA_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.content) > 100:
            return f'{self.content[:100]} ...'
        return self.content


class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    media = models.FileField(upload_to=user_directory_path, verbose_name='Image or Video')

    def save(self, *args, **kwargs):
        # Check if the post has reached the maximum allowed media count
        if self.post.media.count() >= self.post.media_choice:
            raise ValueError("Maximum media count reached for this post.")
        super().save(*args, **kwargs)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.username} liked {self.post}'

    def clean(self):
        already_liked = Like.objects.filter(post=self.post, user=self.user).exists()
        if already_liked:
            raise ValidationError(f'{self.user} have already liked {self.post}')


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.FileField(upload_to=user_directory_path, verbose_name='Image or Video')
    context = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} story"

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Stories'
        verbose_name = 'Story'


class Mention(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentioned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} mentioned {self.mentioned_user}'
