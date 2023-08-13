""" Serializers for groups app """

from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.groups.models import ChatGroup


# Create your serializers here.
class GroupSerializer(HyperlinkedModelSerializer):
    """Group Serializer"""

    class Meta:
        """Meta Data"""

        model = ChatGroup
        fields = ["id", "url", "name", "description"]
