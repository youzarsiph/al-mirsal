"""Consumers for al_mirsal.messages"""

import json
from typing import Any, Dict, Optional, Union
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from al_mirsal.channel.models import Channel
from al_mirsal.channel.serializers import ChannelSerializer
from al_mirsal.chats.models import Chat
from al_mirsal.chats.serializers import ChatSerializer
from al_mirsal.groups.models import Group
from al_mirsal.groups.serializers import GroupSerializer
from al_mirsal.message.models import Message
from al_mirsal.message.serializers import MessageSerializer
from al_mirsal.users.models import User


# Create your consumers here.
class MessageConsumer(AsyncJsonWebsocketConsumer):
    """Base consumer for sending and receiving messages"""

    user: User
    model: Union[Channel, Chat, Group]
    serializer_class: Union[ChannelSerializer, ChatSerializer, GroupSerializer]

    async def connect(self) -> None:
        """Connect to chat"""

        # User
        self.user = self.scope["user"]

        # Check is the user is authenticated
        if not self.user.is_authenticated:
            await self.close(code=401, reason="Authentication")
            return

        # Chat
        self.object = await self.get_object()

        # Check is the user can access the chat
        if not await self.check_authorization():
            await self.close(code=403, reason="Authorization")
            return

        # Accept connection
        await self.accept()

    async def check_authorization(self) -> bool:
        """
        Check if the user is authorized to access the chat

        Returns:
            bool: Weather to allow access or not
        """

        return self.user.pk not in [self.object.form_id, self.object.to_id]

    async def decode_json(self, text_data: str) -> Dict[str, str]:
        """
        Decode and validate the incoming JSON data using a serializer

        Args:
            text_data (str): Incoming data

        Returns:
            dict: The decoded JSON data
        """

        return await self.serialize_message(json.loads(text_data))

    async def receive_json(self, content: Optional[Dict[str, str]], **kwargs) -> None:
        """Receive messages"""

        raise NotImplementedError(f"receive_json is not implemented for {__name__}")

    async def create_user_message(self, content: Dict[str, str]) -> Dict[str, str]:
        """Create user message and add it to chat history"""

        message = await self.serialize_message(
            await self.create_message(
                chat_id=self.object.pk,
                content=content["content"],
            )
        )

        return message

    @database_sync_to_async
    def get_object(self) -> Optional[Union[Channel, Chat, Group]]:
        """
        Get the model instance if it exists or None

        Returns:
            Chat: The model instance
            None: If the model does not exist
        """

        try:
            return self.model.objects.get(pk=self.scope["url_route"]["kwargs"]["id"])

        except self.model.DoesNotExist:
            return None

    @database_sync_to_async
    def serialize_object(self) -> Dict[str, str]:
        """
        Serialize self.object using self.serializer_class

        Returns:
            Dict[str, str]: The serialized self.object
        """

        return self.serializer_class()(instance=self.object).data

    @database_sync_to_async
    def create_message(self, **kwargs) -> Message:
        """
        Create a new message

        Returns:
            Message: Created message
        """

        return self.object.messages.create(user_id=self.user.pk, **kwargs)

    @database_sync_to_async
    def serialize_message(
        self, data: Union[Message, Dict[str, Any]]
    ) -> Optional[Dict[str, str]]:
        """
        Serialize the message

        Returns:
            Dict[str, str]: The serialized message
            None: If data validation fails
        """

        if isinstance(data, dict):
            serializer = MessageSerializer(data=data["message"])

            # Data validation
            if serializer.is_valid(raise_exception=False):
                return serializer.validated_data

            return None

        elif isinstance(data, Message):
            return MessageSerializer(instance=data).data

        return None
