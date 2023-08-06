from django import forms

from water.models import WaterConsumption

class WaterConsumptionForm(forms.ModelsForm):
    class Meta:
        model= WaterConsumption
        fields=('amount_drank',)