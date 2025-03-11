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
    path("add_trainee", views.add_trainee, name="add_trainee"),
    path("delete_trainee/<int:trainee_id>", views.delete_trainee, name="delete_trainee"),
    path("update_trainee/<int:trainee_id>", views.update_trainee, name="update_trainee")
]
