from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    id_no = models.IntegerField()
    city = models.CharField(max_length=100)
