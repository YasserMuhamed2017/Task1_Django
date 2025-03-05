from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('traineelist', views.trainee_list, name="traineelist"),
    path('traineetable', views.trainee_table, name="traineetable"),
    path("add_trainee", views.add_trainee, name="add_trainee"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("add_trainee", views.add_trainee, name="add_trainee")
]
