from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class WaterConsumption(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount_drank = models.FloatField(default=0)
    date = models.DateField(default=timezone.now)

    # @staticmethod
    # def find_by_user_username(username):
    #     return WaterConsumption.objects.get(user__username=username)
        
    def __str__(self):
        return f"User: {self.user}, Amount Drank: {self.amount_drank}, Date: {self.date}"

