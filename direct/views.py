from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DirectMessageSerializer
from .models import DirectMessage


class CreateMessage(CreateAPIView):
    serializer_class = DirectMessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = DirectMessage.objects.all()


class RetrieveMessage(RetrieveAPIView):
    serializer_class = DirectMessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = DirectMessage.objects.all()