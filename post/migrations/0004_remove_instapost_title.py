# Generated by Django 4.2 on 2024-03-04 06:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0003_story_is_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instapost",
            name="title",
        ),
    ]
