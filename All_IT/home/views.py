from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from userlink.models import UserLink, LinkForIT
from accounts.models import UserProfile

def Home(request):
    return render(request, 'home/home.html')

def Display(request):
    user_year = request.session.get('user_year', 0)
    user_major = request.session.get('user_major', 'nah')

    if request.method == 'POST':
        email = request.POST.get('floatingInput')
        password = request.POST.get('floatingPassword')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                user_profile = UserProfile.objects.get(user=user)
                user_year = user_profile.year
                user_major = user_profile.major
                request.session['user_year'] = user_year  # Store user_year in the session
                request.session['user_major'] = user_major  # Store user_major in the session
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
