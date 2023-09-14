""" Mixins for chats app """


from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from messenger.chats.permissions import IsChatOwner


# Create your mixins here.
class ChatOwnerMixin:
    """Add the owner of the object"""

    def perform_create(self, serializer):
        """Save with owner"""

        serializer.save(from_user=self.request.user)

    def get_queryset(self):
        """Filter the queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))
        )

    def get_permissions(self):
        """Customize the permissions based on self.action"""

        if self.action in ("create", "list", "retrieve"):
            permission_classes = self.permission_classes

        else:
            permission_classes = [IsAuthenticated, IsChatOwner]

        return [permission() for permission in permission_classes]
