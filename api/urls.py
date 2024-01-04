from django.urls import path
from .views import hello_world, student_info


urlpatterns = [
    path("hello-world/", hello_world),
    path("student-info/", student_info)
]
