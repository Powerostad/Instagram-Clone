from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


def direct_message_directory_path(instance, filename):
    return f'direct_{instance.sender.id}/{instance.receiver.id}/{filename}'


class DirectMessage(models.Model):
    CONTENT_CHOICE = (('text', 'Text'),
                      ('audio', 'Audio'),
                      ('image', 'Image'),
                      ('video', 'Video'),)

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content_type = models.CharField(max_length=10, choices=CONTENT_CHOICE)
    content = models.FileField(upload_to=direct_message_directory_path, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)

    def clean(self):
        if self.content and self.text_content:
            raise ValidationError("Cannot send multiple types of content in a single message.")
        elif self.content_type != 'text' and self.text_content:
            raise ValidationError("You can't send text when selecting other types!")
        elif self.content_type == 'text' and self.content:
            raise ValidationError("You can't send non-text type content on text type!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
