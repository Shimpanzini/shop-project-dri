from django.urls import path
from .views import SchoolApiView, StudentApiVIew

urlpatterns = [
    path('school/', SchoolApiView.as_view()),
    path('school/<int:pk>/', SchoolApiView.as_view()),
    path('student/', StudentApiVIew.as_view()),
]
