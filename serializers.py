""" Serializers for messenger """


from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


# Create your serializers here.
User = get_user_model()


class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta Data"""

        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "phone",
            "photo",
            "online",
            "typing",
        ]
