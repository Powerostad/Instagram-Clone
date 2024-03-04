from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import InstaPost
from .models import Like, Comment
from .serializers import LikeSerializer, CommentSerializer


class LikePostAPIView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(InstaPost, id=post_id)
        user = request.user
        # Like.objects.filter(user=user, content_type__model='instapost', object_id=post_id).delete()
        like_exist = Like.objects.filter(post__user__id=user.id).exists()
        # Check if the user has already liked the post
        if like_exist:
            Like.objects.filter(post__user__id=user.id).delete()
            return Response({'message': 'You unliked this post.'}, status=status.HTTP_200_OK)

        # Create a new like
        like = Like.objects.create(user=user, content_object=post)

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,]
