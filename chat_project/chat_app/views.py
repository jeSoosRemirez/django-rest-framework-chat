from chat_app.models import Message
from chat_app.serializers import MessageListSerializer, MessageDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class MessageListView(ListCreateAPIView):
    """
    This APIView provides `list` action
    with 'author', 'author_email', 'text', 'created_time'.
    """
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer


class MessageDetailView(RetrieveUpdateDestroyAPIView):
    """
    This APIView provides `list` action
    with 'id', 'author', 'author_email', 'text', 'created_time'.
    """
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'messages': reverse('message-list', request=request, format=format)
    })
