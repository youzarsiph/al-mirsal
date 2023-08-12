""" URLConf for chats app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.chats.views import ChatViewSet


router = DefaultRouter(trailing_slash=False)
router.register('', ChatViewSet, 'chat')


urlpatterns = [
    path('', include(router.urls)),
]
