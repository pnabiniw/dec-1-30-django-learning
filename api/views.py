from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Student

from .serializers import StudentSerializer, StudentModelSerializer


def hello_world(request):
    return JsonResponse({
        "message": "Hello World"
    })


def student_info(request):  # name, age, email, address
    students = Student.objects.all()
    response = []
    for student in students:
        response.append({
            "name": student.name,
            "age": student.age,
            "address": student.address
        })
    return JsonResponse(response, safe=False)


class StudentGetAPIView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs['id']
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({
                "detail": "Not Found"
            })
        # serializer = StudentSerializer(student)  # serialization
        serializer = StudentModelSerializer(student)  # serialization
        return Response(serializer.data)


class StudentListAPIView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        # serializer = StudentSerializer(students, many=True)  # serialization
        serializer = StudentModelSerializer(students, many=True)  # serialization
        return Response(serializer.data)
