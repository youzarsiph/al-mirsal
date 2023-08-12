""" URLConf for channels app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.channel.views import ChannelViewSet


router = DefaultRouter(trailing_slash=False)
router.register('', ChannelViewSet, 'channel')


urlpatterns = [
    path('', include(router.urls)),
]
