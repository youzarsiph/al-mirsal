""" Mixins """


import secrets
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from messenger.permissions import IsOwnerOrReadOnly


# Create your mixins here.
class OwnerMixin:
    """Add the user field to a model automatically when creating"""

    def perform_create(self, serializer):
        """Save the model with request.user"""

        serializer.save(user=self.request.user)

    def get_permissions(self):
        """Customize the permissions based on self.action"""

        if self.action in ("create", "list", "retrieve"):
            permission_classes = self.permission_classes

        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [permission() for permission in permission_classes]


class UserFilterMixin:
    """Filter the queryset by user"""

    def get_queryset(self):
        """Filter queryset by user or member"""

        return super().get_queryset().filter(user=self.request.user)


class MemberMixin:
    """For Groups and Channels"""

    def get_queryset(self):
        """Filter queryset by user or member"""

        return (
            super()
            .get_queryset()
            .filter(Q(user=self.request.user) | Q(members=self.request.user))
        )


class TokenMixin:
    """Add the token field to a model automatically when creating"""

    def perform_create(self, serializer):
        """Save the model with generated token"""

        serializer.save(user=self.request.user, token=secrets.token_urlsafe(7))
