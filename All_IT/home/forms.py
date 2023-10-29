from django import forms
from accounts.models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['year', 'major']
    MAJOR_CHOICES = [
        ('IT', 'IT'),
        ('DSBA', 'DSBA'),
        ('AIT', 'AIT'),
        ('BIT', 'BIT'),
    ]
    major = forms.ChoiceField(
        choices=MAJOR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save Changes'))
