""" Serializers for channels app """


from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.channel.models import Channel, Member, Message


# Create your serializers here.
class ChannelSerializer(HyperlinkedModelSerializer):
    """ Channel Serializer """

    class Meta:
        """ Meta Data """

        model = Channel
        fields = ['id', 'url', 'user', 'name', 'description']


class MemberSerializer(HyperlinkedModelSerializer):
    """ Member Serializer """

    class Meta:
        """ Meta Data """

        model = Member
        fields = ['id', 'url', 'user', 'channel', 'is_admin', 'banned']


class MessageSerializer(HyperlinkedModelSerializer):
    """ Message Serializer """

    class Meta:
        """ Meta Data """

        model = Message
        fields = ['id', 'url', 'user', 'channel', 'text', 'photo', 'file']
