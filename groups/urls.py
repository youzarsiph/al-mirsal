""" URLConf for groups app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.groups.views import GroupViewSet


router = DefaultRouter(trailing_slash=False)
router.register('', GroupViewSet, 'group')


urlpatterns = [
    path('', include(router.urls)),
]
