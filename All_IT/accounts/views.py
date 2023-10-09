from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.http import JsonResponse
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)  # Don't commit yet
            user.save()

            profile = profile_form.save(commit=False)  # Don't commit yet
            profile.user = user  # Associate user with profile
            profile.save()

            return redirect('registration:registration_success')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'account/signup.html', {'user_form': user_form, 'profile_form': profile_form})

def registration_success(request):
    return redirect(reverse('home:Display'))

def validate_credentials(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    # Perform authentication and credential validation here
    # ...

    # For now, let's just return a success response
    return JsonResponse({'success': True})
