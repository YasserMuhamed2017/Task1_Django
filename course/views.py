from django.shortcuts import render

# Create your views here.
def course(request):
    lst_courses = ['JavaScript', 'ES6', 'React']
    return render(request, "course/courselist.html", {
        "courses": lst_courses
    })

def add_course(request):
    return render(request, "course/add_course.html")