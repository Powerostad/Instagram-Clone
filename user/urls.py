from django.urls import path, include
from .views import FollowAPI, UpdateProfileAPI, ProfileViewAPI  # LoginUserAPI, LogoutUserAPI, CreateUserAPI

urlpatterns = [
    # path('create_user/', CreateUserAPI.as_view(), name='create_user'),
    # path('login/', LoginUserAPI.as_view(), name='login'),
    # path('logout/', LogoutUserAPI.as_view(), name='logout'),
    path('follow/', FollowAPI.as_view(), name='follow'),
    path('profile/<str:username>/update/', UpdateProfileAPI.as_view(), name='update_profile'),
    path('profile/<str:username>/', ProfileViewAPI.as_view(), name='profile_view'),
]
