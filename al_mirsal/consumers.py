""" Message Consumer """

import json
from typing import Any, Dict, List, Literal, Union
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db.models import Model, QuerySet

from al_mirsal.channel.models import Channel
from al_mirsal.chats.models import Chat
from al_mirsal.chats.serializers import ChatSerializer
from al_mirsal.members.models import Member
from al_mirsal.messages.models import Message
from al_mirsal.messages.serializers import MessageSerializer


# Create your consumers here.
class MainConsumer(AsyncJsonWebsocketConsumer):
    """Main Consumer"""

    async def connect(self) -> None:
        """Connect to the chat"""

        # User
        self.user = self.scope["user"]

        # Check if user is authenticated
        if not self.user.is_authenticated:
            await self.close()

        await self.accept()

        self.groups = []


class MessageConsumer(AsyncJsonWebsocketConsumer):
    """Message consumer"""

    model = Chat
    serializer_class = ChatSerializer
    model_with_members = False

    async def connect(self) -> None:
        """Connect to the chat"""

        # User
        self.user = self.scope["user"]

        # Check if user is authenticated
        if not self.user.is_authenticated:
            await self.close()

        # Get model instance
        self.object = await self.get_object(id=self.scope["url_route"]["kwargs"]["id"])

        # Close if the object does not exist
        if not self.object:
            await self.close()

        # Check if the user is the owner of the object or a member of the object
        if self.model_with_members:
            # Channel/Group
            if (
                self.user.id != self.object.user_id
                or self.user.id not in await self.get_object_members(only_ids=True)
            ):
                await self.close()

        else:
            # Chat
            if self.user.id not in (self.object.from_user_id, self.object.to_user_id):
                await self.close()

        await self.accept()

        self.groups = [
            (
                "chat_"
                if not self.model_with_members
                else ("channel_" if isinstance(self.object, Channel) else "group_")
            )
            + self.object.pk
        ]

        await self.send_json(self.get_serializer(self.object))

    async def decode_json(self, text_data) -> Dict[str, Any]:
        """
        Decode and validate the incoming JSON data using a serializer

        Returns:
            dict: The decoded JSON data
        """

        data = json.loads(text_data)

        # Data validation
        serializer = MessageSerializer(data=data["content"])

        if not serializer.is_valid(raise_exception=True):
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
    def get_object_members(
        self,
        only_ids: bool = False,
    ) -> Union[QuerySet[Member], List[int]]:
        """
        Get object members

        Args:
            only_ids (bool, optional): If True, return a list of member ids. Defaults to False.

        Returns:
            QuerySet[Member]: The object members
            List[int]: The object member ids
        """

        if only_ids:
            return self.object.members.values_list("id", flat=True)

        return self.object.members.all()

    @database_sync_to_async
    def get_object_messages(self) -> QuerySet[Message]:
        """
        Get object messages

        Returns:
            QuerySet[Message]: The object messages
        """

        return self.object.messages.all()

    def get_serializer(self, *args, **kwargs: Dict[str, Any]):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.

        Returns:
            Serializer: Serializer instance
        """

        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())

        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
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
