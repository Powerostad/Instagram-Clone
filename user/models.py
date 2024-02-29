from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


def user_directory_path(instance, filename):
    return f'ProfilePic_{instance.user.id}/{filename}'


class CustomUser(AbstractUser):
    full_name = models.CharField('Full Name', max_length=30)
    email = models.EmailField('Email', max_length=50, unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    ph_number = models.IntegerField('Phone Number', blank=True, null=True, unique=True, validators=[
        RegexValidator(
            regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}',
            message='Enter a valid registration number in the format 09xxxxxxxxx.',
            code="invalid_registration",
        )
    ])
    bio = models.TextField('Bio', blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    profile_pic = models.ImageField('Profile Picture',
                                    upload_to=user_directory_path,
                                    default='user/user.png')
    gender = models.CharField('Gender',
                              max_length=6,
                              blank=True,
                              choices=[('Male', 'Male'), ('Female', 'Female')])
    account_type = models.CharField('Account Type',
                                    max_length=8,
                                    blank=True,
                                    default='PERSONAL',
                                    choices=[('BUSINESS', 'Business'), ('PERSONAL', 'Personal')])
    followers = models.ManyToManyField(CustomUser,
                                       related_name='Follower',
                                       blank=True,
                                       symmetrical=False)
    following = models.ManyToManyField(CustomUser,
                                       related_name='Following',
                                       blank=True,
                                       symmetrical=False)
    website = models.URLField('Website', max_length=75, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    is_deactivated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} profile'

    def followers_count(self):
        """ No of followers """
        if self.followers.count():
            return self.followers.count()
        return 0

    def following_count(self):
        """ No of following """
        if self.following.count():
            return self.following.count()
        return 0

    def post_count(self):
        """ No of posts """
        if self.user_post.count():
            return self.user_post.count()
        return 0

    def posts(self):
        """ Get all the posts """
        from post.models import InstaPost
        return InstaPost.objects.filter(user__id=self.pk)
