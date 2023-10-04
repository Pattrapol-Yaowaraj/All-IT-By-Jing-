from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def Home(request):
    return render(request, 'home/home.html')

def Display(request):
    return render(request, 'home/display.html')