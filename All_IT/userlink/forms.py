from django import forms
from .models import UserLink

class UserLinkForm(forms.ModelForm):
    class Meta:
        model = UserLink
        fields = ['url', 'description']