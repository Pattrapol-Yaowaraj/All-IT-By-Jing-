from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'sid', 'year', 'major']

    def clean_sid(self):
        sid = self.cleaned_data['sid']
        if UserProfile.objects.filter(sid=sid).exists():
            raise forms.ValidationError("Student ID is already taken.")
        return sid
