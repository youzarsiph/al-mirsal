""" API endpoints for al_mirsal.msgs """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_mirsal.messages.models import Message
from al_mirsal.messages.serializers import MessageSerializer
from al_mirsal.mixins import OwnerMixin


# Create your views here.
class MessageViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete messages"""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "channel", "chat", "group", "is_pinned"]
