from django.shortcuts import render, redirect
from myapp.models import ClassRoom, Student


def add_classroom(request):
    if request.method.lower() == "post":
        class_name = request.POST.get("classname")
        ClassRoom.objects.create(name=class_name)  # ORM
        return redirect("add_classroom")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="forms/classroom.html", context={"classrooms": classrooms})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom_id")
        Student.objects.create(name=name, age=age, email=email, address=address, classroom_id=classroom_id)
        return redirect("student")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="forms/add_student.html", context={"classrooms": classrooms})
