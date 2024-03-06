from rest_framework import serializers
from post.serializers import PostSerializer, StorySerializer
from .models import Profile
from django.contrib.auth import get_user_model
from post.models import InstaPost


User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'full_name',
            'email',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
            'email',
            'password'
        )


class MiniUserSerializer(serializers.ModelSerializer):
    ''' Mini version of User Serializer '''
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'full_name']


class ProfileSerializer(serializers.ModelSerializer):
    followers = MiniUserSerializer(many=True, source='profile.followers', read_only=True)
    following = MiniUserSerializer(many=True, source='profile.following', read_only=True)
    post_count = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()
    followers_count1 = serializers.SerializerMethodField()
    following_count1 = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    stories = StorySerializer(many=True, read_only=True)

    def get_posts(self, obj):
        posts = InstaPost.objects.filter(user__id=obj.id, is_active=True)
        return PostSerializer(posts, many=True).data

    def get_post_count(self, obj):
        if obj.user_post.count():
            return obj.user_post.count()
        return 0

    def get_followers_count1(self, obj):
        return obj.profile.followers.count()

    def get_following_count1(self, obj):
        return obj.profile.following.count()

    class Meta:
        model = Profile
        fields = (
            'user',
            'phone_number',
            'bio',
            'birthday',
            'profile_pic',
            'gender',
            'account_type',
            'followers',
            'followers_count1',
            'following',
            'following_count1',
            'posts',
            'post_count',
            'stories',
            'website',
        )



class FollowSerializer(serializers.Serializer):
    username = serializers.CharField()
