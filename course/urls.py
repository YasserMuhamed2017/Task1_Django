from . import views
from django.urls import path

urlpatterns = [
    path("", views.course, name="course"),
    path("add_course", views.add_course, name="add_course"),
    path("delete_course/<int:course_id>", views.delete_course, name="delete_course")
]