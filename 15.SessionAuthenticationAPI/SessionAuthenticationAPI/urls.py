from django.contrib import admin
from django.urls import path, include
from student import views
from rest_framework.routers import DefaultRouter


# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='studentapi')
router.register('student', views.StudentROMVS, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
