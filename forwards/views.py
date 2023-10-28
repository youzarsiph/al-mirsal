""" API endpoints for messenger.forwards """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.permissions import IsOwner
from messenger.msgs.models import Message
from messenger.forwards.models import Forward
from messenger.forwards.serializers import ForwardSerializer


# Create your views here.
class ForwardViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete message forwards"""

    queryset = Forward.objects.all()
    serializer_class = ForwardSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class MessageForwardsViewSet(ForwardViewSet):
    """User Reactions"""

    def perform_create(self, serializer):
        """Forward a message"""

        message = Message.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, message=message)

    def get_queryset(self):
        """Filter queryset by message"""

        message = Message.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(message=message)


class UserForwardsViewSet(ForwardViewSet):
    """User Reactions"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
