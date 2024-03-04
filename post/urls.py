from django.urls import path
from .views import CreatePostAPIView, PostDetailView, StoryDetailView, Feed

urlpatterns = [
    path('create_post/', CreatePostAPIView.as_view(), name="create_post"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('story/<int:pk>/', StoryDetailView.as_view(), name="story_detail"),
    path('feed/', Feed.as_view(), name='feed'),
]
