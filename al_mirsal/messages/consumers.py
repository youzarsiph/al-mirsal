""" Message Consumer """

import json
from typing import Any, Dict, List, Literal, Union
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db.models import Model, QuerySet
from rest_framework.serializers import ModelSerializer

from al_mirsal.chats.models import Chat
from al_mirsal.chats.serializers import ChatSerializer
from al_mirsal.messages.models import Message
from al_mirsal.messages.serializers import MessageSerializer


# Create your consumers here.
class MessageConsumer(AsyncJsonWebsocketConsumer):
    """Message consumer"""

    model = Chat
    serializer_class = ChatSerializer

    async def connect(self):
        """Connect to the chat"""

        # User
        self.user = self.scope["user"]

        # Check if user is authenticated
        if not self.user.is_authenticated:
            await self.close()

        # Get chat instance
        self.chat = await self.get_object(
            id=self.scope["url_route"]["kwargs"]["chat_id"]
        )

        if not self.chat:
            await self.close()

        # Check if the user is the owner of the chat
        if self.user.id not in (self.chat.from_user_id, self.chat.to_user_id):
            await self.close()

        await self.accept()

        self.groups = [f"chat_{self.chat.id}"]

    async def decode_json(self, text_data) -> Dict[str, Any]:
        """
        Decode and validate the incoming JSON data using a serializer

        Returns:
            dict: The decoded JSON data
        """

        data = json.loads(text_data)

        # Data validation
        serializer = MessageSerializer(data=data["content"])

        if not serializer.is_valid():
            raise ValueError(serializer.errors)

        return {"type": data["type"], "content": serializer.validated_data}

    async def receive_json(
        self,
        content: Dict[Literal["type", "content"], Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Process incoming data

        Args:
            content (Dict[str, Any]): Validated data

        Raises:
            ValueError: _description_

        Returns:
            None
        """

        event = content["type"]

        match event:
            case "model":
                print(content)

            case _:
                raise ValueError("Invalid event type")

    @database_sync_to_async
    def get_object(self, id: int) -> Union[Model, None]:
        """
        Get the model instance if it exists or None

        Args:
            id (int): The model id

        Returns:
            Chat: The model instance
            None: If the model does not exist
        """

        try:
            return self.model.objects.get(id=id)

        except self.model.DoesNotExist:
            return None

    @database_sync_to_async
    def get_model_messages(self) -> QuerySet[Message]:
        """
        Get chat messages

        Returns:
            QuerySet[Message]: The chat messages
        """

        return self.chat.messages.all()

    def get_serializer(
        self,
        *args: List[Any],
        **kwargs: Dict[str, Any],
    ) -> ModelSerializer:
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.

        Returns:
            Serializer: Serializer instance
        """

        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())

        return serializer_class(*args, **kwargs)

    def get_serializer_class(self) -> ModelSerializer:
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        """

        if not self.serializer_class:
            raise ValueError("Serializer class not provided")

        return self.serializer_class

    def get_serializer_context(self) -> Dict[str, Any]:
        """
        Extra context provided to the serializer class.

        Returns:
            dict: The serializer context
        """

        return {"request": self.scope, "view": self}
