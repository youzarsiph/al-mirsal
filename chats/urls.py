""" URLConf for messenger.chats """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.chats.views import ChatViewSet
from messenger.msgs.views import ChatMessagesViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("chats", ChatViewSet, "chat")

sub_router = DefaultRouter()
sub_router.register("messages", ChatMessagesViewSet, "message")

urlpatterns = [
    path("", include(router.urls)),
    # Chat messages
    path(
        "chats/<int:id>/",
        include((sub_router.urls, "chats"), namespace="chats"),
    ),
]
