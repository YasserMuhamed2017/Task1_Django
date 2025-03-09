from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request, "trainee/layout.html")


def trainee_list(request):
    if request.method == "POST":
        trainee_name = request.POST.get("trainee")
        Trainee(trainee=trainee_name).save()
    else:
        return render(request, "trainee/trainee_list.html",
        {
            "trainees": Trainee.objects.all()
        })

def trainee_table(request):
    lst_courses = ['Django', 'Version Control', 'Python']
    two_combined_lists = zip(lst, lst_courses)
    return render(request, "trainee/trainee_table.html", {
        "trainee_course_lists": two_combined_lists
    })

def delete_trainee(request, trainee_id):
    if request.method == 'POST':
        Trainee.objects.get(id=trainee_id).delete()
        return redirect("traineelist")

def add_trainee(request):
    return render(request, "trainee/form.html")

def register(request):
    return render(request, "trainee/register.html")

def login(request):
    return render(request, "trainee/login.html")

def logout(request):
    return render(request, "trainee/logout.html")