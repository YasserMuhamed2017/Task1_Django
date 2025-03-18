from . import views
from django.urls import path
from .views import TraineeListView, TraineeDeleteView, TraineeDetailView, TraineeUpdateView

urlpatterns = [
    path('', views.home, name="home"),
    path("traineelist/", TraineeListView.as_view(), name="traineelist"),
    path("trainee/<int:pk>/delete/", TraineeDeleteView.as_view(), name="delete_trainee"),
    path('trainees/<int:pk>/', TraineeDetailView.as_view(), name='trainee-detail'),
    path("update_trainee/<int:pk>/", TraineeUpdateView.as_view(), name="update_trainee"),
    path('traineetable', views.trainee_table, name="traineetable"),
    path("add_trainee", views.add_trainee, name="add_trainee"),
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path("add_trainee", views.add_trainee, name="add_trainee")
]
