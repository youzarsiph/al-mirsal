""" URLConf for channels app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.channel.views import (
    ChannelViewSet,
    MemberViewSet,
    MessageViewSet,
    ChannelMembersViewSet,
    ChannelMessagesViewSet
)


router = DefaultRouter(trailing_slash=False)
router.register('', ChannelViewSet, 'channel')
router.register('members', MemberViewSet, 'member')
router.register('messages', MessageViewSet, 'message')


urlpatterns = [
    path('', include(router.urls)),

    # Channel Members
    path('<int:id>/members/', ChannelMembersViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:id>/members/<int:pk>/', ChannelMembersViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    # Channel Messages
    path('<int:id>/messages/', ChannelMessagesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:id>/messages/<int:pk>/', ChannelMessagesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
