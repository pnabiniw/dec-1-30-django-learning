from django.urls import path
from .views import hello_world, hello, world, home, portfolio, temp_inherit_home


urlpatterns = [
    path("hello/", hello),
    path("world/", world),
    # path("home/", home),
    path("portfolio/", portfolio, name='portfolio_page'),
    path("temp-inherit/", temp_inherit_home, name='temp_inherit_home'),
    path("", home, name="home_page")
]
