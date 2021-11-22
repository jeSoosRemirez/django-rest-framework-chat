from rest_framework import serializers
from chat_app.models import Message
from utils import email_validator, text_validator


class MessageListSerializer(serializers.HyperlinkedModelSerializer):
    """
    Shows when we see a list of messages
    """
    class Meta:
        model = Message
        fields = ['author', 'author_email', 'text', 'created_time']

    def validate(self, attrs):
        # Check is email valid
        if not email_validator(attrs.get('author_email')):
            raise serializers.ValidationError('Invalid email.')
        # Check is text >= 100 chars
        elif not text_validator(attrs.get('text')):
            raise serializers.ValidationError('Message should be less than 100 chars.')
        return attrs


class MessageDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    Shows when we look at exact message
    """
    class Meta:
        model = Message
        fields = ['id', 'author', 'author_email', 'text', 'created_time']
