from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import hello_world, student_info, StudentGetAPIView, StudentListAPIView, \
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentListCreateView, \
    StudentRetrieveUpdateDeleteView, ClassRoomViewSet, StudentViewSet

router = DefaultRouter()

router.register('classroom', ClassRoomViewSet)
router.register('student', StudentViewSet)

urlpatterns = [
    path("hello-world/", hello_world),
    path("student-info/", student_info),
    path("student-apiview/", StudentListAPIView.as_view()),
    path("student-apiview/<int:id>/", StudentGetAPIView.as_view()),
    path("login/", obtain_auth_token)
]


generic_urls = [
    path("generic-student-list/", StudentListView.as_view()),
    path("generic-student-create/", StudentCreateView.as_view()),
    path("generic-student-update/<int:pk>/", StudentUpdateView.as_view()),
    path("generic-student-delete/<int:pk>/", StudentDeleteView.as_view()),
    path("generic-student-list-create/", StudentListCreateView.as_view()),
    path("generic-student-retrieve-update-delete/<int:pk>/", StudentRetrieveUpdateDeleteView.as_view()),
]

urlpatterns += generic_urls + router.urls
