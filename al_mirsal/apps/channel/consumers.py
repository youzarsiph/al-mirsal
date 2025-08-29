"""Channel Message Consumer"""

from al_mirsal.apps.channel.models import Channel
from al_mirsal.apps.channel.serializers import ChannelSerializer
from al_mirsal.apps.message.consumers import MessageConsumer


# Create your consumers here.
class ChannelMessageConsumer(MessageConsumer):
    """Channel Message consumer"""

    model = Channel
    serializer_class = ChannelSerializer
