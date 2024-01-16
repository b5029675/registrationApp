from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name = models.TextField()

class Module(models.Model):
    name = models.CharField(max_length = 15, primary_key = "name")
    code = models.CharField(max_length = 9)
    credit = models.IntegerField(max_length = 2, choices = [('20', '20'), ('40', '40'), ('60', '60')])
    category = models.TextField(max_length = 10, choices = [('Compulsory', 'Compulsory'), ('Elective', 'Elective')])
    description = models.TextField(max_length = 50)
    availability = models.BooleanField(default = True)
    coursesAllowed = models.ManyToManyField(Course)


    room = models.CharField(max_length = 100)
    details = models.TextField()
    date_submitted = models.DateTimeField(default = timezone.now)
    availabile = models.BooleanField(default = True)
    elCourses = models.CharField(max_length = 100 , choices =
    [('Hardware', 'Hardware'), ('Software', 'Software')])
