from django import forms
from water.models import WaterConsumption
from django.forms import ModelForm

class WaterConsumptionForm(ModelForm):
    class Meta:
        model= WaterConsumption
        fields=('amount_drank',)