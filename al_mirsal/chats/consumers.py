""" Chat Message Consumer """

from al_mirsal.chats.models import Chat
from al_mirsal.chats.serializers import ChatSerializer
from al_mirsal.consumers import MessageConsumer


# Create your consumers here.
class ChatMessageConsumer(MessageConsumer):
    """Chat Message consumer"""

    model = Chat
    serializer_class = ChatSerializer
    model_with_members = False
