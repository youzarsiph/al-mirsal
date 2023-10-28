""" Serializers for messenger.forwards """


from rest_framework.serializers import ModelSerializer
from messenger.forwards.models import Forward


# Create your serializers here.
class ForwardSerializer(ModelSerializer):
    """Forward Serializer"""

    class Meta:
        """Meta data"""

        model = Forward
        fields = ["id", "value", "created_at", "updated_at"]
