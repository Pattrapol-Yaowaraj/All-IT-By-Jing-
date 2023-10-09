from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def Home(request):
    return render(request, 'home/home.html')

def Display(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:Home')  # Redirect to the home view after successful login
        else:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'home/display.html')