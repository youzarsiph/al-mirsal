""" Serializers for messenger.reactions """


from rest_framework.serializers import ModelSerializer
from messenger.reactions.models import Reaction


# Create your serializers here.
class ReactionSerializer(ModelSerializer):
    """Reaction Serializer"""

    class Meta:
        """Meta data"""

        model = Reaction
        read_only_fields = ["user"]
        fields = ["id", "url", "user", "value", "created_at", "updated_at"]
