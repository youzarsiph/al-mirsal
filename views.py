""" API endpoints for messenger app """


from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger import serializers
from messenger.permissions import IsUser
from messenger.models import Member, Message, Reaction
from messenger.mixins import OwnerMixin, UserFilterMixin


# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """Create, read, update and delete users"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = []
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["first_name", "last_name"]

    def perform_create(self, serializer):
        """Encrypt the password"""

        serializer.save(password=make_password(serializer.validated_data["password"]))

    def get_serializer_class(self):
        """Return serializers based on self.action"""

        if self.action == "create":
            self.serializer_class = serializers.UserCreateSerializer

        elif self.action in ("update", "partial_update"):
            self.serializer_class = serializers.UserUpdateSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        """Customize the permissions based on self.action"""

        if self.action == "list":
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        elif self.action != "create":
            self.permission_classes = [IsAuthenticated, IsUser]

        return super().get_permissions()


class MemberViewSet(OwnerMixin, ModelViewSet):
    """Members in groups and channels"""

    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ["user__username", "user__first_name", "user__last_name"]


class UserFilteredMemberViewSet(UserFilterMixin, MemberViewSet):
    """Member ViewSet with queryset filtered by user"""

    pass


class MessageViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete messages"""

    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ["text", "photo", "file"]
    ordering_fields = ["created_at"]
    filterset_fields = ["pinned", "starred"]


class UserFilteredMessageViewSet(UserFilterMixin, MessageViewSet):
    """Message ViewSet with queryset filtered by user"""

    pass


class ReactionViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete messages"""

    queryset = Reaction.objects.all()
    serializer_class = serializers.ReactionSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class UserFilteredReactionViewSet(UserFilterMixin, ReactionViewSet):
    """Reaction ViewSet with queryset filtered by user"""

    pass


class MessageReactionsViewSet(ReactionViewSet):
    """Reactions of a message"""

    def perform_create(self, serializer):
        """Creates a reaction"""

        # Message
        message = Message.objects.get(pk=self.kwargs["id"])

        # Create the reaction
        serializer.save(user=self.request.user, message=message)

    def get_queryset(self):
        """Filter the queryset by message"""

        # Message
        message = Message.objects.get(pk=self.kwargs["id"])

        # Return filtered queryset
        return super().get_queryset().filter(message=message)
