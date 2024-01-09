from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
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

    # def post(self, *args, **kwargs):
    #     print(self.request.data)
    #     name = self.request.data.get("name")
    #     age = self.request.data.get("age")
    #     email = self.request.data.get("email")
    #     address = self.request.data.get("address")
    #     Student.objects.create(name=name, age=age, email=email, address=address)
    #     return Response({
    #         "message": "Student Created Successfully"
    #     })

    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data)  # deserialization
        if serializer.is_valid():
            name = serializer.validated_data['name']
            age = serializer.validated_data['age']
            email = serializer.validated_data['email']
            address = serializer.validated_data['address']
            Student.objects.create(name=name, age=age, email=email, address=address)
            return Response({
                "message": "Student Created Successfully"
            })
        return Response({
            "message": "Invalid Request Data"
        })


class StudentListView(ListAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class StudentCreateView(CreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class StudentUpdateView(UpdateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class StudentDeleteView(DestroyAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class StudentListCreateView(ListCreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class StudentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()
