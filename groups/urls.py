""" URLConf for groups app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.groups.views import (
    GroupViewSet,
    MemberViewSet,
    MessageViewSet,
    GroupMembersViewSet,
    GroupMessagesViewSet
)


router = DefaultRouter(trailing_slash=False)
router.register('', GroupViewSet, 'group')
router.register('members', MemberViewSet, 'member')
router.register('messages', MessageViewSet, 'message')


urlpatterns = [
    path('', include(router.urls)),

    # Channel Members
    path('<int:id>/members/', GroupMembersViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:id>/members/<int:pk>/', GroupMembersViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    # Group Messages
    path('<int:id>/messages/', GroupMessagesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:id>/messages/<int:pk>/', GroupMessagesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
