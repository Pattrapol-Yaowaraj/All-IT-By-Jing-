from django import forms
from accounts.models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['year', 'major']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save Changes'))
