""" API endpoints for messenger.reactions """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.msgs.models import Message
from messenger.permissions import IsOwner
from messenger.reactions.models import Reaction
from messenger.reactions.serializers import ReactionSerializer


# Create your views here.
class ReactionViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete message reactions"""

    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class MessageReactionsViewSet(ReactionViewSet):
    """User Reactions"""

    def perform_create(self, serializer):
        """Creates a reaction for a message"""

        message = Message.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, message=message)

    def get_queryset(self):
        """Filter queryset by message"""

        message = Message.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(message=message)


class UserReactionsViewSet(ReactionViewSet):
    """User Reactions"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
