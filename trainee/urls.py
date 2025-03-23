from . import views
from .views import TraineeListView, TraineeDeleteView, TraineeDetailView, TraineeUpdateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TraineeListCreateView, TraineeRetrieveUpdateDestroyView, track_update, TrackViewSet
from course.views import CourseListCreateView, CourseRetrieveUpdateDestroyView, TrackViewSet

router = DefaultRouter()
router.register(r'tracks', TrackViewSet)

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
    path("add_trainee", views.add_trainee, name="add_trainee"),
    path('trainees/', TraineeListCreateView.as_view(), name='list-trainees'), 
    path('trainee/<int:pk>/', TraineeRetrieveUpdateDestroyView.as_view(), name='update-trainee'), 
    path('track-update/', track_update, name='track-update'),  
    path('courses/', CourseListCreateView.as_view(), name='list-courses'),
    path('course/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='update-course'),
    path('', include(router.urls)),
]
