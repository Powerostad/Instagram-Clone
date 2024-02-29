# Generated by Django 4.2 on 2024-02-29 06:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ph_number",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_registration",
                                message="Enter a valid registration number in the format 09xxxxxxxxx.",
                                regex="09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}",
                            )
                        ],
                        verbose_name="Phone Number",
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True, verbose_name="Bio")),
                (
                    "birthday",
                    models.DateField(blank=True, null=True, verbose_name="Birthday"),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        default="user/user.png",
                        upload_to=user.models.user_directory_path,
                        verbose_name="Profile Picture",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=6,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "account_type",
                    models.CharField(
                        blank=True,
                        choices=[("BUSINESS", "Business"), ("PERSONAL", "Personal")],
                        default="PERSONAL",
                        max_length=8,
                        verbose_name="Account Type",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True, max_length=75, null=True, verbose_name="Website"
                    ),
                ),
                ("is_private", models.BooleanField(default=False)),
                ("is_deactivated", models.BooleanField(default=False)),
                (
                    "followers",
                    models.ManyToManyField(
                        blank=True, related_name="Follower", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True,
                        related_name="Following",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
