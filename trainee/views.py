from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.views.generic import ListView, FormView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import TraineeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    return render(request, "trainee/layout.html")


class TraineeListView(ListView, FormView):
    model = Trainee
    template_name = "trainee/trainee_list.html"
    context_object_name = "trainees"
    form_class = TraineeForm
    success_url = reverse_lazy("traineelist")  # Redirect after successful submission

    def form_valid(self, form):
        form.save()  # Save new trainee
        return super().form_valid(form)

def trainee_table(request):
    lst_trainees = Trainee.objects.all()
    lst_courses = Course.objects.all()
    two_combined_lists = zip(lst_trainees, lst_courses)
    return render(request, "trainee/trainee_table.html", {
        "trainee_course_lists": two_combined_lists
    })

class TraineeDeleteView(DeleteView):
    model = Trainee
    success_url = reverse_lazy("traineelist") 

class TraineeDetailView(DetailView):
    model = Trainee
    template_name = 'trainee/trainee_detail.html'
    context_object_name = 'trainee'


def add_trainee(request):
    return render(request, "trainee/form.html")

class TraineeUpdateView(UpdateView):
    model = Trainee
    template_name = "trainee/update_trainee.html"
    fields = ["trainee"]  # Fields to be updated
    context_object_name = "trainee"
    success_url = reverse_lazy("traineelist") 

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password1)
        user.save()

        login(request, user)
        return redirect("traineetable") # Redirect after registration

    return render(request, "trainee/register.html")
    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("traineetable")  # Redirect after login
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "trainee/login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")  # Redirect to login page after logout
