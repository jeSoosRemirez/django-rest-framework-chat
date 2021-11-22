from rest_framework import serializers
from chat_app.models import Message


class MessageListSerializer(serializers.HyperlinkedModelSerializer):
    """
    Shows when we see a list of messages
    """
    class Meta:
        model = Message
        fields = ['author', 'author_email', 'text', 'created_time']


class MessageDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    Shows when we look at exact message
    """
    class Meta:
        model = Message
        fields = ['id', 'author', 'author_email', 'text', 'created_time']
