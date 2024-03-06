from django.contrib.auth import get_user_model
from django.core.files import File
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import InstaPost, Tag, Media, Story, Mention

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = ('name',)


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('media',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    user = serializers.SlugRelatedField('username', read_only=True)
    likes_count = serializers.SerializerMethodField()
    media = MediaSerializer(many=True, read_only=True)

    def get_likes_count(self, obj):
        if obj.likes.count():
            return obj.likes.count()
        return 0

    class Meta:
        model = InstaPost
        fields = (
            'caption',
            'user',
            'tags',
            'media_choice',
            'media',
            'created_at',
            'is_active',
            'likes_count',
        )


class CreatePostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField('name',many=True, queryset=Tag.objects.all())
    media = MediaSerializer(write_only=True, required=False)

    class Meta:
        model = InstaPost
        fields = (
            'caption',
            'tags',
            'media_choice',
            'media',
        )


class FeedSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField('username', read_only=True)
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = InstaPost
        fields = (
            'caption',
            'user',
            'tags',
            'media',
        )


class StorySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField('username', read_only=True)
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Story
        fields = (
            'user',
            'media',
            'context',
            'get_likes',
        )


