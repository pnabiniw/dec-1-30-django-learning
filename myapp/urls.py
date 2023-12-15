from django.urls import path
from .views import hello_world, hello, world, home, portfolio, temp_inherit_home, \
    temp_inherit_features, temp_inherit_pricing


urlpatterns = [
    path("hello/", hello),
    path("world/", world),
    # path("home/", home),
    path("portfolio/", portfolio, name='portfolio_page'),
    path("temp-inherit/", temp_inherit_home, name='temp_inherit_home'),
    path("features/", temp_inherit_features, name='temp_inherit_features'),
    path("pricing/", temp_inherit_pricing, name='temp_inherit_pricing'),
    path("", home, name="home_page")
]
