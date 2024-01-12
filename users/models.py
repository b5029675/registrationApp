from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to = 'profile_pics')
    dateBirth = models.DateField(null = True)
    address = models.CharField(max_length = 20 ,null = True)
    citytown = models.CharField(max_length = 20 ,null = True)
    country = models.CharField(max_length = 20 ,null = True)


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'