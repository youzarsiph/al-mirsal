""" Serializers for groups app """

from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.groups.models import Group, Member, Message


# Create your serializers here.
class GroupSerializer(HyperlinkedModelSerializer):
    """ Group Serializer """

    class Meta:
        """ Meta Data """

        model = Group
        fields = ['id', 'url', 'user', 'name', 'description']


class MemberSerializer(HyperlinkedModelSerializer):
    """ Member Serializer """

    class Meta:
        """ Meta Data """

        model = Member
        fields = ['id', 'url', 'user', 'group', 'is_admin', 'banned']


class MessageSerializer(HyperlinkedModelSerializer):
    """ Message Serializer """

    class Meta:
        """ Meta Data """

        model = Message
        fields = ['id', 'url', 'user', 'group', 'text', 'photo', 'file']
