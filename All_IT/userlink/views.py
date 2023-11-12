from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserLinkForm
from accounts.models import UserProfile
from .models import UserLink
from django.http import JsonResponse

@login_required
def userlink(request, user_sid):
    user_profile = get_object_or_404(UserProfile, sid=user_sid)

    if request.method == 'POST':
        form = UserLinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            description = form.cleaned_data['description']
            user = request.user
            UserLink.objects.create(link=link, description=description\
                                    , sid=user_sid, user=user)

            return redirect('home:Display')
    else:
        form = UserLinkForm()

    return render(request, 'userlink/userlink.html', {'form': form, 'sid': user_sid})

@login_required
def delete_link(request, link_id):
    link = get_object_or_404(UserLink, id=link_id)
    if link.sid == request.session.get('user_sid', '0'):
        link.delete()
    return redirect('home:Display')