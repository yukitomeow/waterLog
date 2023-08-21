from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label=_("Email"),
        help_text=_("Please enter a valid email address.")
    )
    unit = forms.ChoiceField(
        choices=UserProfile.UNIT_CHOICES,
        widget=forms.RadioSelect,
        initial='ml',
        label=_("Unit"),
        help_text=_("Please select your preferred unit.")
    )




# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     unit = forms.ChoiceField(choices=UserProfile.UNIT_CHOICES, widget=forms.RadioSelect, initial='ml')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "unit"]

