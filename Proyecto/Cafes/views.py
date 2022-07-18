from django.shortcuts import render, redirect
from django.http import HttpResponse
from Cafes.models import *
from . forms import *


def inicio(request):
    return render(request, 'Cafes/index.html', {})

def blogs(request):
    blogs=Blogs.objects.all()
    return render(request, 'Cafes/blogs.html', {"blogs":blogs})

def cafeterias(request):
    cafeterias=Cafeterias.objects.all()
    return render(request,'Cafes/cafeterias.html', {"cafeterias":cafeterias})

def about(request):
    return render(request , 'Cafes/about.html', {})
