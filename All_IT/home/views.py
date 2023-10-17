from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from userlink.models import UserLink, LinkForIT
from accounts.models import UserProfile
from .forms import UserProfileEditForm

def Home(request):
    return render(request, 'home/home.html')

@login_required
def editprofile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            request.session['user_year'] = form.instance.year
            request.session['user_major'] = form.instance.major
            request.session.save()
            return redirect('home:Display')
    else:
        form = UserProfileEditForm(instance=user_profile)

    return render(request, 'home/edit.html', {'form': form})

def Display(request):
    user_year = request.session.get('user_year', 0)
    user_major = request.session.get('user_major', 'nah')

    user_profile = UserProfile.objects.filter(year=user_year, major=user_major).first()

    if request.method == 'POST':
        email = request.POST.get('floatingInput')
        password = request.POST.get('floatingPassword')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                if user_profile is None:
                    user_profile = UserProfile.objects.get(user=user)
                user_year = user_profile.year
                user_major = user_profile.major
                request.session['user_year'] = user_year
                request.session['user_major'] = user_major
                user_links = list(UserLink.objects.all().values())
                links_for_user = list(LinkForIT.objects.filter(year=user_year, major=user_major).values())
                return JsonResponse({'valid': True, 'user_year': user_year, 'user_major': user_major, 'user_links': user_links, 'links_for_user': links_for_user})
            except UserProfile.DoesNotExist:
                return JsonResponse({'valid': False, 'error': 'UserProfile does not exist for this user.'})
        else:
            return JsonResponse({'valid': False, 'error': 'Authentication failed.'})

    user_links = UserLink.objects.all()
    links_for_user = LinkForIT.objects.filter(year=user_year, major=user_major)
    return render(request, 'home/display.html', {'user_links': user_links, 'links_for_user': links_for_user})
