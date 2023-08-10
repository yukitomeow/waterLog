from django import forms
from .models import UserProfile


class MetricSystemForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["metric_system"]
