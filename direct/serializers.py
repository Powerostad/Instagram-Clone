from rest_framework import serializers
from .models import DirectMessage


class DirectMessageSerializer(serializers.ModelSerializer):
    # sender = serializers.SlugRelatedField('username', read_only=True)
    # receiver = serializers.SlugRelatedField('username', read_only=True)

    class Meta:
        model = DirectMessage
        fields = '__all__'
