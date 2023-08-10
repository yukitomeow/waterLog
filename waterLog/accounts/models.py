from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    metric_system = models.CharField(
        max_length=2, choices=[("ml", "Milliliters"), ("oz", "Ounces")], default="ml"
    )
