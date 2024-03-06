from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from log.models import PostViewLog, StoryViewLog
from .serializers import CreatePostSerializer, FeedSerializer, PostSerializer, StorySerializer, MediaSerializer
from user.serializers import ProfileSerializer
from .models import InstaPost, Story, Tag, Media


# Create your views here.


# class CreatePostAPIView(CreateAPIView):
#     serializer_class = CreatePostSerializer
#     queryset = InstaPost.objects.all()
#     permission_classes = (IsAuthenticated,)

class InstaPostCreateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        tags_data = request.data.pop('tags', [])
        media_data = request.data.pop('media', None)

        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            insta_post = serializer.save(user=self.request.user)
            print(tags_data)
            # Handle new tags
            for tag_string in tags_data:
                print(tag_string)
                # Extract individual tag names from the string
                tag_names = tag_string.strip('[]').split(',')
                print(tag_names)
                for tag_name in tag_names:
                    print(tag_name)
                    tag, _ = Tag.objects.get_or_create(name=str(tag_name))
                    insta_post.tags.add(tag)

            # Handle media
            if media_data:
                for media_file in media_data:
                    Media.objects.create(post=insta_post, media=media_file)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Feed(ListAPIView):
    serializer_class = FeedSerializer

    def get_queryset(self):
        user = self.request.user
        following = user.profile.following.all()
        queryset = InstaPost.objects.filter(
            Q(user__in=following) | Q(user=user)
        ).order_by('-created_at')
        return queryset


class PostDetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(InstaPost, pk=pk)
        PostViewLog.objects.create(user=request.user, post=post)
        return Response(PostSerializer(post).data)


class StoryDetailView(APIView):
    def get(self, request, pk):
        story = get_object_or_404(Story, pk=pk)
        StoryViewLog.objects.create(user=request.user, story=story)
        return Response(StorySerializer(story).data)

