""" API Views """


from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.permissions import IsUser
from messenger.serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer
)


# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """ User ViewSet """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']

    def perform_create(self, serializer):
        """ Encrypt the password """

        serializer.save(
            password=make_password(
                serializer.validated_data['password']
            )
        )

    def get_serializer_class(self):
        """ Return serializers based on self.action """

        if self.action == 'create':
            self.serializer_class = UserCreateSerializer

        elif self.action in ('update', 'partial_update'):
            self.serializer_class = UserUpdateSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        """ Customize the permissions based on self.action """

        if self.action in ('list', 'retrieve'):
            permission_classes = [IsAuthenticated]

        elif self.action == 'create':
            permission_classes = self.permission_classes

        else:
            permission_classes = [IsAuthenticated, IsUser]

        return [permission() for permission in permission_classes]
