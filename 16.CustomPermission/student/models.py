from django.db import models

# Create your models here.
# superuser
# 1234

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)

# normaluser user:user1, password:superadmin123
# adminuser user:admin, password:superadmin123
