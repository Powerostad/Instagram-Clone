from rest_framework import serializers
from .models import InstaPost, Tag, Media, Story, Mention


class TagSerializer(serializers.ModelSerializer):
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
    tags = TagSerializer(many=True, write_only=True)
    user = serializers.SlugRelatedField('username', read_only=True)
    media = MediaSerializer(many=True, write_only=True)

    class Meta:
        model = InstaPost
        fields = (
            'caption',
            'user',
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


