from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "trainee/layout.html")

# It's a list of three trainees.
lst = ['Yasser', 'Mohamed', 'Ahmed']

def trainee_list(request):
    return render(request, "trainee/trainee_list.html",
    {
        "trainees": lst
    })

def trainee_table(request):
    lst_courses = ['Django', 'Version Control', 'Python']
    two_combined_lists = zip(lst, lst_courses)
    return render(request, "trainee/trainee_table.html", {
        "trainee_course_lists": two_combined_lists
    })

def add_trainee(request):
    
    return render(request, "trainee/form.html")

def register(request):
    return render(request, "trainee/register.html")

def login(request):
    return render(request, "trainee/login.html")

def logout(request):
    return render(request, "trainee/logout.html")