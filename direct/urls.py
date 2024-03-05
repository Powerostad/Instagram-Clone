from django.urls import path
from .views import CreateMessage, RetrieveMessage

urlpatterns = [
    path('send_message/', CreateMessage.as_view(), name='send-direct'),
    path('get_message/<int:pk>/', RetrieveMessage.as_view(), name='get-direct'),
]
