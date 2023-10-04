from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'home/home.html')

def Display(request):
    return render(request, 'home/display.html')

def Signup(request):
    return render(request, 'home/signup.html')
