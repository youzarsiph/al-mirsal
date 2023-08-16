""" API Views """


from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.mixins import OwnerMixin
from messenger.permissions import IsUser
from messenger.models import Member, Message
from messenger.serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    MemberSerializer,
    MessageSerializer,
)


# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """User ViewSet"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ["first_name", "last_name"]
    ordering_fields = ["first_name", "last_name"]

    def perform_create(self, serializer):
        """Encrypt the password"""

        serializer.save(password=make_password(serializer.validated_data["password"]))

    def get_serializer_class(self):
        """Return serializers based on self.action"""

        if self.action == "create":
            self.serializer_class = UserCreateSerializer

        elif self.action in ("update", "partial_update"):
            self.serializer_class = UserUpdateSerializer

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
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    ordering_fields = []


class MessageViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete messages"""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ['text', 'photo', 'file']
