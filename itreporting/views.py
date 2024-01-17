from django.shortcuts import render
from .models import Course, Module
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'itreporting/home.html', {'title':'Home'})

def about(request):
    return render(request, 'itreporting/about.html', {'title':'About'})

def contact(request):
    #if User.is_superuser:
    return render(request, 'itreporting/contact.html', {'title':'Contact'})
    #else:
         #return render(request, 'itreporting/home.html', {'title':'Home'})

def course(request):
    courses = {'courses': Course.objects.all(), 'title': 'Courses'}
    return render(request, 'itreporting/course.html', courses)

def module(request):
    modules = {'modules': Module.objects.all(), 'title': 'Modules'}
    return render(request, 'itreporting/module.html', modules)