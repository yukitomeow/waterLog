from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UNIT_CHOICES = [
        ('ml', 'Milliliters'),
        ('oz', 'Ounces'),
    ]
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='ml')

