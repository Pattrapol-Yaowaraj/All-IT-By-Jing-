from django.shortcuts import render, redirect
from .forms import UserLinkForm
from django.urls import reverse
from .models import UserLink

def input_link(request):
    if request.method == 'POST':
        form = UserLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_links')
    else:
        form = UserLinkForm()
    return render(request, 'userlink/userlink.html', {'form': form})

def display_links(request):
    return redirect(reverse('home:Display'))