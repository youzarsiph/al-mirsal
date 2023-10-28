""" API endpoints for messenger """


from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.permissions import IsUser
from messenger.serializers import UserSerializer


# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """Create, read, update and delete users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["first_name", "last_name"]

    def perform_create(self, serializer):
        """Encrypt the password"""

        serializer.save(password=make_password(serializer.validated_data["password"]))

    def get_permissions(self):
        """Customize the permissions based on self.action"""

        if self.action == "retrieve":
            self.permission_classes.remove(IsUser)

        return super().get_permissions()
