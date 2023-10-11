from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.http import JsonResponse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data['username']
            sid = request.POST.get('sid')  # Correctly get sid from POST data
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('registration:register')

            if UserProfile.objects.filter(sid=sid).exists():
                messages.error(request, 'Student ID is already taken.')
                return redirect('registration:register')

            user = user_form.save(commit=False)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('registration:registration_success')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'account/signup.html', {'user_form': user_form, 'profile_form': profile_form})
def registration_success(request):
    return redirect(reverse('home:Home'))

def validate_credentials(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    return JsonResponse({'success': True})
