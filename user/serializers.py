from rest_framework import serializers
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
    post_count = serializers.ReadOnlyField()
    posts = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    def get_posts(self, obj):
        return InstaPost.objects.filter(user__id=obj.id, is_active=True)
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
            'followers_count',
            'following',
            'following_count',
            'posts',
            'post_count',
            'website',
            'is_private',
            'is_deactivated',
        )



class FollowSerializer(serializers.Serializer):
    username = serializers.CharField()
