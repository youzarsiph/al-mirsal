"""Group Message Consumer"""

from al_mirsal.apps.groups.models import Group
from al_mirsal.apps.groups.serializers import GroupSerializer
from al_mirsal.apps.message.consumers import MessageConsumer


# Create your consumers here.
class GroupMessageConsumer(MessageConsumer):
    """Group Message consumer"""

    model = Group
    serializer_class = GroupSerializer
