from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from userlink.models import UserLink

def Home(request):
    return render(request, 'home/home.html')

def Display(request):
    if request.method == 'POST':
        email = request.POST.get('floatingInput')  # Check the form input names
        password = request.POST.get('floatingPassword')  # Check the form input names

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})

    user_links = UserLink.objects.all()
    return render(request, 'home/display.html', {'user_links': user_links})
