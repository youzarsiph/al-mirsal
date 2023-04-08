""" URLConf for chats app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.chats.views import (
    ChatViewSet,
    MessageViewSet,
    ChatMessagesViewSet
)


router = DefaultRouter(trailing_slash=False)
router.register('', ChatViewSet, 'chat')
router.register('messages', MessageViewSet, 'message')


urlpatterns = [
    path('', include(router.urls)),

    # Chat Messages
    path('<int:id>/messages/', ChatMessagesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:id>/messages/<int:pk>/', ChatMessagesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
