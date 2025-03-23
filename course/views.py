from django.shortcuts import render, redirect
from trainee.models import *
from django.http import HttpResponseRedirect
from rest_framework import generics
from trainee.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

@api_view(['GET'])
def track_update(request):
    return Response({"message": "Tracking updates!"})

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


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
