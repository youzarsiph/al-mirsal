""" API endpoints for dar_al_salam.msgs """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from dar_al_salam.messages.models import Message
from dar_al_salam.messages.serializers import MessageSerializer
from dar_al_salam.mixins import OwnerMixin


# Create your views here.
class MessageViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete messages"""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "channel", "chat", "group", "is_pinned"]
