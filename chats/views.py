""" API endpoints fro messenger.chats """


from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.chats.models import Chat
from messenger.chats.permissions import IsChatParticipant
from messenger.chats.serializers import ChatSerializer


# Create your views here.
class ChatViewSet(ModelViewSet):
    """Create, read, update and delete chats"""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, IsChatParticipant]
    ordering_fields = ["created_at"]
    search_fields = [
        "to_user__username",
        "to_user__first_name",
        "to_user__last_name",
        "from_user__username",
        "from_user__first_name",
        "from_user__last_name",
    ]

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
