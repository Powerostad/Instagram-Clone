from django.urls import path
from .views import LikePostAPIView, CommentCreateAPIView, CommentDeleteAPIView

urlpatterns = [
    path('like/<int:post_id>/', LikePostAPIView.as_view(), name='like_post'),
    path('comment/create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('comment/delete/<int:pk>/', CommentDeleteAPIView.as_view(), name='comment_delete'),
]
