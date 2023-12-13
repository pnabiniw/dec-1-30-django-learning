from django.urls import path
from .views import hello_world, hello, world, home, portfolio


urlpatterns = [
    path("hello/", hello),
    path("world/", world),
    path("home/", home),
    path("portfolio/", portfolio),
    path("", hello_world)
]
