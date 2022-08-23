from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.LCStudentAPI.as_view()),
    path('student/<int:pk>', views.RUDStudenAPI.as_view()),
]
