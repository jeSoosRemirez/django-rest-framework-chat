from rest_framework import serializers
from chat_app.models import Message


class MessageListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = ['author', 'author_email', 'text', 'created_time']


class MessageDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'author', 'author_email', 'text', 'created_time']
