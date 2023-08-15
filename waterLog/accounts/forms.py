from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    unit = forms.ChoiceField(choices=UserProfile.UNIT_CHOICES, widget=forms.RadioSelect, initial='ml')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "unit"]

