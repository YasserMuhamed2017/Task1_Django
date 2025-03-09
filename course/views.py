from django.shortcuts import render, redirect
from trainee.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def course(request):
    if request.method == "POST":
        course = request.POST.get("course")
        Course(course=course).save()
        return redirect("course")
    else:
        lst_courses = Course.objects.all()
        return render(request, "course/courselist.html", {
            "courses": lst_courses
        })

def add_course(request):
    return render(request, "course/add_course.html")

def delete_course(request, course_id):
    if request.method == "POST":
        Course(id=course_id).delete()
        return redirect("course")
