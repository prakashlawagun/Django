from django.db import models

# Create your models here.
class Student(models.Model):
    frist_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    