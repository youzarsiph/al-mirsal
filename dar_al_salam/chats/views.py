""" API endpoints fro dar_al_salam.chats """

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from dar_al_salam.chats.models import Chat
from dar_al_salam.chats.serializers import ChatSerializer
from dar_al_salam.permissions import IsChatOwner


# Create your views here.
class ChatViewSet(ModelViewSet):
    """Create, read, update and delete chats"""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, IsChatOwner]
    ordering_fields = ["created_at", "updated_at"]
    search_fields = ["to_user", "from_user"]

    def perform_create(self, serializer):
        """Add the owner of the chat"""

        serializer.save(from_user=self.request.user)

    def get_queryset(self):
        """Filter the queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))
        )
