""" Custom Routers """


from rest_framework.routers import DefaultRouter


# Create your routers here.
class Router(DefaultRouter):
    """ Custom Router """

    trailing_slash = False
    include_root_view = False
