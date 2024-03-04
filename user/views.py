from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated

from log.models import ProfileViewLog
from .models import Profile
from .serializers import ProfileSerializer, CreateUserSerializer, FollowSerializer
from django.contrib.auth import (get_user_model,
                                 authenticate,
                                 login,
                                 logout)
# Create your views here.

User = get_user_model()


# simple Permission for find people who are not authenticated
# class NotAuthenticated(BasePermission):
#
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return True
#
#
# class CreateUserAPI(CreateAPIView):
#     permission_classes = [NotAuthenticated]
#     serializer_class = CreateUserSerializer
#     queryset = User.objects.all()


# class LoginUserAPI(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if not user.is_active:
#                 return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
#                                 data={'error': 'This account is deactivated.'})
#             login(request, user)
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
#                         data={'error': 'Invalid credentials'})
#
#
# class LogoutUserAPI(APIView):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             logout(request.user)
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'User not found.'})

# Simple permission for user's profile
class OwnProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only allowed to the owner of the profile
        return obj.id == request.user.id


class ProfileViewAPI(RetrieveAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]

    def get_object(self):
        username = self.kwargs["username"]
        profile = Profile.objects.filter(user__username=username).first()
        ProfileViewLog.objects.create(user=self.request.user, profile=profile)
        return get_object_or_404(User, username=username)


class UpdateProfileAPI(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, OwnProfile]

    def get_object(self):
        username = self.kwargs["username"]
        return get_object_or_404(User, username=username)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class FollowAPI(APIView):
    def post(self, request):
        serializer = FollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        to_follow = get_object_or_404(User, username=serializer.data['username'])

        # Follow
        if to_follow not in user.profile.following.all():
            user.profile.following.add(to_follow)
            to_follow.profile.followers.add(user)
        # Unfollow
        else:
            user.profile.following.remove(to_follow)
            to_follow.profile.followers.remove(user)

        return Response({'success': 'Updated follow'}, status=status.HTTP_200_OK)

