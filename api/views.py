from django.http import JsonResponse
from myapp.models import Student


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


"""
[
    {"name": Jon, email: jcbds@df.com, age: 30},
    {"name": Jon, email: jcbds@df.com, age: 30},
    {"name": Jon, email: jcbds@df.com, age: 30},
    {"name": Jon, email: jcbds@df.com, age: 30},
]

"""
