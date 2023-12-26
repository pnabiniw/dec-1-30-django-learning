from django.urls import path
from .views import add_classroom


urlpatterns = [
    path("add-classroom/", add_classroom, name="add_classroom")
]
