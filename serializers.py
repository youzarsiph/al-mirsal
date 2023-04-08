""" Serializers """


from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer


# Create your serializers here
User = get_user_model()


class UserSerializer(HyperlinkedModelSerializer):
    """ User Serializer """

    class Meta:
        """ Meta Data """

        model = User
        fields = [
            'id', 'url', 'username', 'first_name', 'last_name', 'phone',
            'photo', 'online', 'typing', 'chats', 'chat_groups', 'channels'
        ]


class UserCreateSerializer(UserSerializer):
    """ Serializer for creating users """

    class Meta(UserSerializer.Meta):
        """ Meta Data """

        fields = [
            'username', 'password', 'first_name', 'last_name', 'phone', 'photo'
        ]


class UserUpdateSerializer(UserSerializer):
    """ Serializer for creating users """

    class Meta(UserSerializer.Meta):
        """ Meta Data """

        fields = [
            'username', 'first_name', 'last_name', 'phone', 'photo'
        ]
