""" Channel Message Consumer """

from al_mirsal.channel.models import Channel
from al_mirsal.channel.serializers import ChannelSerializer
from al_mirsal.consumers import MessageConsumer


# Create your consumers here.
class ChannelMessageConsumer(MessageConsumer):
    """Channel Message consumer"""

    model = Channel
    serializer_class = ChannelSerializer
    model_with_members = True
