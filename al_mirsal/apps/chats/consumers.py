"""Chat Message Consumer"""

from typing import Dict, Optional

from al_mirsal.apps.chats.models import Chat
from al_mirsal.apps.chats.serializers import ChatSerializer
from al_mirsal.apps.message.consumers import MessageConsumer


# Create your consumers here.
class ChatMessageConsumer(MessageConsumer):
    """Chat Message consumer"""

    model = Chat
    serializer_class = ChatSerializer

    async def check_authorization(self) -> bool:
        """Check if the user is the sender or receiver of the messages"""

        return self.user.pk in [self.object.from_user_id, self.object.to_user_id]

    async def receive_json(self, content: Optional[Dict[str, str]], **kwargs) -> None:
        """Creates the received message then sends it back"""

        if content is None:
            return

        message = await self.create_user_message(content)
        await self.channel_layer.group_send(
            self.channel_id,
            {"type": "chat_message", "generating": True, "data": message},
        )

    # Receive message from room group
    async def chat_message(self, event: Dict[str, str]) -> None:
        """"""
        message = event["data"]

        # Send message to WebSocket
        await self.send_json(
            {"generating": True, "data": message},
        )
