""" Views """


from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.views import MessageViewSet
from messenger.chats.models import Chat
from messenger.chats.mixins import ChatOwnerMixin
from messenger.chats.serializers import ChatSerializer


# Create your views here.
User = get_user_model()


class ChatViewSet(ChatOwnerMixin, ModelViewSet):
    """Chat ViewSet"""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = []
    ordering_fields = []


# Filtered ViewSets
class UserChatsViewSet(ChatViewSet):
    """Chats of a particular user"""

    def get_queryset(self):
        """Filter the queryset by user"""

        # Get the user instance
        user = User.objects.get(pk=self.kwargs["id"])

        # Return filtered queryset
        return super().get_queryset().filter(from_user=user)


class ChatMessagesViewSet(MessageViewSet):
    """Messages of a chat"""

    
    def perform_create(self, serializer):
        """Creates a message in a chat"""

        # Chat
        chat = Chat.objects.get(pk=self.kwargs["id"])

        # Create the message in chat
        serializer.save(user=self.request.user, chat=chat)

    def get_queryset(self):
        """Filter the queryset by chat"""

        # Chat
        chat = Chat.objects.get(pk=self.kwargs["id"])

        # Return filtered queryset
        return super().get_queryset().filter(chat=chat)
