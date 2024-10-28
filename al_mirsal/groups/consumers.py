""" Group Message Consumer """

from al_mirsal.consumers import MessageConsumer
from al_mirsal.groups.models import Group
from al_mirsal.groups.serializers import GroupSerializer


# Create your consumers here.
class GroupMessageConsumer(MessageConsumer):
    """Group Message consumer"""

    model = Group
    serializer_class = GroupSerializer
    model_with_members = True
