"""API endpoints"""

from django.db.models import Q
from django.utils.text import slugify
from djoser.views import UserViewSet as BaseUVS
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from al_mirsal.api import serializers
from al_mirsal.api.mixins import OwnerMixin
from al_mirsal.apps.channel.models import Channel
from al_mirsal.apps.chats.models import Chat
from al_mirsal.apps.groups.models import Group
from al_mirsal.apps.members.models import Member
from al_mirsal.apps.message.models import Message


# Create your views here.
class UserViewSet(BaseUVS):
    """
    API endpoints for managing user accounts.

    ## Overview

    API endpoints are to manage user registration, authentication, and profile operations.
    Custom endpoints and extra actions have been added to support additional user-related features.

    ## Endpoints

    - **List Users**
    `GET /api/users`
    Retrieves a list of all user accounts.

    - **Create User (Registration)**
    `POST /api/users`
    Registers a new user. Requires user details such as username, email, and password.

    - **Retrieve User**
    `GET /api/users/{id}`
    Retrieves detailed information for the user account identified by `id`.

    - **Update User**
    `PUT /api/users/{id}`
    Fully updates the user account with the provided data.

    - **Partial Update User**
    `PATCH /api/users/{id}`
    Partially updates the user account fields.

    - **Delete User**
    `DELETE /api/users/{id}`
    Deletes the user account identified by `id`.

    ## Query Parameters

    - **search:**
    Filter users by username, first name, or last name (e.g., `?search=john`).

    - **ordering:**
    Order users by a specific field (e.g., `?ordering=-date_joined` for the most recent first).

    ## Permissions

    - **Authenticated Users:**
    Can view their own profile details.

    - **Admin/Staff Users:**
    Can list, retrieve, update, or delete any user account.

    *Note: Some endpoints (like registration) might be public while others require authentication.*

    ## Extra Actions

    This viewset extends functionality beyond the standard endpoints with additional custom actions:

    ## Example API Requests

    **List Users:**

    ```bash
    curl -X GET /api/users \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Register a New User:**

    ```bash
    curl -X POST /api/users \\
        -H "Content-Type: application/json" \\
        -d '{
                "username": "johndoe",
                "email": "john@example.com",
                "password": "securepassword"
            }'
    ```

    **Set User Password:**
    
    ```bash
    curl -X POST /api/users/1/set_password \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "old_password": "oldpassword",
                "new_password": "newsecurepassword"
            }'
    ```
    """

    lookup_field = "pk"
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["username", "date_joined", "last_login"]
    filterset_fields = ["username"]


class ChannelViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Channels"""

    queryset = Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "slug", "is_private"]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            slug=slugify(serializer.validated_data["slug"]),
        )

    def perform_update(self, serializer):
        serializer.save(slug=slugify(serializer.validated_data["slug"]))

    def get_serializer_class(self):
        if self.action == "join":
            self.serializer_class = Serializer

        return super().get_serializer_class()

    @action(methods=["post"], detail=True)
    def join(self, request: Request, pk: int) -> Response:
        """
        Join a channel
        """

        message: str
        channel: Channel = self.get_object()

        if request.user in channel.subscribers.all():
            channel.subscribers.remove(request.user)
            message = f"You left {channel}!"

        else:
            channel.subscribers.add(request.user)
            message = f"You joined {channel}!"

        return Response(status=status.HTTP_201_CREATED, data={"details": message})


class ChatViewSet(ModelViewSet):
    """Create, read, update and delete chats"""

    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at", "updated_at"]
    search_fields = ["to_user"]
    filterset_fields = ["to_user"]

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


class GroupViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete chat groups"""

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "slug", "is_private"]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            slug=slugify(serializer.validated_data["slug"]),
        )

    def perform_update(self, serializer):
        serializer.save(slug=slugify(serializer.validated_data["slug"]))

    def get_serializer_class(self):
        if self.action == "join":
            self.serializer_class = Serializer

        return super().get_serializer_class()

    @action(methods=["post"], detail=True)
    def join(self, request: Request, pk: int) -> Response:
        """
        Join a channel
        """

        message: str
        group: Group = self.get_object()

        if request.user in group.members.all():
            group.members.remove(request.user)
            message = f"You left {group}!"

        else:
            group.members.add(request.user)
            message = f"You joined {group}!"

        return Response(status=status.HTTP_201_CREATED, data={"details": message})


class MemberViewSet(OwnerMixin, ModelViewSet):
    """Members in groups and channels"""

    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "channel", "group", "status"]
    search_fields = []


class MessageViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete messages"""

    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content", "photo", "file"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "channel", "chat", "group", "is_pinned"]
