from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from log.models import PostViewLog, StoryViewLog
from .serializers import CreatePostSerializer, FeedSerializer, PostSerializer, StorySerializer
from user.serializers import ProfileSerializer
from .models import InstaPost, Story


# Create your views here.


class CreatePostAPIView(CreateAPIView):
    serializer_class = CreatePostSerializer
    queryset = InstaPost.objects.all()
    permission_classes = (IsAuthenticated,)


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

