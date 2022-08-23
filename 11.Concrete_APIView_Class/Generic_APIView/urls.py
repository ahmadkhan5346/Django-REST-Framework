from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/', views.StudentList.as_view()),
    # path('student/', views.StudentCreate.as_view()),
    # path('student/<int:pk>', views.StudentRetrieve.as_view()),
    # path('student/<int:pk>', views.StudentUpdate.as_view()),
    # path('student/<int:pk>', views.StudentDestroy.as_view()),

    # path('student/', views.LC_Student.as_view()),
    # path('student/<int:pk>', views.RU_Student.as_view()),
    # path('student/<int:pk>', views.RD_Student.as_view()),
    # path('student/<int:pk>', views.RUD_Student.as_view()),


    path('api/user/', include('crud.urls')),
]
