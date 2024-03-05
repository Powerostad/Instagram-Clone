from django.db.models.signals import post_save
from django.dispatch import receiver
from post.models import Mention
from .models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=Comment)
def create_mention(sender, instance, created, **kwargs):
    if created:
        content = instance.content
        mentions = []
        for word in content.split():
            if word.startswith('@'):
                mentions.append(word[1:])

        for mention in mentions:
            try:
                mentioned_user = User.objects.get(username=mention)
                Mention.objects.create(
                    user=instance.user,
                    mentioned_user=mentioned_user,
                    post=instance.post,
                    comment=instance
                )
            except User.DoesNotExist:
                pass
