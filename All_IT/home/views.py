from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from userlink.models import UserLink, LinkForIT
from accounts.models import UserProfile
from .forms import UserProfileEditForm

def Home(request):
    return render(request, 'home/home.html')

def Delete(request):
    return render(request, 'home/delete.html')

@login_required
def Editprofile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    major_value = user_profile.major

    if request.method == 'POST':
        if 'delete_account' in request.POST:
            user_profile.user.delete()
            logout(request)
            return redirect('home:Delete')

        form = UserProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            request.session['user_year'] = form.cleaned_data['year']
            request.session['user_major'] = form.cleaned_data['major']
            return redirect('home:Display')
    else:
        form = UserProfileEditForm(instance=user_profile)

    return render(request, 'home/edit.html', {'form': form, 'user_profile'\
                                              : user_profile, 'major_value': major_value})

def Display(request):
    user_year = request.session.get('user_year', 0)
    user_major = request.session.get('user_major', 'nah')
    user_sid = request.session.get('user_sid', '0')
    user_profile = UserProfile.objects.filter(year=user_year, major=user_major, sid=user_sid).first()

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
                user_sid = user_profile.sid
                request.session['user_year'] = user_year
                request.session['user_major'] = user_major
                request.session['user_sid'] = user_sid
                links_for_user = list(LinkForIT.objects.filter(year=user_year, major=user_major).values())
                return JsonResponse({'valid': True, 'user_year': user_year, 'user_major': user_major\
                                     , 'links_for_user': links_for_user, 'user_sid':user_sid})
            except UserProfile.DoesNotExist:
                return JsonResponse({'valid': False, 'error': 'UserProfile does not exist for this user.'})
        else:
            return JsonResponse({'valid': False, 'error': 'Authentication failed.'})

    user_links = UserLink.objects.filter(sid=user_sid)
    links_for_user = LinkForIT.objects.filter(year=user_year, major=user_major)
    return render(request, 'home/display.html', {'user_links': user_links, 'links_for_user'\
                                                 : links_for_user, 'user_sid': user_sid})

def Logout(request):
    logout(request)
    return redirect('home:Home')