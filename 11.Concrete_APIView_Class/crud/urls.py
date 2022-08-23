from django.urls import path, include
from crud.views import StudentListCreate, StudentRetrieveUpdateDestroy



urlpatterns = [
    path('crud/', StudentListCreate.as_view()),
    path('crud/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),
]
