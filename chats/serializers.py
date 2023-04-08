""" Serializers for chats app """


from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.chats.models import Chat, Message


# Create your serializers here.
class ChatSerializer(HyperlinkedModelSerializer):
    """ Chat Serializer """

    class Meta:
        """ Meta Data """

        model = Chat
        fields = ['id', 'url', 'from_user', 'to_user', 'muted']


class MessageSerializer(HyperlinkedModelSerializer):
    """ Chat Message Serializer """

    class Meta:
        """ Meta Data """

        model = Message
        fields = ['id', 'url', 'user', 'chat', 'text', 'photo', 'file']
