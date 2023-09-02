from django import forms
from water.models import WaterConsumption
from django.forms import ModelForm

class WaterConsumptionForm(ModelForm):
    amount_drank = forms.FloatField(label='', widget=forms.TextInput(attrs={'placeholder': 'Amount Drank'}))

    class Meta:
        model = WaterConsumption
        fields = ('amount_drank',)

