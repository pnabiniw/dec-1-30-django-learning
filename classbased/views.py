from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from myapp.models import ClassRoom, Student
from django.urls import reverse_lazy
from .forms import ClassRoomModelForm


class HomeView(TemplateView):
    template_name = "classbased/home.html"


class ClassRoomView(CreateView):
    form_class = ClassRoomModelForm
    template_name = "classbased/classroom.html"
    queryset = ClassRoom.objects.all()
    success_url = reverse_lazy('classbased_classroom')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()  # {"form": , "view": }
        print(context)
        context["classrooms"] = ClassRoom.objects.all()
        return context


class StudentView(ListView):
    template_name = "classbased/student.html"
    queryset = Student.objects.all()
    context_object_name = "students"


def delete_classroom(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        classroom.delete()
        return redirect("classbased_classroom")
    return render(request, template_name="classbased/delete_classroom.html",
                  context={"classroom": classroom})
