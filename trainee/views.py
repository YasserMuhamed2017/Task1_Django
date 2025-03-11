from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.
def home(request):
    return render(request, "trainee/layout.html")


def trainee_list(request):
    if request.method == "POST":
        trainee_name = request.POST.get("trainee")
        Trainee(trainee=trainee_name).save()
        return HttpResponseRedirect("traineelist")
    else:
        return render(request, "trainee/trainee_list.html",
        {
            "trainees": Trainee.objects.all()
        })

def trainee_table(request):
    lst_trainees = Trainee.objects.all()
    lst_courses = Course.objects.all()
    two_combined_lists = zip(lst_trainees, lst_courses)
    return render(request, "trainee/trainee_table.html", {
        "trainee_course_lists": two_combined_lists
    })

def delete_trainee(request, trainee_id):
    if request.method == 'POST':
        Trainee.objects.get(id=trainee_id).delete()
        return redirect("traineelist")

def add_trainee(request):
    return render(request, "trainee/form.html")

def update_trainee(request, trainee_id):
    if request.method == "POST":
        updated_trainee = request.POST["updated_trainee"]
        print(updated_trainee)
        trainee = Trainee.objects.get(id=trainee_id)
        trainee.trainee = updated_trainee
        trainee.save()
        return redirect("traineelist")
    return render(request, "trainee/update_trainee.html", {
        "trainee_id": trainee_id,
        "trainee_name": Trainee.objects.get(id=trainee_id).trainee
    })

def register(request):
    return render(request, "trainee/register.html")

def login(request):
    return render(request, "trainee/login.html")

def logout(request):
    return render(request, "trainee/logout.html")