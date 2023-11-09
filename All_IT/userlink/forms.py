from django import forms
from .models import UserLink

class UserLinkForm(forms.ModelForm):
    class Meta:
        model = UserLink
        fields = ['link', 'description', 'sid']
    def __init__(self, *args, **kwargs):
        super(UserLinkForm, self).__init__(*args, **kwargs)