from django import forms
from django.contrib.auth.models import User
from itreporting.models import Course
from django.contrib.auth.forms import UserCreationForm
from .models import Student


COURSES = [
    ('BSc Cyber Security','BSc Cyber Security'),
    ('BSc Information Technology','BSc Information Technology'),
    ('BSc Smart Computing','BSc Smart Computing')
]
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True, empty_label = 'Select Course', label = 'Your Course')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'course', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['image', 'dateBirth', 'address', 'citytown', 'country']
