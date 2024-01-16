from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Module(models.Model):
    name = models.CharField(max_length = 15, primary_key = "name")
    code = models.CharField(max_length = 9)
    credit = models.IntegerField(max_length = 2, choices = [('20', '20'), ('40', '40'), ('60', '60')])
    category = models.TextField(max_length = 10, choices = [('Compulsory', 'Compulsory'), ('Elective', 'Elective')])
    description = models.TextField(max_length = 50)
    availability = models.BooleanField(default = True)
    coursesAllowed = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.name}'
    
class Registration(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    module = models.OneToOneField(Module)
    dateRegistered = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


    #room = models.CharField(max_length = 100)
    #details = models.TextField()
    #date_submitted = models.DateTimeField(default = timezone.now)
    #availabile = models.BooleanField(default = True)
    #elCourses = models.CharField(max_length = 100 , choices =
    #[('Hardware', 'Hardware'), ('Software', 'Software')])
